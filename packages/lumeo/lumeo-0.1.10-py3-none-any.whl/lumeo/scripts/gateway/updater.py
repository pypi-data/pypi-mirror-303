import os

from .host_utils import run_command
from .display import print_text

def install_gateway_updater():
    # Uninstall lumeo-container-update cron script if installed
    if os.path.exists("/etc/cron.hourly/lumeo-container-update"):
        run_command("rm -f /etc/cron.hourly/lumeo-container-update", sudo=True)
        print_text("Removed old lumeo-container-update cron script")

    # Uninstall lumeo-wgm-update cron script if installed
    if os.path.exists("/etc/cron.hourly/lumeo-wgm-update-cron"):
        run_command("rm -f /etc/cron.hourly/lumeo-wgm-update-cron", sudo=True)
        print_text("Removed old lumeo-wgm-update-cron cron script")

    # Install the new, unified lumeo_gateway_update_cron.sh script
    if not os.path.exists("/etc/cron.hourly/lumeo_update_cron"):    
        script_path = os.path.join(os.path.dirname(__file__), 'lumeo_update_cron.sh')
        run_command(f"install -m u=rwx,g=rx,o=rx {script_path} /etc/cron.hourly/lumeo_update_cron", sudo=True)
