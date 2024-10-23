import os
import shutil
import subprocess
import json
import sys
import time

from rich.progress import Progress

from .display import prompt_yes_no, print_text

# Common host utilities
def check_os():
    """Check if the OS is Linux."""
    if os.name != "posix" or os.uname().sysname != "Linux":
        print_text("[bold red]Error:[/bold red] This script must be run on a Linux system.")
        sys.exit(1)

def run_command(command, check=True, shell=True, sudo=False, error_message=None, useOsRun=False):
    """Run a command and return its output."""
    try:
        command_name = command.split()[0]  # Get the name of the command
        if shutil.which(command_name) is None:  # Check if the command is available
            print_text(f"[bold red]Command '{command}' not found.[/bold red]")
            return None                
        
        if sudo:
            command = f"sudo {command}"
        
        if not shell:
            command = command.split()
            
        if useOsRun:
            result = os.system(command)
            return result
        else:
            result = subprocess.run(command, check=check, shell=shell, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print_text(f"[bold red]Error executing command: {e}[/bold red]")
        print_text(f"[bold red]Command output:[/bold red] {e.output}")
        print_text(f"[bold red]Command error:[/bold red] {e.stderr}")
        if error_message:
            print_text(f"[bold red]{error_message}[/bold red]")
        sys.exit(1)

def check_lock(command):
    """Check for apt/dpkg locks and wait if necessary."""
    max_attempts = 300
    with Progress() as progress:
        task = progress.add_task("[cyan]Waiting for locks to be released...", total=max_attempts)
        for i in range(max_attempts):
            if not run_command("sudo fuser /var/lib/dpkg/lock /var/lib/apt/lists/lock /var/cache/apt/archives/lock", check=False):
                break
            progress.update(task, advance=1)
            time.sleep(1)
        else:
            print_text("[bold red]Error:[/bold red] Unable to acquire lock after 5 minutes. Aborting installation.")
            sys.exit(1)
    
    run_command(command, shell=True, sudo=True)

def apt_install(packages, update_first=False):
    """Install packages using apt, optionally updating first."""
    if update_first:
        check_lock("apt update")
    check_lock(f"apt install -y {packages}")


# Install host packages
def setup_host_common():
    apt_install("curl jq python3 lshw util-linux smartmontools", update_first=True)

        

def prompt_disable_x_server():
    """Prompt to disable X server and return whether a reboot is required."""
    if prompt_yes_no("[Optional] Disable GUI (X server) to free up memory, allowing you to run more pipelines? (reboot required)", "n"):
        run_command("systemctl enable multi-user.target", sudo=True)
        run_command("systemctl set-default multi-user.target", sudo=True)
        return "In order to turn off GUI (X server), a reboot is required"
    return None


def toggle_ssh(enable=False):
    """Enable or disable SSH."""
    action = "enable" if enable else "disable"
    if prompt_yes_no(f"Do you want to {action} SSH?", "n"):
        print_text(f"{'Enabling' if enable else 'Disabling'} SSH...")
        run_command(f"systemctl {action} ssh", sudo=True)
        print_text(f"SSH has been {action}d.")
    else:
        print_text("Operation cancelled.")


def toggle_user_lock(username, lock=True):
    """Lock or unlock the user account."""    
    action = "lock" if lock else "unlock"
    if prompt_yes_no(f"Do you want to {action} the password for user {username}?", "n"):
        print_text(f"{'Locking' if lock else 'Unlocking'} password for user {username}...")
        run_command(f"passwd -{action[0]} {username}", sudo=True)
        print_text(f"User {username} has been {action}ed.")
    else:
        print_text("Operation cancelled.")
        

def check_disk_space():
    docker_data_folder = run_command("docker info -f '{{ .DockerRootDir}}'", sudo=True)
    if os.path.isdir(docker_data_folder):
        arch_type = os.uname().machine
        required_size_KB = 8388608 if arch_type == "aarch64" else 20971520

        available_space_KB = int(run_command(f"df -P {docker_data_folder} | awk 'END{{print $4}}'", sudo=True))

        if available_space_KB < required_size_KB:
            required_size_GB = required_size_KB / (1024 ** 2)
            available_space_GB = available_space_KB / (1024 ** 2)

            print("WARNING: There is not enough free space on the disk where Docker stores its data.")
            print(f"You have {available_space_GB:.2f} GB available, but at least {required_size_GB:.2f} GB is required for fresh lumeod installations.")
            print("If the container image has not been pulled yet, or lumeod is not installed, you might run out of disk space during installation.")

            if prompt_yes_no("Do you want to continue despite the low disk space?", "n"):
                print("Proceeding despite the low disk space warning.")
            else:
                print("Exiting due to insufficient disk space.")
                exit(1)
