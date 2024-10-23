import platform
import subprocess
import os
import json
import argparse
import threading
from typing import List
import base64

from . import container_utils

from pyntcli.ui import ui_thread
from pyntcli.analytics import send as analytics
from pyntcli.store import CredStore
from pyntcli.auth.login import PYNT_ID, PYNT_SAAS, PYNT_BUCKET_NAME, PYNT_PARAM1, PYNT_PARAM2

PYNT_DOCKER_IMAGE = "ghcr.io/pynt-io/pynt"
IMAGE_TAGS = ["postman-latest", "newman-latest", "har-latest", "proxy-latest", "v1-latest"]

PYNT_CONTAINER_INTERNAL_PORT = "5001"


def create_mount(src, destination, mount_type="bind"):
    return {
        'Target': destination,
        'Source': src,
        'Type': mount_type,
        'ReadOnly': False,
        'NoCopy': False,
    }


class DockerNotAvailableException(Exception):
    pass


class DockerNativeUnavailableException(Exception):
    pass


class ImageUnavailableException(Exception):
    pass


class PortInUseException(Exception):
    def __init__(self, port=""):
        self.message = ui_thread.print(
            ui_thread.PrinterText(f"Port: {port} already in use, please use a different one", ui_thread.PrinterText.WARNING))
        super().__init__(self.message)


def get_docker_platform_name():
    try:
        version_data = json.loads(subprocess.check_output(["docker", "version", "--format", "{{json .}}"], text=True))
        platform = version_data.get("Server", {}).get("Platform", {})
        analytics.deferred_emit(analytics.DOCKER_PLATFORM, platform)
        return platform.get("Name", "")
    except Exception:
        raise DockerNotAvailableException()


class PyntBaseContainer():
    def __init__(self, docker_type, docker_arguments, mounts, environment={}) -> None:
        self.docker_type = docker_type
        self.docker_arguments = docker_arguments
        self.mounts = mounts
        self.environment = environment


class PyntDockerPort:
    def __init__(self, src, dest, name) -> None:
        self.src = src
        self.dest = dest
        self.name = name


class PyntDockerImage:
    def __init__(self, name, is_self_managed) -> None:
        self.name = name
        self.is_self_managed = is_self_managed


class DockerContainerConfig:
    def __init__(self, args: argparse.Namespace, integration_name: str, *port_args: PyntDockerPort):
        self.image = get_image_config(args)
        self.is_detach = True
        self.ports = port_args
        self.docker_arguments = build_docker_args(integration_name, args)
        self.mounts = get_docker_mounts(args)
        self.env_vars = {PYNT_ID: CredStore().get_tokens(), "PYNT_SAAS_URL": PYNT_SAAS}
        if user_set_all_variables():
            add_env_variables(self.env_vars)

        ports = {}
        create_network_host = is_network_host()
        for p in port_args:
            if create_network_host:
                self.docker_arguments.append(p.name)
                self.docker_arguments.append(str(p.dest))
            else:
                # `dest` is the host port, `src` is in the container
                ports[str(p.dest)] = int(p.src)

        if create_network_host:
            self.docker_type = PyntNativeHost(network="host")
        else:
            self.docker_type = PyntDockerDesktopContainer(ports=ports)


def get_image_config(args: argparse.Namespace) -> PyntDockerImage:
    default_image = f'{PYNT_DOCKER_IMAGE}:v1-latest'
    if "pynt_image" in args and args.pynt_image:
        return PyntDockerImage(args.pynt_image, True)
    env_name = value_from_environment_variable("IMAGE")
    env_tag = value_from_environment_variable("TAG")
    if env_name:
        return PyntDockerImage(f'{env_name}:{env_tag}', True)

    return PyntDockerImage(default_image, False)


def is_network_host() -> bool:
    platform_sys_name = platform.system()
    if platform_sys_name == "Windows" or platform_sys_name == "Darwin":
        return False
    else:
        docker_platform_name = get_docker_platform_name().lower()
        if "desktop" in docker_platform_name:
            return False
        return True


def user_set_all_variables():
    return all([PYNT_BUCKET_NAME, PYNT_PARAM1, PYNT_PARAM2])


