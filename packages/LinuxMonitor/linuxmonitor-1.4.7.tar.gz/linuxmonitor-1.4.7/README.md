# Linux Monitor (Python library)
[![PyPI version](https://badge.fury.io/py/LinuxMonitor.svg)](https://pypi.org/project/LinuxMonitor/) [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/QuentinCG/Linux-Monitor-Python-Library/blob/master/LICENSE.md) [![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/QuentinCG) [![Downloads](https://static.pepy.tech/badge/LinuxMonitor)](https://pepy.tech/project/LinuxMonitor) [![Downloads](https://static.pepy.tech/badge/LinuxMonitor/month)](https://pepy.tech/project/LinuxMonitor)

## What is it

This python library is designed to be integrated in python or shell projects to monitor Linux servers.
It is compatible with python 3+ and usable only on Linux.

It is also designed to be easily integrated in discussion channel bots python scripts (example: [Discord Bot Linux Monitor](https://github.com/QuentinCG/Discord-Bot-Linux-Monitor-Python-Library))

<img src="https://github.com/QuentinCG/Linux-Monitor-Python-Library/raw/master/welcome.png" width="300">

## Functionalities

Most important functionalities:
  - Do all checks bellow in a scheduled tasks and display the results only if there is an issue (only in console if using only the library)
  - Do all checks bellow in a scheduled tasks and display the results every time (only in console if using only the library)

List of 'check' functionalities:
  - Check CPU, RAM, SWAP, Temperature
  - Check disk usage
  - Check folder usage
  - Check websites basic availability (ping)
  - Check websites access with optional authentication (GET request)
  - Check services status and restart them if needed
  - Check certificates expiration and validity
  - Check last user connections IPs
  - Check uptime (to inform if the server has been rebooted)
  - Check custom commands

Additionnal functionalities:
  - Get hostname, OS details, kernel version, server datetime, uptime
  - Get connected users
  - Get processes list (PID and name)
  - Kill a process by PID
  - Reboot server
  - Restart/stop a service
  - Execute custom commands

## How to install (python script and shell)

  - Install package calling `pip install linux-monitor` (or `python setup.py install` from the root of this repository)
  - Copy and edit [config-example.json file](https://github.com/QuentinCG/Linux-Monitor-Python-Library/blob/master/config-example.json) depending on your need (on first launch, remove all `restart_command` from config file to prevent potential looping service restart issues on your server in case your config file is not well configured)
  - Add rights to user launching the library depending on what you want it to do
```sh
# Only if this library should be able to reboot the server on demand:
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /sbin/reboot" >> /etc/sudoers.d/USERNAME_HERE
# Only if this library should be able to kill a process on demand:
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /bin/kill" >> /etc/sudoers.d/USERNAME_HERE

# To check last user connection
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /usr/bin/last" >> /etc/sudoers.d/USERNAME_HERE

# Add also all processes added in your config JSON file you want the library to be able to execute
# Example for the existing config-example.json file:
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /bin/systemctl" >> /etc/sudoers.d/USERNAME_HERE
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /etc/init.d/apache2" >> /etc/sudoers.d/USERNAME_HERE
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /etc/init.d/mariadb" >> /etc/sudoers.d/USERNAME_HERE
```
  - Check monitor possibilities (you can find it out by calling `python -m linuxmonitor --help` from the root of this repository)
  - Load your shell or python script

## How to use in shell

```sh
# Get help
python3 -m linuxmonitor --help
# Use "--debug" to show more information during command
# Use "--nodebug" to not show any warning information during command



# Start periodic task to show potential issues periodically (will run indefinitely)
# Best is to call this as a service and put the result in a log file or do something of the stdout
python3 -m linuxmonitor --start_scheduled_task_check_for_issues --config_file config-example.json --nodebug

# Start periodic task to show system information periodically (will run indefinitely)
# Best is to call this as a service and put the result in a log file or do something of the stdout
python3 -m linuxmonitor --start_scheduled_task_show_info --config_file config-example.json --nodebug



# View disk space, CPU, RAM, ...
python3 -m linuxmonitor --usage --config_file config-example.json --nodebug

# View basic system information
python3 -m linuxmonitor --os_infos --config_file config-example.json --nodebug

# View connected users
python3 -m linuxmonitor --users --config_file config-example.json --nodebug

# View last user connections
python3 -m linuxmonitor --user_logins --config_file config-example.json --nodebug

# Check websites (ping)
python3 -m linuxmonitor --ping --config_file config-example.json --nodebug

# Check websites access with optional authentication (GET request)
python3 -m linuxmonitor --websites --config_file config-example.json --nodebug

# Check SSL certificates
python3 -m linuxmonitor --certificates --config_file config-example.json --nodebug

# Check if services are running and restart if down
python3 -m linuxmonitor --services_status --config_file config-example.json --nodebug

# List all available services
python3 -m linuxmonitor --list_services --config_file config-example.json --nodebug

# Restart all services
python3 -m linuxmonitor --restart_all --config_file config-example.json --nodebug

# Restart a service
python3 -m linuxmonitor --restart_service SERVICE_NAME_HERE --config_file config-example.json --nodebug

# Stop a service
python3 -m linuxmonitor --stop_service SERVICE_NAME_HERE --config_file config-example.json --nodebug

# Check ports
python3 -m linuxmonitor --ports --config_file config-example.json --nodebug

# List active processes
python3 -m linuxmonitor --list_processes --config_file config-example.json --nodebug

# Stop a process by PID
python3 -m linuxmonitor --kill_process PID_HERE --config_file config-example.json --nodebug

# Restart the entire server
python3 -m linuxmonitor --reboot_server --config_file config-example.json --nodebug

# List all custom commands
python3 -m linuxmonitor --list_commands --config_file config-example.json --nodebug

# Execute a custom commands
python3 -m linuxmonitor --execute_command CUSTOM_COMMAND_HERE --config_file config-example.json --nodebug

# Execute all custom commands
python3 -m linuxmonitor --execute_all_commands --config_file config-example.json --nodebug
```

## How to use in python script

Example of python script using this library:
 - [Discord Bot Linux Monitor](https://github.com/QuentinCG/Discord-Bot-Linux-Monitor-Python-Library)

## License

This project is under MIT license. This means you can use it as you want (just don't delete the library header).

## Contribute

If you want to add more examples or improve the library, just create a pull request with proper commit message and right wrapping.
