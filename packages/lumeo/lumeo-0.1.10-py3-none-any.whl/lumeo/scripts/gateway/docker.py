import shutil
import platform
import json
import os
import docker
import requests
import subprocess

from .display import print_text, prompt_yes_no, prompt_input, output_message
from .host_utils import run_command, apt_install
from .nvidia import l4t_version


DOCKER_CONFIG_FILE = "/etc/docker/daemon.json"
DOCKER_CLIENT = docker.from_env()
LUMEO_WATCHTOWER_VERSION = "2"


def check_container_exists(container_name):
    all_containers = DOCKER_CLIENT.containers.list(all=True)
    for container in all_containers:
        if container_name == container.name:
            return True
    return False


def install_docker_and_nvidia_toolkit():
    """Install Docker and NVIDIA toolkit if necessary."""
    if shutil.which("docker") is None:
        apt_install("docker.io containerd", update_first=True)
    
    run_command("systemctl start docker", sudo=True)
    
    arch_type = platform.machine()
    l4t_ver = l4t_version() if arch_type == "aarch64" else None
    
    if arch_type == "x86_64" or (arch_type == "aarch64" and l4t_ver and l4t_ver >= "36"):
        if not run_command("dpkg-query -W -f='${Status}' nvidia-container-toolkit", check=False):
            apt_install("curl gnupg", update_first=True)
            run_command("curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg --yes", shell=True)
            run_command("curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list > /dev/null", shell=True)
            apt_install("nvidia-container-toolkit", update_first=True)
            run_command("nvidia-ctk runtime configure --runtime=docker", sudo=True)
            run_command("systemctl restart docker", sudo=True)
    
    elif arch_type == "aarch64" and l4t_ver and l4t_ver < "36":
        if not run_command("dpkg -l nvidia-docker2", check=False):
            apt_install("nvidia-docker2", update_first=True)
            run_command("systemctl restart docker", sudo=True)


def stop_and_remove_docker_containers(container_prefix="lumeo/gateway", silent=False):
    """Stop and remove Docker containers with image name starting with the specified prefix."""    
    print_text(f"Checking for running Docker containers with image name starting with '{container_prefix}'. Will stop and remove.")    
    docker_containers = run_command(f"docker ps -a --format '{{{{.Image}}}} {{{{.ID}}}}' | grep '^{container_prefix}' | awk '{{print $2}}'", sudo=True)
    
    if docker_containers:
        if not silent:
            print_text("Stopping and removing Docker containers...")
        for container in docker_containers.split():
            run_command(f"docker stop {container}", sudo=True)
            run_command(f"docker rm -v {container}", sudo=True)
    else:
        print_text(f"No Docker containers with image name starting with '{container_prefix}' found.")
        
        

def check_set_docker_data_dir():
    
    move_docker_data_dir = prompt_yes_no("Use external drive to store the Docker data directory? (for docker images & volumes)? (Recommended if your root partition is smaller than 32 GB). Check instructions how to mount the external drive in https://docs.lumeo.com/. Proceed?", "n")
    
    if move_docker_data_dir:
        
        external_folder = prompt_input("Enter the path to the external drive where Docker data directory will be moved. (e.g. /mnt/nvme1n1p1)")
        
        original_folder = run_command("docker info -f '{{ .DockerRootDir}}'", sudo=True)

        if not os.path.isdir(external_folder):
            print(f"Error: Directory '{external_folder}' does not exist. Please make sure the external drive is correctly mounted.")
            exit(1)

        run_command("systemctl stop docker docker.socket containerd", sudo=True)

        if os.path.isdir(original_folder):
            available_space = int(run_command(f"df -P {external_folder} | awk 'END{{print $4}}'", sudo=True))
            original_folder_size = int(run_command(f"du -s {original_folder} | awk '{{print $1}}'", sudo=True))

            if original_folder_size > available_space:
                print(f"Error: There's not enough space on '{external_folder}' to move the contents of '{original_folder}'")
                run_command("systemctl start docker", sudo=True)
                exit(1)
            else:
                print(f"Moving the contents of '{original_folder}' to '{external_folder}/docker'. Please wait a moment...")
                run_command(f"cp -rp {original_folder} {external_folder}", sudo=True)
        else:
            print(f"Error: Directory '{original_folder}' does not exist. Please make sure Docker is correctly installed.")
            run_command("systemctl start docker", sudo=True)
            exit(1)

        run_command(f"mv {original_folder} {original_folder}.old", sudo=True)
        update_docker_data_directory(f"{external_folder}/docker")
        print(f"Successfully updated docker daemon data folder to '{external_folder}/docker'. Backups can be found in '{original_folder}.old' directory")
        run_command("systemctl start docker", sudo=True)
        
        
def update_docker_data_directory(docker_data_folder):
    print("[lumeo-container-manager] Updating docker daemon data-root")
    docker_config_file = "/etc/docker/daemon.json"

    with open(docker_config_file, "r") as json_file:
        docker_config = json.load(json_file)
        docker_config["data-root"] = docker_data_folder

    with open(docker_config_file, "w") as json_file:
        json.dump(docker_config, json_file)

        