def add_env_variables(env: dict):
    env["PYNT_BUCKET_NAME"] = PYNT_BUCKET_NAME
    env["PYNT_PARAM1"] = base64.b64encode(PYNT_PARAM1.encode('utf-8'))
    env["PYNT_PARAM2"] = base64.b64encode(PYNT_PARAM2.encode('utf-8'))


def value_from_environment_variable(key):
    e = os.environ.get(key)

    if e:
        ui_thread.print_verbose(f"Using environment variable {key}={e}")
        return e

    return None


def build_docker_args(integration_name:str, args: argparse.Namespace) -> list[str]:
    docker_arguments = [integration_name]

    if "insecure" in args and args.insecure:
        docker_arguments.append("--insecure")

    if "application_id" in args and args.application_id:
        docker_arguments += ["--application-id", args.application_id]

    if "proxy" in args and args.proxy:
        docker_arguments += ["--proxy", args.proxy]

    if "dev_flags" in args:
        docker_arguments += args.dev_flags.split(" ")

    if "host_ca" in args and args.host_ca:
        ca_name = os.path.basename(args.host_ca)
        docker_arguments += ["--host-ca", ca_name]

    if "transport_config" in args and args.transport_config:
        tc_name = os.path.basename(args.transport_config)
        docker_arguments += ["--transport-config", tc_name]

    if "verbose" in args and args.verbose:
        docker_arguments.append("--verbose")

    return docker_arguments


def get_docker_mounts(args: argparse.Namespace) -> list:
    mounts = []
    if "host_ca" in args and args.host_ca:
        ca_name = os.path.basename(args.host_ca)
        mounts.append(create_mount(os.path.abspath(args.host_ca), "/etc/pynt/{}".format(ca_name)))

    if "transport_config" in args and args.transport_config:
        tc_name = os.path.basename(args.transport_config)
        mounts.append(create_mount(os.path.abspath(args.transport_config), "/etc/pynt/{}".format(tc_name)))

    return mounts


