import argparse
import os
import sys

from lumeo.utils import check_for_update
from .display import print_header, prompt_input, set_output_format, generate_table, print_text
from .lumeod import list_containers, install_container, download_container, get_lumeo_containers, stop_container, upgrade_and_restart_container, remove_container, logs, shell, update_containers, write_hardware_information_to_container
from .wgm import install_wgm, reset_wgm, update_wgm
from .schedule import edit_update_schedule
from .docker import start_watchtower, migrate_watchtower, set_docker_logs_configuration, fix_nvidia_nvml_init_issue


NO_PROVISION = os.environ.get('NO_PROVISION', False)
def exit_manager():
    sys.exit(0)


COMMANDS = {
    "list": ("List the currently installed Lumeo gateway containers", list_containers, True),
    "install": ("Install a new Lumeo gateway container", install_container, True),
    "download": ("Download the latest Lumeo gateway container image (OEM use only)", download_container, True),
    "stop": ("Kills a running Lumeo gateway container", stop_container, True),
    "restart": ("Restart a Lumeo gateway container & update to the latest version", upgrade_and_restart_container, True),
    "update": ("Update all Lumeo gateway containers to the latest image", update_containers, True),
    "remove": ("Remove a Lumeo gateway container", remove_container, True),
    "logs": ("Print the logs of a Lumeo gateway container", logs, True),
    "shell": ("Open an interactive shell in a running Lumeo gateway container", shell, True),

    "schedule": ("Schedule container update in a certain date range", edit_update_schedule, True),
    
    "install-wgm": ("Install Web Gateway Manager", install_wgm, True),
    "update-wgm": ("Update Web Gateway Manager", update_wgm, True),
    "reset-wgm": ("Reset Web Gateway Manager", reset_wgm, True),
    
    "fix_nvidia_driver_issue": ("Fix the issue with the NVIDIA driver", fix_nvidia_nvml_init_issue, False),
    "set_docker_logs_configuration": ("Set the Docker logs configuration", set_docker_logs_configuration, False),
    "write_hardware_information": ("Write the hardware information to a file", write_hardware_information_to_container, False),
    
    "start_watchtower": ("Start Watchtower", start_watchtower, False),
    "migrate_watchtower": ("Migrate Watchtower", migrate_watchtower, False),
    
    "exit": ("Quits this script", exit_manager, True),
}

def print_usage():
    update_info = check_for_update()
    print_text("")
    print_header(get_usage(), f"Lumeo Gateway Manager v{update_info[2]}")

def get_usage():
    headers = ["Command", "Description"]
    rows = [
        [command_name, description]
        for command_name, (description, _, show_in_menu) in COMMANDS.items()
        if show_in_menu
    ]
    return generate_table(headers, rows, "Commands")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=COMMANDS.keys(), nargs="?")
    parser.add_argument("--container-name")
    parser.add_argument("--force-update", action="store_true", help="Force update without checking schedule")
    parser.add_argument("--script", action="store_true", help="Script mode. Uses defaults, does not prompt for input", default=False)
    parser.add_argument("--output", choices=['json', 'table'], default="table", help="Output format")

    args = parser.parse_args()

    if not args.script:
        set_output_format(args.output)
        containers_list = get_lumeo_containers()

        if not containers_list:
            if NO_PROVISION:
                # pull the latest version of lumeo image, but not attempt to install it
                #os.system("sudo docker pull {}".format(LUMEO_IMAGE))
                download_container()
            else:
                # start a new container installation if no containers are found
                install_container()
                sys.exit(0)

        print_usage()

        # if Lumeo containers are found, we list them
        list_containers()

        while True:
            try:
                user_option = prompt_input("Enter the command")
                if user_option in COMMANDS:
                    COMMANDS[user_option][1]()
                else:
                    print("Error: Command is not recognized! Please select a valid command\n")
                    print_usage()
            except KeyboardInterrupt:
                sys.exit(0)
    else:
        set_output_format('json')
        # Perform a single operation and exit
        if args.container_name and args.command in ["stop", "restart", "remove", "logs", "shell", "wgm",
                                                    "write_hardware_information"]:
            COMMANDS[args.command][1](args.container_name)
        elif args.force_update and args.command == "update":
            COMMANDS[args.command][1](args.force_update)
        else:
            COMMANDS[args.command][1]()
            
            
if __name__ == "__main__":
    main()