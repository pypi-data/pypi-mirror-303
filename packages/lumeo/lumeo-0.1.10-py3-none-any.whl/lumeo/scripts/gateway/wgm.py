import os
import platform

from .host_utils import run_command
from .common import install_common_dependencies
from .display import print_text, print_header
from .updater import install_gateway_updater

def install_wgm():
    """Install Lumeo Web Gateway Manager."""    
    arch_type = platform.machine()
    
    install_common_dependencies()
        
    # Create shared volume directory
    os.makedirs("/opt/lumeo/wgm", exist_ok=True)    
    
    # Install WGM container
    wgm_container = "lumeo/wgm-x64:latest" if arch_type == "x86_64" else "lumeo/wgm-arm:latest"

    # Remove existing lumeo_wgm container
    if run_command("docker ps -a -q -f name=lumeo_wgm", sudo=True, check=False):
        run_command("docker stop lumeo_wgm", sudo=True)
        run_command("docker rm lumeo_wgm", sudo=True)
        run_command("rm -rf /opt/lumeo/wgm", sudo=True)

    # Pull and run new container
    run_command(f"docker pull {wgm_container}", sudo=True)
    run_command(f"docker run -d -v /opt/lumeo/wgm/:/lumeo_wgm/ --name lumeo_wgm --restart=always --network host {wgm_container}", sudo=True)

    # Install and start lumeo-wgm-pipe
    run_command("install -m u=rw,g=r,o=r /opt/lumeo/wgm/scripts/lumeo-wgm-pipe.service /etc/systemd/system/", sudo=True)
    run_command("systemctl enable --now lumeo-wgm-pipe", sudo=True)

    # Restart container
    run_command("docker restart lumeo_wgm", sudo=True)

    # Install update cron job
    install_gateway_updater()

    print_text("Lumeo Web Gateway Manager has been installed. Access by visiting https://<device-ip-address>")


def update_wgm():
    """Update Lumeo Web Gateway Manager."""        
    
    # Determine the appropriate container based on architecture
    arch_type = platform.machine()
    wgm_container = "lumeo/wgm-x64:latest" if arch_type == "x86_64" else "lumeo/wgm-arm:latest"

    # Get the Image ID of the currently running container
    running_image_id = run_command("docker inspect --format='{{.Image}}' lumeo_wgm", sudo=True)

    if running_image_id:
        # Pull the latest image
        run_command(f"docker pull {wgm_container}", sudo=True)

        # Get the Image ID of the latest image
        latest_image_id = run_command(f"docker inspect --format='{{{{.Id}}}}' {wgm_container}", sudo=True)

        # Compare the IDs. If they are different, stop, remove and run the new container
        if running_image_id != latest_image_id:
            run_command("docker stop lumeo_wgm && docker rm -f lumeo_wgm", sudo=True)

            # Host network needed for bonjour broadcast
            run_command(f"docker run -d -v /opt/lumeo/wgm/:/lumeo_wgm/ --name lumeo_wgm --restart=always --network host {wgm_container}", sudo=True)
            
            # Remove the old image
            run_command(f"docker image rm -f {running_image_id}", sudo=True)
            print_text("Updated and started new Docker container successfully.")
        else:
            print_text("Running Docker container is up-to-date.")
    else:
        print_text("Lumeo Web Gateway Manager container not found.")


def reset_wgm(silent=False):
    """Reset the password for the Lumeo Web Gateway Manager."""    
    reset = True
    
    if not silent:
        print_header("Lumeo Web Gateway Manager Password Reset")
        print_text(" ")
        print_text("Resetting the web password will require you to create a new device ")
        print_text("account via the web interface. You should do so immediately, since ")
        print_text("once reset, anyone can create a new device account.")
        print_text(" ")    
        answer = input("Would you like to reset the web password for this device (yes/no)? ")
        if answer.lower() == "yes" or answer.lower() == "y":
            reset = True
        else:
            reset = False
    
    if reset:
        run_command("rm -f /opt/lumeo/wgm/db.sqlite", sudo=True)
        run_command("docker restart lumeo_wgm", sudo=True)
        print_text("Device account reset complete")