# Sets up logging configuration for docker daemon.
# This applies only to newly created containers. 
# During lumeod update, the container gets re-created.
def set_docker_logs_configuration():
    # Check if the file exists
    if os.path.isfile(DOCKER_CONFIG_FILE):
        # If the file exists, open it and load the JSON data
        with open(DOCKER_CONFIG_FILE, 'r') as f:
            config = json.load(f)
    else:
        # If the file doesn't exist, create an empty dictionary to use as the config
        config = {}

    # If we had already set this, exit.
    if "log-opts" in config:
        print(f"'log-opts' are already set to {config['log-opts']}, exiting ...")
        return

    # Add the "log-opts" entry to the config
    config["log-opts"] = {
        "max-size": "10m",
        "max-file": "1"
    }

    # Write the config back to the file
    with open(DOCKER_CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

    print("Docker config updated, restarting docker daemon ...")
    run_command("systemctl restart docker", sudo=True)
    print("Done.")
    
    
# This fixes "Failed to initialize NVML: Unknown Error".
# The error happens when someone (usually apt) does `systemctl daemon-reload`.
# GPUs disappear from the container but still available on the host and lumeod container restart helps.
# The official workaround is to switch back to the old `cgroups` implementation: `cgroupfs`.
# For more information see:
# - https://github.com/NVIDIA/nvidia-docker/issues/1730
# - https://github.com/NVIDIA/nvidia-docker/issues/1671
# TODO: switch this back when NVIDIA releases the correct way to deal with this.
def fix_nvidia_nvml_init_issue():
    # TODO: Don't do this on OpenVINO when we have more precise platform specification.
    arch_type = platform.machine()
    if arch_type != "x86_64":
        print("Only x86 is affected, exiting ...")
        return

    # Check if the file exists
    if os.path.isfile(DOCKER_CONFIG_FILE):
        # If the file exists, open it and load the JSON data
        with open(DOCKER_CONFIG_FILE, 'r') as f:
            config = json.load(f)
    else:
        # If the file doesn't exist, create an empty dictionary to use as the config
        config = {}

    # If we had already set this, exit.
    # If someone else had set 'exec-opts', let's exit as well not to mess things up.
    if "exec-opts" in config:
        print(f"'exec-opts' are already set to {config['exec-opts']}, exiting ...")
        return

    # Add the "exec-opts" entry to the config
    config["exec-opts"] = ["native.cgroupdriver=cgroupfs"]

    # Write the config back to the file
    with open(DOCKER_CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

    print("Docker config updated, restarting docker daemon ...")
    run_command("systemctl restart docker", sudo=True)
    print("Done.")
    
    

def start_watchtower():
    watchtower_name = "lumeo-watchtower"
    if not DOCKER_CLIENT.containers.list(all=True, filters={"name": watchtower_name}):
        watchtower_labels = {
            "lumeo.container_version": LUMEO_WATCHTOWER_VERSION,
            "lumeo.container_type": "containrrr/watchtower",
        }
        DOCKER_CLIENT.containers.run(
            "containrrr/watchtower:1.4.0",
            command=["--http-api-update", "--http-api-token", "lumeo-container-update-watchtower-token",
                     "--label-enable", "--include-stopped", "--cleanup"],
            volumes=["/var/run/docker.sock:/var/run/docker.sock"],
            restart_policy={"MaximumRetryCount": 0, "Name": "always"},
            name=watchtower_name,
            labels=watchtower_labels,
            ports={'8080/tcp': ('127.0.0.1', 46655)},
            detach=True,
        )


# Re-creates watchtower if the current version is other than LUMEO_WATCHTOWER_VERSION
def migrate_watchtower():
    try:
        # Get the watchtower container
        watchtower = DOCKER_CLIENT.containers.get("lumeo-watchtower")

        # Get the current version of the watchtower container
        current_version = watchtower.attrs["Config"]["Labels"]["lumeo.container_version"]

        # Migrate 1 to 2.
        if current_version == "1":
            # Remove the existing watchtower container
            watchtower.remove(force=True)

            # Start a new watchtower container with the updated version
            start_watchtower()

            output_message("Watchtower migrated to the latest version.", "success")
        else:
            output_message("Watchtower is already up to date.", "info")
    except docker.errors.NotFound:
        output_message("Watchtower container not found.", "info")
    except (KeyError, ValueError):
        output_message("Error parsing watchtower version.", "error")
    except Exception as e:
        output_message(f"Error migrating watchtower: {str(e)}", "error")


def watchtower_trigger_update():
    print("Checking for updates in Lumeo containers images")
    # Ask watchtower to check for container image updates
    token = "lumeo-container-update-watchtower-token"
    final_url = "http://localhost:46655/v1/update"
    headers_api = {
        "Authorization": "Bearer " + token
    }
    try:
        requests.get(url=final_url, headers=headers_api)
    except Exception as err:
        output_message("[lumeo-container-update] Exception: {}".format(err), "error")