class PyntContainerNative:
    def __init__(self, container_config: DockerContainerConfig):
        self.config = container_config
        self.container_name = "pynt_engine"
        self.system = platform.system().lower()
        self.stdout = None
        self.running = False

        creds_path = os.path.dirname(CredStore().file_location)
        mitm_cert_path = os.path.join(creds_path, "cert")
        os.makedirs(mitm_cert_path, exist_ok=True)
        self.config.mounts.append(create_mount(mitm_cert_path, "/root/.mitmproxy"))

    def is_alive(self):
        command = ["docker", "ps", "--filter", f"name={self.container_name}", "--filter", "status=running"]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        return len(result.stdout.splitlines()) > 1

    def prepare_client(self):
        pass

    def run(self):
        self.running = True

        self.fetch_and_validate_image()
        args = self.config.docker_arguments if self.config.docker_arguments else None
        docker_command = ["docker", "run", "--rm", "-d", "--name", self.container_name]

        mounts = []
        for mount in self.config.mounts:
            mounts.extend(["-v", f"{mount['Source']}:{mount['Target']}"])

        env_vars = []
        for key, value in self.config.env_vars.items():
            env_vars.extend(self.adapt_environment_variable_partial(key, value))

        docker_type_options = []
        for key, value in self.config.docker_type.get_arguments().items():
            if key == "ports" and isinstance(value, dict):
                for host_port, container_port in value.items():
                    # --publish HOST_PORT:CONTAINER_PORT for each port
                    docker_type_options.extend(["-p", f"{host_port}:{container_port}"])
            else:
                docker_type_options.extend([f"--{key}={value}"])

        docker_command += mounts
        docker_command += env_vars
        docker_command += docker_type_options
        docker_command += [f"{self.config.image.name}"]
        docker_command += args

        command = self.adapt_run_command(docker_command)
        PyntContainerRegistry.instance().register_container(self)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if stderr:
            print(stderr)

        container_id = stdout.strip()

        if process.returncode and process.returncode != 0:
            raise DockerNativeUnavailableException(f"Unable to perform docker run command, return code: {process.returncode}")

        # Start log streaming in a separate thread
        if ui_thread.VERBOSE:
            log_thread = threading.Thread(target=self.stream_docker_logs, args=(container_id,))
            log_thread.daemon = True
            log_thread.start()

    def stream_docker_logs(self, container_id):
        logs_process = subprocess.Popen(
            ['docker', 'logs', '-f', container_id],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        while True:
            log_output = logs_process.stdout.readline()
            if log_output == '' and logs_process.poll() is not None:
                break
            if log_output:
                print(log_output.strip())

        logs_process.stdout.close()

    def kill_other_instances(self, report_to_user=True):
        ui_thread.print_verbose("Killing other pynt containers if such exist")
        try:
            for _ in IMAGE_TAGS:
                command = ["docker", "ps", "-a", "-q", "-f", f"name={self.container_name}"]
                containers_output = subprocess.check_output(command, text=True)
                if not containers_output:
                    continue

                container_ids = containers_output.splitlines()
                for container_id in container_ids:
                    kill_command = ["docker", "kill", container_id]
                    remove_command = ["docker", "remove", container_id]
                    subprocess.run(kill_command,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    subprocess.run(remove_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    if report_to_user:
                        ui_thread.print(
                            ui_thread.PrinterText("Another Pynt container was running, killed it", ui_thread.PrinterText))

        except subprocess.CalledProcessError:
            analytics.emit(analytics.ERROR, {"error": "Unable to kill other pynt containers"})
            ui_thread.print(ui_thread.PrinterText("Error: Unable to kill other pynt containers", ui_thread.PrinterText.WARNING))

    def fetch_and_validate_image(self):
        try:
            ui_thread.print(ui_thread.PrinterText("Pulling latest docker image", ui_thread.PrinterText.INFO))
            pull_command = ['docker', 'pull', self.config.image.name]
            get_image_command = ['docker', 'images', '-q', f'{self.config.image.name}']
            pull_process = subprocess.Popen(pull_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            _, pull_stderr = pull_process.communicate()
            get_process = subprocess.Popen(get_image_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            get_stdout, _ = get_process.communicate()
            local_image_id = get_stdout.decode('utf-8')
            if self.config.image.is_self_managed and local_image_id:
                return local_image_id.strip()
            elif local_image_id == "":
                ui_thread.print(ui_thread.PrinterText(f"Error: the image {self.config.image.name} not found",
                                                      ui_thread.PrinterText.WARNING))
                raise ImageUnavailableException("Failed to find local image")
            if pull_stderr and local_image_id == "":
                ui_thread.print(ui_thread.PrinterText(f"Error: {pull_stderr}", ui_thread.PrinterText.WARNING))
                raise ImageUnavailableException("Failed to pull image")

            if pull_process.returncode != 0:
                raise ImageUnavailableException("Failed to pull image")
        except Exception as e:
            raise ImageUnavailableException(f"An error occurred: {str(e)}")

    def stop(self):
        if not self.running:
            return
        self.kill_other_instances(report_to_user=False)
        self.running = False

    def adapt_run_command(self, docker_command=[]):
        if self.system == "windows":
            return ' '.join(docker_command)
        return docker_command

    def adapt_environment_variable_partial(self, key, value):
        if self.system == "windows":
            return ["-e", f"{key}={json.dumps(value)}"]
        return ["-e", f"{key}={value}"]

    def pre_run_validation(self, port):
        self.kill_other_instances()

        if container_utils.is_port_in_use(int(port)):
            raise PortInUseException(port)


class PyntDockerDesktopContainer:
    def __init__(self, ports) -> None:
        self.ports = ports

    def get_arguments(self):
        return {"ports": self.ports} if self.ports else {}


class PyntNativeHost:
    def __init__(self, network) -> None:
        self.network = network

    def get_arguments(self):
        return {"network": self.network} if self.network else {}


class PyntContainerRegistry:
    _instance = None

    def __init__(self) -> None:
        self.containers: List[PyntContainerNative] = []

    @staticmethod
    def instance():
        if not PyntContainerRegistry._instance:
            PyntContainerRegistry._instance = PyntContainerRegistry()

        return PyntContainerRegistry._instance

    def register_container(self, c: PyntContainerNative):
        self.containers.append(c)

    def stop_all_containers(self):
        for c in self.containers:
            c.stop()
