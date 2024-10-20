from .linuxmonitor import LinuxMonitor

import argparse
import sys
import logging
import asyncio

def main() -> None:
    parser = argparse.ArgumentParser(description='System Management CLI Tool')

    # Define available arguments
    parser.add_argument('--config_file', type=str, required=True, help='Path to the configuration file (must be a JSON file)')
    parser.add_argument('--start_scheduled_task_check_for_issues', action='store_true', help='Start periodic task to show potential issues periodically (in background, will not stop until you stop the script)')
    parser.add_argument('--start_scheduled_task_show_info', action='store_true', help='Start periodic task to show system information periodically (in background, will not stop until you stop the script)')
    parser.add_argument('--usage', action='store_true', help='📊 View disk space, CPU, RAM, ... 📊')
    parser.add_argument('--os_infos', action='store_true', help='🖥 View basic system information 🖥')
    parser.add_argument('--users', action='store_true', help='👥 View connected users 👥')
    parser.add_argument('--user_logins', action='store_true', help='👥 View last user connections 👥')
    parser.add_argument('--ping', action='store_true', help='🌐 Ping websites 🌐')
    parser.add_argument('--websites', action='store_true', help='🌐 Check websites access (GET requests) 🌐')
    parser.add_argument('--certificates', action='store_true', help='🔒 Check SSL certificates 🔒')
    parser.add_argument('--reboot_server', action='store_true', help='🔄 Restart the entire server 🔄')
    parser.add_argument('--services_status', action='store_true', help='🩺 Check services are running 🩺')
    parser.add_argument('--restart_all', action='store_true', help='🚀 Restart all services 🚀')
    parser.add_argument('--restart_service', type=str, help='🚀 Restart a service 🚀')
    parser.add_argument('--stop_service', type=str, help='🚫 Stop a service 🚫')
    parser.add_argument('--list_services', action='store_true', help='📋 List all available services 📋')
    parser.add_argument('--ports', action='store_true', help='🔒 Check ports 🔒')
    parser.add_argument('--list_processes', action='store_true', help='📋 List active processes 📋')
    parser.add_argument('--kill_process', type=int, help='🚫 Stop a process by PID 🚫')
    parser.add_argument('--list_commands', action='store_true', help='📋 List all available commands 📋')
    parser.add_argument('execute_command', type=str, help='📋 Execute a command 📋')
    parser.add_argument('execute_all_commands', type=str, help='📋 Execute all commands 📋')

    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--nodebug', action='store_true', help='Disable all logs')

    # Parse arguments
    args = parser.parse_args()

    # Enable or disable debug mode
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    elif args.nodebug:
        logging.getLogger().setLevel(logging.CRITICAL)
    else:
        # Default to warning
        logging.getLogger().setLevel(logging.WARNING)

    # Ensure the config file is provided
    if not args.config_file:
        print("Error: --config_file is required")
        parser.print_help()
        sys.exit(1)

    allow_scheduled_tasks_check_for_issues: bool = args.start_scheduled_task_check_for_issues is not None
    allow_scheduled_task_show_info: bool = args.start_scheduled_task_show_info is not None
    monitoring = LinuxMonitor(config_file=args.config_file, allow_scheduled_tasks_check_for_issues=allow_scheduled_tasks_check_for_issues, allow_scheduled_task_show_info=allow_scheduled_task_show_info)

    # Handle all commands
    handled: bool = False

    if args.usage:
        handled = True
        print("Viewing disk space, CPU, RAM, ...")
        out_msg: str = monitoring.check_all_disk_usage(is_private=True, display_only_if_critical=False)
        msg: str = monitoring.check_all_folder_usage(is_private=True, display_only_if_critical=False)
        if msg != "":
            if out_msg != "":
                out_msg += "\n"
            out_msg += msg

        out_msg += "\n"
        out_msg += monitoring.check_cpu_usage(display_only_if_critical=False) + "\n"
        out_msg += monitoring.check_ram_usage(display_only_if_critical=False) + "\n"
        out_msg += monitoring.check_swap_usage(display_only_if_critical=False) + "\n"
        out_msg += monitoring.check_cpu_temperature(display_only_if_critical=False) + "\n"
        out_msg += monitoring.get_network_info()
        print(out_msg)

    if args.os_infos:
        handled = True
        print("Viewing basic system information...")
        out_msg: str = monitoring.get_hostname() + "\n"
        out_msg += monitoring.get_os_details() + "\n"
        out_msg += monitoring.get_kernel_version() + "\n"
        out_msg += monitoring.check_uptime(display_only_if_critical=False) + "\n"
        out_msg += monitoring.get_server_datetime()
        print(out_msg)

    if args.users:
        handled = True
        print("Viewing connected users...")
        out_msg: str = monitoring.get_connected_users()
        print(out_msg)

    if args.user_logins:
        handled = True
        print("Viewing last user connections...")
        out_msg: str = monitoring.check_all_recent_user_logins(display_only_if_critical=False)
        print(out_msg)

    if args.ping:
        handled = True
        print("Pinging websites...")
        out_msg: str = asyncio.run(monitoring.ping_all_websites(is_private=True, display_only_if_critical=False))
        print(out_msg)

    if args.websites:
        handled = True
        print("Checking websites availability...")
        out_msg: str = asyncio.run(monitoring.check_all_websites(is_private=True, display_only_if_critical=False))
        print(out_msg)

    if args.certificates:
        handled = True
        print("Checking SSL certificates...")
        out_msg: str = monitoring.check_all_certificates(is_private=True, display_only_if_critical=False)
        print(out_msg)

    if args.reboot_server:
        handled = True
        print("Restarting the entire server...")
        out_msg: str = asyncio.run(monitoring.reboot_server())
        print(out_msg)

    if args.services_status:
        handled = True
        print("Checking if services are running and restart if down...")
        out_msg: str = asyncio.run(monitoring.check_all_services_status(is_private=True, display_only_if_critical=False))
        print(out_msg)

    if args.restart_all:
        handled = True
        print("Restarting all services...")
        out_msg: str = asyncio.run(monitoring.restart_all_services(is_private=True))

    if args.restart_service is not None:
        handled = True
        print(f"Restarting service: {args.restart_service}...")
        out_msg: str = asyncio.run(monitoring.restart_service(is_private=True, service_name=args.restart_service, force_restart=True))
        print(out_msg)

    if args.stop_service is not None:
        handled = True
        print(f"Stopping service: {args.stop_service}...")
        out_msg: str = asyncio.run(monitoring.stop_service(is_private=True, service_name=args.stop_service))
        print(out_msg)

    if args.list_services:
        handled = True
        print("Listing all available services...")
        out_msg: str = monitoring.get_all_services(is_private=True)
        print(out_msg)

    if args.list_commands:
        handled = True
        print("Listing all available commands...")
        out_msg: str = asyncio.run(monitoring.list_commands(is_private=True))
        print(out_msg)

    if args.execute_command is not None:
        handled = True
        print(f"Executing command: {args.execute_command}...")
        out_msg: str = asyncio.run(monitoring.execute_command(is_private=True, command_name=args.execute_command))
        print(out_msg)

    if args.execute_all_commands is not None:
        handled = True
        print(f"Executing all commands...")
        out_msg: str = asyncio.run(monitoring.execute_all_commands(is_private=True))
        print(out_msg)

    if args.ports:
        handled = True
        print("Checking ports...")
        out_msg: str = asyncio.run(monitoring.check_all_ports(is_private=True, display_only_if_critical=False))
        print(out_msg)

    if args.list_processes:
        handled = True
        print("Listing active processes (ordered by RAM usage)...")
        out_msg: str = asyncio.run(monitoring.get_ordered_processes(get_non_consuming_processes=False, order_by_ram=True))
        print(out_msg)

    if args.list_processes_order_by_cpu:
        handled = True
        print("Listing active processes (ordered by CPU usage)...")
        out_msg: str = asyncio.run(monitoring.get_ordered_processes(get_non_consuming_processes=False, order_by_ram=False))
        print(out_msg)

    if args.kill_process is not None:
        handled = True
        print(f"Stopping process with PID: {args.kill_process}...")
        out_msg: str = asyncio.run(monitoring.kill_process(pid=args.kill_process))
        print(out_msg)

    if args.start_scheduled_task_check_for_issues:
        handled = True
        print("Starting periodic task (will show something only in case of error (or if debug enabled))...")
        async def async_print(msg: str) -> None:
            print(msg)
        asyncio.run(monitoring.schedule_task(handle_error_message=async_print, is_private=True))

    if args.start_scheduled_task_show_info:
        handled = True
        print("Starting periodic task (will show system information periodically)...")
        async def async_print(msg: str) -> None:
            print(msg)
        asyncio.run(monitoring.schedule_task_show_info(show_message=async_print, is_private=True))

    # Show help if no command was provided or the command was not recognized
    if not handled:
        parser.print_help()

if __name__ == "__main__":
    main()
