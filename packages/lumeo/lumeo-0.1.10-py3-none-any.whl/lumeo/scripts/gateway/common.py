from .host_utils import check_disk_space, check_os, prompt_disable_x_server
from .nvidia import check_nvidia_dgpu_driver, check_disable_nvidia_driver_updates, enable_jetson_clocks, setup_jetson_gpio, install_jetson_extras, get_jetson_model_name
from .docker import install_docker_and_nvidia_toolkit, set_docker_logs_configuration, fix_nvidia_nvml_init_issue, check_set_docker_data_dir, start_watchtower, migrate_watchtower


def install_common_dependencies():
    
    check_os()
    
    check_disk_space()
    
    # Setup Nvidia DGPU drivers
    check_nvidia_dgpu_driver()
    check_disable_nvidia_driver_updates()

    # Setup Jetson specific components
    enable_jetson_clocks()
    jetson_model_name = get_jetson_model_name()
    if jetson_model_name:
        setup_jetson_gpio()    
    install_jetson_extras()

    # Setup Docker and NVIDIA toolkit
    install_docker_and_nvidia_toolkit()       
    check_set_docker_data_dir()
    set_docker_logs_configuration()
    fix_nvidia_nvml_init_issue()
    
    # Disable X server
    prompt_disable_x_server()
    
    # Start watchtower
    start_watchtower()
    
    return

    
def update_common_dependencies():
    
    fix_nvidia_nvml_init_issue()
    
    enable_jetson_clocks()

    set_docker_logs_configuration()
    
    migrate_watchtower()
    
    return
    