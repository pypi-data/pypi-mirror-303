
"""
Linux Monitor Library: A library to monitor a Linux server and send the results to 'anything' (or to console if using only the library).

Non exhaustive list of features (available by using it in shell or in python script):
    - Do all checks bellow in a scheduled tasks and display the results only if there is an issue (only in console if using only the library)
    - Do all checks bellow in a scheduled tasks and display the results every time (only in console if using only the library)

    - Check CPU, RAM, SWAP, Temperature
    - Check disk usage
    - Check folder usage
    - Check websites basic availability (ping)
    - Check websites access with optional authentication (GET request)
    - Check services status and restart them if needed
    - Check certificates expiration and validity
    - Check last user connections IPs
    - Check uptime (to inform if the server has been rebooted)

    - Restart/stop a service
    - List all services

    - Get hostname, OS details, kernel version, server datetime, uptime
    - Get connected users

    - Get processes list (PID and name)
    - Kill a process by PID

    - Reboot server
"""

__author__ = 'Quentin Comte-Gaz'
__email__ = "quentin@comte-gaz.com"
__license__ = "MIT License"
__copyright__ = "Copyright Quentin Comte-Gaz (2024)"
__python_version__ = "3.+"
__version__ = "1.4.7 (2024/10/07)"
__status__ = "Usable for any Linux project"

import json
import subprocess
import time
import shutil
from typing import Callable, Optional, Dict, Set, List, Tuple, Awaitable, Any
import psutil
import os
import ssl
import socket
from datetime import datetime, timedelta
import platform
import re
import logging
import asyncio
from http.client import responses
import aiohttp

class LinuxMonitor:
    def __init__(self, config_file: str, allow_scheduled_tasks_check_for_issues: bool, allow_scheduled_task_show_info: bool) -> None:
        """
        Linux Monitor class to monitor a Linux server.

        :param config_file: The path to the JSON configuration file.
        :param allow_scheduled_tasks_check_for_issues: Allow scheduled tasks to check for issues (because it is the python script that will start the scheduled tasks).
        :param allow_scheduled_task_show_info: Allow scheduled tasks to show info (because it is the python script that will start the scheduled tasks).

        :raises ValueError: If the configuration file is incorrect.
        """
        logging.debug(msg=f"Loading configuration file {config_file}...")
        with open(file=config_file, mode='r') as file:
            self.config = json.load(file)


        self.allow_scheduled_tasks_check_for_issues: bool = allow_scheduled_tasks_check_for_issues
        self.allow_scheduled_task_show_info: bool = allow_scheduled_task_show_info

        # Check if the configuration is correct
        self._init_and_check_configuration()

    def _init_and_check_configuration(self) -> None:
        """
        Check if the JSON configuration file is correct.
        """
        # Check if the configuration is a dictionary
        if not isinstance(self.config, dict):
            raise ValueError("The configuration must be a dictionary")

        # Check if the configuration contains the necessary keys
        if 'basic_config' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'basic_config' key")
        if 'scheduled_tasks_check_for_issues' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'scheduled_tasks_check_for_issues' key")
        if 'disks' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'disks' key")
        if 'folders' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'folders' key")
        if 'pings' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'pings' key")
        if 'services' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'services' key")
        if 'certificates' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'certificates' key")
        if 'websites' not in self.config: # type: ignore
            raise ValueError("The configuration must contain the 'websites' key")

        # Get the basic configuration (check if it is a dictionary)
        basic_config: Dict[str, Any] = self.config.get('basic_config', {}) # type: ignore
        if not isinstance(basic_config, dict):
            raise ValueError("The basic configuration must be a dictionary")

        if 'warning_cpu_percent' not in basic_config:
            raise ValueError("The basic configuration must contain the 'warning_cpu_percent' key")
        self.warning_cpu_percent: float = basic_config.get('warning_cpu_percent') # type: ignore

        if 'critical_cpu_percent' not in basic_config:
            raise ValueError("The basic configuration must contain the 'critical_cpu_percent' key")
        self.critical_cpu_percent: float = basic_config.get('critical_cpu_percent') # type: ignore

        if 'warning_ram_percent' not in basic_config:
            raise ValueError("The basic configuration must contain the 'warning_ram_percent' key")
        self.warning_ram_percent: float = basic_config.get('warning_ram_percent') # type: ignore

        if 'critical_ram_percent' not in basic_config:
            raise ValueError("The basic configuration must contain the 'critical_ram_percent' key")
        self.critical_ram_percent: float = basic_config.get('critical_ram_percent') # type: ignore

        if 'warning_swap_percent' not in basic_config:
            raise ValueError("The basic configuration must contain the 'warning_swap_percent' key")
        self.warning_swap_percent: float = basic_config.get('warning_swap_percent') # type: ignore

        if 'critical_swap_percent' not in basic_config:
            raise ValueError("The basic configuration must contain the 'critical_swap_percent' key")
        self.critical_swap_percent: float = basic_config.get('critical_swap_percent') # type: ignore

        if 'warning_temperature_celsius' not in basic_config:
            raise ValueError("The basic configuration must contain the 'warning_temperature_celsius' key")
        self.warning_temperature_celsius: float = basic_config.get('warning_temperature_celsius') # type: ignore

        if 'critical_temperature_celsius' not in basic_config:
            raise ValueError("The basic configuration must contain the 'critical_temperature_celsius' key")
        self.critical_temperature_celsius: float = basic_config.get('critical_temperature_celsius') # type: ignore

        if 'critical_uptime_seconds' not in basic_config:
            raise ValueError("The basic configuration must contain the 'critical_uptime_seconds' key")
        self.critical_uptime_seconds: int = basic_config.get('critical_uptime_seconds') # type: ignore

        if 'warning_uptime_seconds' not in basic_config:
            raise ValueError("The basic configuration must contain the 'warning_uptime_seconds' key")
        self.warning_uptime_seconds: int = basic_config.get('warning_uptime_seconds') # type: ignore

        self.excluded_interfaces: List[str] = basic_config.get('excluded_interfaces', []) # type: ignore

        # Get the scheduled tasks for issues configuration
        if self.allow_scheduled_tasks_check_for_issues:
            schedule_check_for_issues_config: Dict[str, Any] = self.config.get('scheduled_tasks_check_for_issues', {}) # type: ignore
            if not isinstance(schedule_check_for_issues_config, dict):
                raise ValueError("The scheduled tasks checking for issues configuration (schedule_check_for_issues_config) must be a dictionary")

            if 'max_duration_seconds_showing_same_error' not in schedule_check_for_issues_config:
                raise ValueError("The scheduled tasks configuration must contain the 'max_duration_seconds_showing_same_error' key")
            self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks: int = schedule_check_for_issues_config.get('max_duration_seconds_showing_same_error') # type: ignore

            if 'start_immediately' not in schedule_check_for_issues_config:
                raise ValueError("The scheduled tasks configuration must contain the 'start_immediately' key")
            self.start_scheduled_tasks_immediately: bool = schedule_check_for_issues_config.get('start_immediately') # type: ignore

            if 'duration_in_sec_wait_between_each_execution' not in schedule_check_for_issues_config:
                raise ValueError("The scheduled tasks configuration must contain the 'duration_in_sec_wait_between_each_execution' key")
            self.duration_in_sec_wait_between_each_schedule_task_execution: int = schedule_check_for_issues_config.get('duration_in_sec_wait_between_each_execution') # type: ignore

        # Get the scheduled tasks show info configuration
        if self.allow_scheduled_task_show_info:
            schedule_show_info_config: Dict[str, Any] = self.config.get('scheduled_tasks_show_infos', {}) # type: ignore
            if not isinstance(schedule_show_info_config, dict):
                raise ValueError("The scheduled show info tasks configuration (scheduled_tasks_show_infos) must be a dictionary")

            if 'start_immediately' not in schedule_show_info_config:
                raise ValueError("The scheduled tasks configuration must contain the 'start_immediately' key")
            self.start_scheduled_task_show_info_immediately: bool = schedule_show_info_config.get('start_immediately') # type: ignore

            if 'duration_in_sec_wait_between_each_execution' not in schedule_show_info_config:
                raise ValueError("The scheduled tasks configuration must contain the 'duration_in_sec_wait_between_each_execution' key")
            self.duration_in_sec_wait_between_each_schedule_task_show_info_execution: int = schedule_show_info_config.get('duration_in_sec_wait_between_each_execution') # type: ignore

        logging.debug(msg="Configuration loaded successfully")

    #region Execute Command

    def _json_to_md(self, json_string: str, level: int = 0) -> str:
        """
        Convert a JSON string into a Markdown representation.

        Parameters:
            json_string (str): The input JSON string.
            level (int): The current indentation level (default is 0).

        Returns:
            str: The resulting Markdown formatted string.
        """
        md: str = ""
        indent: str = "  " * level  # type: ignore # Indentation for markdown headings

        # Preprocess the input to convert single quotes to double quotes
        json_string = re.sub(r"'", '"', json_string)

        # Parse the JSON string to a Python object
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError as e:
            return f"Error parsing JSON: {str(e)}"

        # Helper function to convert the parsed JSON to markdown
        def process_data(data, level: int) -> None: # type: ignore
            nonlocal md  # Declare md as nonlocal so it can be modified
            indent = "  " * level

            if isinstance(data, dict):
                for key, value in data.items(): # type: ignore
                    md += f"{indent}- {key}\n"
                    process_data(value, level + 1) # type: ignore
            elif isinstance(data, list):
                if not data:  # Show "nothing" for empty lists
                    md += f"{indent}- Nothing\n"
                else:
                    for item in data: # type: ignore
                        process_data(item, level)  # Skip "Item" label # type: ignore
            else:
                md += f"{indent}- {data}\n"

        process_data(data, level)

        return md

    async def execute_and_verify(self, command: str, display_name: str, show_only_std_and_exception: bool, timeout_in_sec: Optional[int] = None, display_only_if_critical: bool = False, check_also_stdout_not_containing: Optional[str] = None, is_stdout_json: bool=False) -> Tuple[Optional[bool], str]:
        """
        Execute a shell command asynchronously and verify its correct execution.

        :param command: A list of strings representing the command and its arguments.
        :param display_name: The name of the command to display in the output message.
        :param timeout_in_sec: Timeout in seconds for the command execution. None means no timeout.
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.
        :param check_also_stdout_not_containing: If not None, we check that the stdout does not contain this string, if found, we consider it as an execution error.

        :return: A tuple containing a boolean indicating if the command was executed successfully and a string containing the result message.
        """
        returncode: Optional[int] = None

        try:
            logging.debug(msg=f"Executing command {display_name} (command: {command})...")
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                shell=True
            )

            try:
                stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout_in_sec)
                returncode = process.returncode
            except asyncio.TimeoutError:
                logging.warning(msg=f"Timeout expired for {display_name} (command: {command})")
                process.kill()
                return None, f"  - ⚠️ **Error {display_name}**:\n    - Failed to execute the command in less than {timeout_in_sec} seconds)"
        except Exception as e:
            # Failed to execute the command
            if not show_only_std_and_exception:
                out_msg = f"  - ⚠️ **Error {display_name}**:\n```sh\n{e}\n```"
            else:
                out_msg = f"```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return None, out_msg

        # Decode and replace backticks with double quotes
        stdout_str: str = stdout.decode(encoding='utf-8').replace('`', '"').strip()
        stderr_str: str = stderr.decode(encoding='utf-8').replace('`', '"').strip()

        # Check if the command executed successfully
        res: Optional[bool] = (returncode == 0) if (returncode != None) else None
        if res and check_also_stdout_not_containing:
            res = check_also_stdout_not_containing not in stdout_str

        out_msg: str = ""
        if res == False:
            # Command returned an error code
            if not show_only_std_and_exception:
                out_msg = f"  - ❌ **Error {display_name}**\n"
            out_msg += f"  - Error code: `{returncode}`"

            if stderr_str != "":
                out_msg += f"\n  - Error log:\n```sh\n{stderr_str}\n```"

            if stdout_str != "":
                msg_stout: str = stdout_str
                if is_stdout_json:
                    msg_stout = self._json_to_md(stdout_str)
                out_msg += f"\n  - Info:\n```sh\n{msg_stout}\n```"
        elif res == None:
            # Command timed out
            if not show_only_std_and_exception:
                out_msg = f"  - ⚠️ **Error {display_name}**\n"
            out_msg += f"  - Failed to wait for the command to finish (due to timeout of {timeout_in_sec} seconds)"
        else:
            # Command executed successfully
            if not display_only_if_critical:
                if not show_only_std_and_exception:
                    out_msg = f"  - ✅ **{display_name} executed successfully**"
                else:
                    if stdout_str != "":
                        msg_stout: str = stdout_str
                        if is_stdout_json:
                            msg_stout = self._json_to_md(stdout_str)
                        if msg_stout != "":
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += f"```sh\n{msg_stout}\n```"

        if res == True:
            logging.info(msg=f"Command {display_name} (command {command}) executed successfully")
        else:
            logging.error(msg=f"Error executing command {display_name} (command {command}):\n{out_msg}")

        return res, out_msg

    #endregion

    #region Reboot

    async def reboot_server(self) -> str:
        """
        Reboot the server.

        :return: A string containing the output message.

        IMPORTANT: To be usable, the user must have the right to execute `sudo /sbin/reboot` command without password.
        """
        logging.info(msg="Rebooting the server...")
        _, out_msg = await self.execute_and_verify(command="sudo /sbin/reboot", display_name="Server reboot", show_only_std_and_exception=False, timeout_in_sec=None, display_only_if_critical=False)

        if out_msg != "":
            out_msg = f"# 🔄 Reboot 🔄\n{out_msg}"

        return out_msg

    #endregion

    #region Disk Usage

    def _check_disk_usage_per_disk(self, disk_path: str, display_name: str, warning_disk_percent: float, critical_disk_percent: float, display_only_if_critical: bool=False) -> str:
        """
        Check the disk usage for a specific disk.

        :param disk_path: The path to the disk.
        :param display_name: The name of the disk to display in the output message.
        :param warning_disk_percent: The warning disk usage percentage.
        :param critical_disk_percent: The critical disk usage percentage.
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            total, used, free = shutil.disk_usage(path=disk_path)
            total_gb: float = total / (2**30)
            used_gb: float = used / (2**30)
            free_gb: float = free / (2**30)

            percent_used: float = (used / total) * 100
            if critical_disk_percent != -1 and percent_used > critical_disk_percent:
                out_msg = f"- 🚨 Critical disk {display_name} (`{disk_path}`) space:\n" \
                        f"  - Total: {total_gb:.2f}GB\n" \
                        f"  - Used: {used_gb:.2f}GB ({percent_used:.2f}%)\n" \
                        f"  - Free: {free_gb:.2f}GB\n" \
                        f"⚠️ **Free up disk space** ⚠️"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if warning_disk_percent != -1 and percent_used > warning_disk_percent:
                    icon: str = "⚠️ "
                elif critical_disk_percent == -1 and warning_disk_percent == -1:
                    icon = ""
                else:
                    icon = "✅ "
                out_msg = f"{icon} {display_name} (`{disk_path}`): {free_gb:.2f}GB free, {used_gb:.2f}GB used (**{percent_used:.2f}%** used on a total of {total_gb:.2f}GB)"
                logging.info(msg=out_msg)
        except Exception as e:
            out_msg = f"⚠️ **Error getting disk {display_name} (`{disk_path}`) space**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    def check_all_disk_usage(self, is_private: bool, display_only_if_critical: bool=False) -> str:
        """
        Check the disk usage for all disks configured in the JSON configuration file.

        :param is_private: User permission to check private or public disks (True for private, False for public).
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        try:
            out_msg: str = ""
            for disk_config in self.config['disks']:
                if is_private or is_private == disk_config['is_private']:
                    device = disk_config['device']
                    display_name = disk_config.get('display_name', device)
                    # Verify that warning_percent & critical_percent exist, otherwise use -1
                    warning_percent = disk_config.get('warning_percent', -1)
                    critical_percent = disk_config.get('critical_percent', -1)

                    # We only check what is needed
                    if not display_only_if_critical or (display_only_if_critical and critical_percent != -1):
                        result: str = self._check_disk_usage_per_disk(disk_path=device, display_name=display_name, warning_disk_percent=warning_percent, critical_disk_percent=critical_percent, display_only_if_critical=display_only_if_critical)
                        if result and result != "":
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += f"- {result}"

            if out_msg != "":
                out_msg = f"# 🖥️ Disk space 🖥️\n{out_msg}"

            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error retrieving disk space**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    #endregion

    #region Folder Usage

    def _get_folder_size_in_bytes(self, start_path: str = '.') -> float:
        """
        Get the size of a folder in bytes.

        :param start_path: The path to the folder.

        :return: The size of the folder in bytes.
        """
        try:
            total_size = 0
            for dirpath, _, filenames in os.walk(start_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)

                    # Skip if it is symbolic link
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
            logging.info(msg=f"Total size of folder {start_path}: {total_size} bytes")
            return total_size
        except Exception as e:
            logging.exception(msg=f"Error getting folder size in bytes for {start_path}:\n{e}")
            return -1

    def _check_folder_usage(self, folder_path: str, display_name: str, warning_usage_giga: float, critical_usage_giga: float, total_disk_giga: float, display_only_if_critical: bool=False) -> str:
        """
        Check the folder usage for a specific folder.

        :param folder_path: The path to the folder.
        :param display_name: The name of the folder to display in the output message.
        :param warning_usage_giga: The warning folder usage in gigabytes.
        :param critical_usage_giga: The critical folder usage in gigabytes.
        :param total_disk_giga: The total disk space in gigabytes.
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            total_used_bytes = self._get_folder_size_in_bytes(start_path=folder_path)
            total_used_giga = total_used_bytes / (2**30)

            percent_used: float = 0
            if critical_usage_giga > 0:
                percent_used = (total_used_bytes / (critical_usage_giga * (2**30)) ) * 100

            if critical_usage_giga > 0 and total_used_bytes >= critical_usage_giga * (2**30):
                out_msg = f"- 🚨 Critical folder {display_name} space (`{folder_path}`):\n" \
                        f"  - Total allowed: {critical_usage_giga:.2f}GB\n" \
                        f"  - Used: {total_used_giga:.2f}GB ({percent_used:.2f}%)\n" \
                        f"⚠️ **Please free up space in this folder** ⚠️"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if warning_usage_giga > 0 and total_used_bytes >= warning_usage_giga * (2**30):
                    icon: str = "⚠️ "
                elif critical_usage_giga == -1 and warning_usage_giga == -1:
                    icon = ""
                else:
                    icon = "✅ "

                if critical_usage_giga > 0:
                    out_msg = f"{icon}{display_name}: {total_used_giga:.2f}GB used (**{((total_used_bytes / (total_disk_giga * (2**30))) * 100):.2f}%** of total disk space, {percent_used:.2f}% used of a total allowed of {critical_usage_giga:.2f}GB)"
                else:
                    out_msg = f"{icon}{display_name}: {total_used_giga:.2f}GB used (**{((total_used_bytes / (total_disk_giga * (2**30))) * 100):.2f}%** of total disk space)"

                logging.info(msg=out_msg)
        except Exception as e:
            out_msg = f"⚠️ **Error getting folder {display_name} space**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    def check_all_folder_usage(self, is_private: bool, display_only_if_critical: bool=False) -> str:
        """
        Check the folder usage for all folders configured in the JSON configuration file.

        :param is_private: User permission to check private or public folders (True for private, False for public).
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        try:
            # Get total disk space of the system to display a usage percentage
            try:
                total_disk, _, _ = shutil.disk_usage(path="/")
                total_disk_giga: float = total_disk / (2**30)
            except Exception as e:
                total_disk_giga = 0
                logging.exception(msg=f"Error getting total disk space:\n{e}")

            out_msg: str = ""
            for folder_config in self.config['folders']:
                if is_private or is_private == folder_config['is_private']:
                    folder_path = folder_config['folder_path']
                    display_name = folder_config.get('display_name', folder_path)
                    # Verify that warning_usage_giga & critical_usage_giga exist, otherwise use -1
                    warning_usage_giga = folder_config.get('warning_usage_giga', -1)
                    critical_usage_giga = folder_config.get('critical_usage_giga', -1)

                    # We only check what is needed
                    if not display_only_if_critical or (display_only_if_critical and critical_usage_giga != -1):
                        result: str = self._check_folder_usage(folder_path=folder_path, display_name=display_name, warning_usage_giga=warning_usage_giga, critical_usage_giga=critical_usage_giga, total_disk_giga=total_disk_giga, display_only_if_critical=display_only_if_critical)
                        if result and result != "":
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += f"- {result}"

            if out_msg != "":
                out_msg = f"# 📂 Folder space 📂\n{out_msg}"

            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error getting folder space**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    #endregion

    #region CPU & RAM & Swap & Temperature & Uptime

    def _get_cpu_name(self) -> str:
        """
        Get the CPU name.

        :return: The CPU name.
        """
        cpu_name: str = ""
        try:
            cpu_name = platform.processor()
            if not cpu_name or cpu_name == "":
                with open(file="/proc/cpuinfo", mode="r") as file:
                    cpu_info_lines: List[str] = file.readlines()
                    for line in cpu_info_lines:
                        if "model name" in line:
                            cpu_name = re.sub(pattern=r"model name\s+:\s+", repl="", string=line)
                            # remove extra spaces
                            cpu_name = re.sub(pattern=r"\s+", repl=" ", string=cpu_name).strip()
                            break

            logging.info(msg=f"CPU name: {cpu_name}")
            return cpu_name
        except Exception as e:
            logging.exception(msg=f"Error getting CPU name:\n{e}")
            return ""

    def check_cpu_usage(self, display_only_if_critical: bool=False) -> str:
        """
        Check the CPU usage.

        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            # Getting average CPU usage for the last second
            cpu_percent: float = psutil.cpu_percent(percpu=False)

            # Getting number of cores and Ghz
            cpu_info: float = psutil.cpu_freq().max / 1000
            cpu_cores: int = psutil.cpu_count(logical=False)
            cpu_name: str = self._get_cpu_name()

            if cpu_percent > self.critical_cpu_percent:
                out_msg = f"- 🚨 **Critical CPU usage**:\n- **{cpu_percent:.2f}%** used on {cpu_cores} core of {cpu_info:.2f}GHz ({cpu_name})\n⚠️ **Check what is using so much CPU power** ⚠️"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if cpu_percent > self.warning_cpu_percent:
                    icon = "⚠️"
                else:
                    icon = "✅"
                out_msg = f"- {icon} **{cpu_percent:.2f}%** used on {cpu_cores} core of {cpu_info:.2f}GHz ({cpu_name})"
                logging.info(msg=out_msg)
        except Exception as e:
            out_msg = f"- ⚠️ **Error getting CPU usage**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        if out_msg != "":
            out_msg = f"# 📈 CPU 📈\n{out_msg}"

        return out_msg

    def check_ram_usage(self, display_only_if_critical: bool=False) -> str:
        """
        Check the RAM usage.

        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            # Getting RAM usage
            ram = psutil.virtual_memory()
            total_ram: float = ram.total / (2**30)
            used_ram: float = ram.used / (2**30)
            free_ram: float = total_ram - used_ram
            percent_ram: float = ram.percent
            if percent_ram > self.critical_ram_percent:
                out_msg = f"- 🚨 **Critical RAM usage**:\n- Total: {total_ram:.2f}GB\n- Used: {used_ram:.2f}GB ({percent_ram:.2f}%)\n- Free: {free_ram:.2f}GB\n⚠️ **Check what is using so much RAM** ⚠️"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if percent_ram > self.warning_ram_percent:
                    icon = "⚠️"
                else:
                    icon = "✅"
                out_msg = f"- {icon} **{percent_ram:.2f}%** used on a total of {total_ram:.2f}GB ({free_ram:.2f}GB free, {used_ram:.2f}GB used)"
                logging.info(msg=out_msg)
        except Exception as e:
            out_msg = f"⚠️ **Error getting RAM usage**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        if out_msg != "":
            out_msg = f"# 📊 RAM 📊\n{out_msg}"

        return out_msg

    def check_swap_usage(self, display_only_if_critical: bool=False) -> str:
        """
        Check the SWAP usage.

        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            # Getting Swap usage
            swap = psutil.swap_memory()
            total_swap: float = swap.total / (2**30)
            used_swap: float = swap.used / (2**30)
            free_swap: float = swap.free / (2**30)
            percent_swap: float = swap.percent
            if percent_swap > self.critical_swap_percent:
                out_msg = f"- 🚨 **Critical SWAP usage**\n- Total: {total_swap:.2f}GB\n- Used: {used_swap:.2f}GB ({percent_swap:.2f}%)\n- Free: {free_swap:.2f}GB\n⚠️ **Check what is using so much SWAP** ⚠️"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if percent_swap > self.warning_swap_percent:
                    icon = "⚠️"
                else:
                    icon = "✅"
                out_msg = f"- {icon} **{percent_swap:.2f}%** used on a total of {total_swap:.2f}GB ({free_swap:.2f}GB free, {used_swap:.2f}GB used)"
                logging.info(msg=out_msg)
        except Exception as e:
            out_msg = f"- ⚠️ **Error getting SWAP usage**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        if out_msg != "":
            out_msg = f"# 🔄 SWAP 🔄\n{out_msg}"

        return out_msg

    def check_cpu_temperature(self, display_only_if_critical: bool=False) -> str:
        """
        Check the CPU temperature.

        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            if not hasattr(psutil, "sensors_temperatures"):
                logging.error(msg="psutil does not support reading CPU temperatures")
                if not display_only_if_critical:
                    return "- ⚠️ **Error reading CPU temperature**: `psutil` does not support reading CPU temperatures."
                else:
                    return ""

            temps = psutil.sensors_temperatures() # type: ignore
            cpu_temps = temps.get('coretemp', [])  # type: ignore # 'coretemp' est commun sur les systèmes Intel

            if not cpu_temps:
                logging.error(msg="No CPU temperature sensors found")
                if not display_only_if_critical:
                    return "- ⚠️ **Error reading CPU temperature**: No CPU temperature sensor found."
                else:
                    return ""

            # Calculer la température maximale
            max_temp = max(temp.current for temp in cpu_temps) # type: ignore

            # Vérifier la température par rapport au seuil critique
            if max_temp > self.critical_temperature_celsius:
                out_msg = f"- 🚨 **Critical CPU temperature**:\n- {max_temp:.2f}°C\n- Critical threshold: {self.critical_temperature_celsius}°C\n⚠️ **Check the CPU cooling system** ⚠️"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if max_temp > self.warning_temperature_celsius:
                    icon = "⚠️"
                else:
                    icon = "✅"
                out_msg = f"- {icon} **{max_temp:.2f}°C**"
                logging.info(msg=out_msg)
        except Exception as e:
            out_msg = f"- ⚠️ **Error getting CPU temperature**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        if out_msg != "":
            out_msg = f"# 🌡️ Temperature 🌡️\n{out_msg}"

        return out_msg

    def check_uptime(self, display_only_if_critical: bool=False) -> str:
        """
        Check the system uptime.

        :param display_only_if_critical: If True, the string result will only be returned if uptime is less than the critical uptime defined in the configuration.

        :return: A string containing the result message.
        """
        try:
            # Obtenir l'uptime du système en secondes
            uptime_seconds: float = time.time() - psutil.boot_time()
            years, months = divmod(uptime_seconds, 60*60*24*30*12)
            months, days = divmod(months, 60*60*24*30)
            days, hours = divmod(days, 60*60*24)
            hours, minutes = divmod(hours, 60*60)
            minutes, seconds = divmod(minutes, 60)

            # Date de démarrage du système
            boot_time: str = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(psutil.boot_time()))

            dispo: str = ""
            if years >= 1:
                dispo += f"{int(years)} year(s) "
            if months >= 1:
                dispo += f"{int(months)} month(s) "
            if days >= 1:
                dispo += f"{int(days)} day(s) "
            if hours >= 1:
                dispo += f"{int(hours)}h "
            if minutes >= 1:
                dispo += f"{int(minutes)}min "
            if seconds >= 1:
                dispo += f"{int(seconds)}sec "
            dispo += "ago"

            out_msg: str = ""
            if uptime_seconds < self.critical_uptime_seconds:
                out_msg = f"- 🚨 **Server restarted recently**:\n- {dispo} (started on {boot_time})"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if uptime_seconds < self.warning_uptime_seconds:
                    out_msg = f"- ⚠️ **Server restarted recently**: {dispo} (started on {boot_time})"
                    logging.warning(msg=out_msg)
                else:
                    # Funny emoji depending on uptime if everything is fine
                    emoji: str = ""
                    if years >= 2:
                        emoji = "🎂"
                    if years >= 1:
                        emoji = "🎉"
                    elif months >= 6:
                        emoji = "🥳"
                    elif months >= 1:
                        emoji = "😀"
                    elif days >= 1:
                        emoji = "🎊"
                    elif hours >= 1:
                        emoji = "👶"
                    elif minutes >= 20:
                        emoji = "🤔"
                    else:
                        emoji = "☢️"

                    out_msg = f"- {emoji} **{dispo}** (started on {boot_time})"

            if out_msg != "":
                out_msg = f"# 🕒 System availability 🕒\n{out_msg}"
                logging.info(msg=out_msg)
        except Exception as e:
            out_msg = f"- ⚠️ **Error getting system uptime**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    #endregion

    #region Ping Websites

    async def _ping_website(self, website: str, display_name: str, timeout_in_sec: int, display_only_if_critical: bool=False) -> str:
        """
        Ping a website.

        :param website: The website to ping.
        :param display_name: The name of the website to display in the output message.
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        try:
            ping_command: str = f"ping -c 1 {website}"
            display_name = f"[{display_name}](https://{website})"

            start_time: float = time.time()
            res, out_msg = await self.execute_and_verify(command=ping_command, display_name=f"ping {display_name}", show_only_std_and_exception=False, timeout_in_sec=timeout_in_sec, display_only_if_critical=display_only_if_critical)
            end_time: float = time.time()

            if res == True and not display_only_if_critical:
                res_ping_sec: str = "{:.2f}sec".format(end_time - start_time)
                out_msg: str = f"✅ **{display_name} answered in {res_ping_sec}**."
                logging.info(msg=out_msg)

            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error pinging {display_name}**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    async def ping_all_websites(self, is_private: bool, display_only_if_critical: bool=False) -> str:
        """
        Ping all websites configured in the JSON configuration file.

        :param is_private: User permission to check private or public websites (True for private, False for public).
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        for ping_config in self.config['pings']:
            if is_private or is_private == ping_config['is_private']:
                timeout_in_sec: int = ping_config.get('timeout_in_sec', 5)
                result: str = await self._ping_website(website=ping_config['website'], display_name=ping_config['display_name'], timeout_in_sec=timeout_in_sec, display_only_if_critical=display_only_if_critical)
                if result:
                    if out_msg:
                        out_msg += "\n"
                    out_msg += f"- {result}"

        if out_msg != "":
            out_msg = f"# 🌐 Website state 🌐\n{out_msg}"

        return out_msg

    #endregion

    #region Check website response

    async def _check_website(self, url: str, display_name: str, show_content_if_issue: bool, service_name: str = "",
                             timeout_in_sec: int = 5, auth_type: Optional[str] = None, username: Optional[str] = None,
                             password: Optional[str] = None, token: Optional[str] = None, additional_allowed_statuses: List[int] = [],
                             display_only_if_critical: bool=False) -> Tuple[bool, str]:
        try:
            display_name = f"[{display_name}]({url})"

            auth = None
            headers: Dict[str, str] = {}

            # Select the appropriate authentication method
            if auth_type == 'basic' and username and password:
                auth = aiohttp.BasicAuth(username, password)  # Use aiohttp.BasicAuth for basic authentication
            elif auth_type == 'digest' and username and password:
                return False, f"❌ **Digest authentication not supported, cannot check {display_name}**."
            elif auth_type == 'bearer' and token:
                headers = {'Authorization': f'Bearer {token}'}

            # Create an aiohttp client session to make the request
            async with aiohttp.ClientSession() as session:
                start_time: float = time.time()
                async with session.get(url, auth=auth, headers=headers, timeout=timeout_in_sec) as response:
                    end_time: float = time.time()
                    # Default allowed status codes (200-299)
                    allowed_statuses = list(range(200, 300))

                    # Include any additional allowed status codes if provided
                    if additional_allowed_statuses:
                        allowed_statuses += additional_allowed_statuses

                    # Check if the status code is within the allowed list
                    if response.status in allowed_statuses:
                        if not display_only_if_critical:
                            out_msg: str = f"✅ **{display_name} answered with valid status code {response.status}** in {end_time - start_time:.2f}sec."
                            logging.info(msg=out_msg)
                            return True, out_msg
                        else:
                            return True, ""
                    else:
                        # Get the reason phrase (e.g., "Unauthorized" for 401)
                        status_reason: str = responses.get(response.status, "Unknown status")
                        out_msg = f"❌ **{display_name} answered with invalid status code {response.status} - {status_reason}**."
                        if show_content_if_issue:
                            content: str = (await response.text()).replace('`', '"').strip()
                            out_msg += f"\n```sh\n{content}\n```"
                        logging.warning(msg=out_msg)
                        return False, out_msg
        except asyncio.TimeoutError:
            out_msg = f"⚠️ **Error checking {display_name}: Timeout**"
            return False, out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error checking {display_name}**:\n```sh\n{e}\n```"
            return False, out_msg

    async def check_all_websites(self, is_private: bool, display_only_if_critical: bool=False) -> str:
        try:
            out_msg: str = ""
            for website_config in self.config['websites']:
                if is_private or is_private == website_config['is_private']:
                    timeout_in_sec: int = website_config.get('timeout_in_sec', 5)
                    url: str = website_config['url']
                    display_name: str = website_config.get('display_name', url)
                    show_content_if_issue: bool = website_config.get('show_content_if_issue', False)
                    service_name_to_restart: str = website_config.get('service_name_to_restart', "")
                    auth_type: Optional[str] = website_config.get('auth_type', None)
                    username: Optional[str] = website_config.get('username', None)
                    password: Optional[str] = website_config.get('password', None)
                    token: Optional[str] = website_config.get('token', None)
                    additional_allowed_statuses: List[int] = website_config.get('additional_allowed_statuses', [])

                    res, msg = await self._check_website(url=url, display_name=display_name, timeout_in_sec=timeout_in_sec,
                                                       show_content_if_issue=show_content_if_issue,
                                                       auth_type=auth_type, username=username, password=password, token=token,
                                                       additional_allowed_statuses=additional_allowed_statuses,
                                                       display_only_if_critical=display_only_if_critical)
                    if msg != "":
                        if out_msg:
                            out_msg += "\n"
                        out_msg += f"- {msg}"

                    if not res and service_name_to_restart != "":
                        restart_msg = await self.restart_service(is_private=is_private, service_name=service_name_to_restart, force_restart=False)
                        out_msg += f"\n  - {restart_msg}"

            if out_msg != "":
                out_msg = f"# 🌐 Website access state 🌐\n{out_msg}"

            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error checking website access states**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    #endregion

    #region Services

    def get_all_services(self, is_private: bool) -> str:
        """
        Get all services allowed to restart which are configured in the JSON configuration file.

        :param is_private: User permission to check private or public services (True for private, False for public).

        :return: A string containing the result message.
        """
        out_msg: str = ""
        for service_name in self.config['services'].keys():
            service = self.config['services'][service_name]
            if is_private or service['is_private'] == is_private:
                is_allowed_to_restart: bool = 'restart_command' in service
                is_allowed_to_stop: bool = 'stop_command' in service
                auto_restart: bool = service.get('auto_restart', False)

                if out_msg != "":
                    out_msg += "\n"
                out_msg += f"- `{service_name}`: {service['display_name']}:\n"
                if not is_allowed_to_restart:
                    out_msg += "  - ❌ Not authorized to restart (no 'restart_command')\n"
                else:
                    if auto_restart:
                        out_msg += "  - ✅ Can be restarted (automatically & manually)\n"
                    else:
                        out_msg += "  - ✅ Can be restarted (manually only because 'auto_restart' = false)\n"

                if is_allowed_to_stop:
                    out_msg += "  - ✅ Can be stopped manually"
                else:
                    out_msg += "  - ❌ Not authorized to stop manually (no 'stop_command')"

        if out_msg != "":
            out_msg = f"# 🔄 Services list 🔄\n{out_msg}"
        else:
            out_msg = f"❌ **No service found**."

        logging.info(msg=out_msg)
        return out_msg

    async def restart_service(self, is_private: bool, service_name: str, force_restart: bool) -> str:
        """
        Restart a specific service.

        :param is_private: User permission to restart private or public services (True for private, False for public).
        :param service_name: The name of the service name to restart (as configured in the JSON configuration file).

        :return: A string containing the result message.
        """
        try:
            if service_name not in self.config['services'].keys():
                out_msg = f"❌ **Service {service_name} not found**."
                logging.error(msg=out_msg)
                return out_msg

            service = self.config['services'][service_name]
            if not is_private and is_private != service['is_private']:
                out_msg = f"❌ **Service {service_name} not authorized to restart in public**."
                logging.error(msg=out_msg)
                return out_msg

            display_name: str = service.get('display_name', service_name)
            if 'restart_command' not in service:
                out_msg = f"❌ **Restart command not found for {display_name}**."
                logging.error(msg=out_msg)
                return out_msg

            if not force_restart and not service.get('auto_restart', False):
                out_msg = f"⚠️ **Service {display_name} can be restarted only manually** (change configuration if needed)."
                logging.error(msg=out_msg)
                return out_msg

            timeout_in_sec: int = service.get('timeout_in_sec', 90)

            service_call: str = service['restart_command']
            out_msg: str = ""

            logging.info(f"Trying to restart {display_name} (command: {service_call}) in less than {timeout_in_sec}sec...")

            start_time: float = time.time()
            res, res_msg = await self.execute_and_verify(command=service_call, display_name=f"restart {display_name}", show_only_std_and_exception=True, timeout_in_sec=timeout_in_sec, display_only_if_critical=False)
            end_time: float = time.time()

            if res == True:
                readable_duration: str = "{:.2f}".format(end_time - start_time)
                out_msg = f"✅ **{display_name} restarted with success** in {readable_duration}sec."
                logging.info(msg=out_msg)
            else:
                out_msg = f"❌ **Error restarting service {display_name}**"
                if res_msg and res_msg != "":
                    out_msg += f"\n{res_msg}"
                logging.warning(msg=out_msg)

            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error restarting service {service_name}**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    async def restart_all_services(self, is_private: bool) -> str:
        """
        Restart all services allowed to restart which are configured in the JSON configuration file.

        :param is_private: User permission to restart private or public services (True for private, False for public).

        :return: A string containing the result message.
        """
        try:
            out_msg: str = ""
            for service_name in self.config["services"].keys():
                if is_private or self.config["services"][service_name]['is_private'] == is_private:
                    res: str = await self.restart_service(is_private=is_private, service_name=service_name, force_restart=True)
                    if res != "":
                        if out_msg:
                            out_msg += "\n"
                        out_msg += f"- {res}"

            if out_msg:
                out_msg = f"# 📱 Restart services 📱\n{out_msg}"

            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error restarting services**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    async def _get_service_status(self, is_private: bool, service_name: str) -> Tuple[Optional[bool], str]:
        """
        Get the status of a specific service.

        :param is_private: User permission to check private or public services (True for private, False for public).
        :param service_name: The name of the service name to check (as configured in the JSON configuration file).

        :return: A tuple containing the status of the service (True for active, False for inactive, None for error) and a string containing the result message.
        """
        try:
            if service_name not in self.config["services"].keys():
                logging.error(msg=f"Service {service_name} not found")
                return None, ""

            service = self.config["services"][service_name]
            display_name = service.get('display_name', service_name)
            timeout_in_sec = service.get('timeout_in_sec', 30)

            if 'status_command' not in service:
                logging.error(msg=f"Status command (status_command) not found for service {service_name}")
                return None, ""

            status_command: str = service['status_command']
            check_also_stdout_not_containing = service.get('check_also_stdout_not_containing', None)

            res, out_msg = await self.execute_and_verify(command=status_command, display_name=f"état de {display_name}", show_only_std_and_exception=True, timeout_in_sec=timeout_in_sec, display_only_if_critical=False, check_also_stdout_not_containing=check_also_stdout_not_containing)
            return res, out_msg
        except Exception as e:
            out_msg = f"  - ⚠️ **Error checking status of service {service_name}**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return None, out_msg

    async def check_all_services_status(self, is_private: bool, display_only_if_critical: bool=False) -> str:
        """
        Check the status of all services configured in the JSON configuration file.

        :param is_private: User permission to check private or public services (True for private, False for public).

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            logging.info(msg="Checking the status of services in progress...")

            # Define the type hint for the lambda function
            status_to_string: Callable[[Optional[bool]], str] = lambda res: (
                "Error retrieving status" if res is None else
                "Active" if res else
                "Inactive"
            )

            status_to_icon: Callable[[Optional[bool]], str] = lambda res: (
                "⚠️" if res is None else
                "✅" if res else
                "❌"
            )

            for service_name in self.config["services"].keys():
                if is_private or self.config["services"][service_name]['is_private'] == is_private:
                    status, status_msg = await self._get_service_status(is_private=is_private, service_name=service_name)
                    service_status: str = status_to_string(res=status)
                    service_icon: str = status_to_icon(res=status)

                    if status is not True or not display_only_if_critical:
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += f"- {service_icon} {self.config['services'][service_name]['display_name']}: **{service_status}**"
                        if status != True and status_msg != "":
                            out_msg += f"\n{status_msg}"

                        if status is False:
                            out_msg += f"\n  - " + await self.restart_service(is_private=is_private, service_name=service_name, force_restart=False)

        except Exception as e:
            out_msg = f"**Internal error checking services status**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)


        if out_msg != "":
            out_msg = f"# 📱 Services status 📱\n{out_msg}"

        return out_msg

    async def stop_service(self, is_private: bool, service_name: str) -> str:
        """
        Stop a specific service.

        :param is_private: User permission to stop private or public services (True for private, False for public).
        :param service_name: The name of the service name to stop (as configured in the JSON configuration file).

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            if service_name not in self.config['services'].keys():
                out_msg = f"❌ **Service {service_name} not found**."
                logging.error(msg=out_msg)
                return out_msg

            service = self.config['services'][service_name]
            if not is_private and is_private != service['is_private']:
                out_msg = f"❌ **Service {service_name} not authorized to stop in public**."
                logging.error(msg=out_msg)
                return out_msg

            display_name: str = service.get('display_name', service_name)
            if 'stop_command' not in service:
                out_msg = f"❌ **Stop command not found for {display_name}**."
                logging.error(msg=out_msg)
                return out_msg

            timeout_in_sec: int = service.get('timeout_in_sec', 90)

            service_call: str = service['stop_command']
            out_msg: str = ""

            logging.info(f"Trying to stop {display_name} (command: {service_call}) in less than {timeout_in_sec}sec...")

            start_time: float = time.time()
            res, res_msg = await self.execute_and_verify(command=service_call, display_name=f"stop {display_name}", show_only_std_and_exception=True, timeout_in_sec=timeout_in_sec, display_only_if_critical=False)
            end_time: float = time.time()

            if res == True:
                readable_duration: str = "{:.2f}".format(end_time - start_time)
                out_msg = f"✅ **{display_name} stopped with success** in {readable_duration}sec."
                logging.info(msg=out_msg)
            else:
                out_msg = f"❌ **Error stopping service {display_name}**"
                if res_msg and res_msg != "":
                    out_msg += f"\n{res_msg}"
                logging.warning(msg=out_msg)
        except Exception as e:
            out_msg = f"⚠️ **Error stopping service {service_name}**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    #endregion

    #region SSL Certificates

    def _get_certificate_info(self, hostname: str): # type: ignore
        """
        Get the certificate information for a specific hostname.

        :param hostname: The hostname to get the certificate information.

        :return: A dictionary containing the certificate information.
        """
        context: ssl.SSLContext = ssl.create_default_context()
        conn: ssl.SSLSocket = context.wrap_socket(sock=socket.socket(socket.AF_INET), server_hostname=hostname)

        try:
            conn.connect((hostname, 443))
            cert = conn.getpeercert()

            # Get the certificate expiration date
            expiry_date: datetime = datetime.strptime(cert.get("notAfter"), '%b %d %H:%M:%S %Y GMT') # type: ignore

            # Get today's date
            today: datetime = datetime.today()

            # Calculate the number of remaining days
            remaining_days: int = (expiry_date - today).days

            # Check if the certificate is still valid
            is_valid: bool = remaining_days > 0

            logging.info(msg=f"Certificate for {hostname} is valid: {is_valid}, remaining days: {remaining_days}")
            return {
                'is_valid': is_valid,
                'remaining_days': remaining_days,
                'expiry_date': expiry_date,
                'error': None
            } # type: ignore

        except Exception as e:
            logging.exception(msg=f"Error getting certificate info for {hostname}:\n{e}")
            return {
                'hostname': hostname,
                'is_valid': False,
                'remaining_days': 0,
                'expiry_date': None,
                'error': str(e)
            } # type: ignore

        finally:
            conn.close()

    def _check_certificate(self, hostname: str, display_name: str, warning_remaining_days: int, critical_remaining_days: int, display_only_if_critical: bool=False) -> str:
        """
        Check the SSL certificate for a specific hostname.

        :param hostname: The hostname to check the SSL certificate.
        :param display_name: The name of the website to display in the output message.
        :param warning_remaining_days: The warning remaining days for the SSL certificate.
        :param critical_remaining_days: The critical remaining days for the SSL certificate.
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        out_msg: str = ""
        try:
            cert_infos = self._get_certificate_info(hostname=hostname) # type: ignore

            remaining_days: int = 0
            if isinstance(cert_infos["remaining_days"], int):
                remaining_days = cert_infos["remaining_days"]

            expiry_date: datetime = datetime.today()
            if isinstance(cert_infos["expiry_date"], datetime):
                expiry_date = cert_infos["expiry_date"]

            if not cert_infos["is_valid"]:
                out_msg = f"- ❌ **Invalid SSL certificate [{display_name}](https://{hostname})**\n" \
                        f"  - **Certificate expired on {expiry_date.strftime('%d/%m/%Y')}**\n" \
                        f"  - **Renew the SSL certificate immediately**"
                logging.warning(msg=out_msg)
            elif critical_remaining_days > 0 and remaining_days < critical_remaining_days:
                out_msg = f"- ⚠️ **SSL certificate [{display_name}](https://{hostname}) will expire soon**:\n" \
                        f"  - Certificate expires on {expiry_date.strftime('%d/%m/%Y')}\n" \
                        f"  - **{remaining_days} remaining days (which is in less than {critical_remaining_days} days)**\n" \
                        f"  - **Renew the SSL certificate quickly**"
                logging.warning(msg=out_msg)
            elif not display_only_if_critical:
                if warning_remaining_days > 0 and remaining_days < warning_remaining_days:
                    icon: str = "⚠️ "
                elif critical_remaining_days <= 0 and warning_remaining_days <= 0:
                    icon = ""
                else:
                    icon = "✅ "

                out_msg = f"- {icon}[{display_name}](https://{hostname}): {remaining_days} remaining days (expires on {expiry_date.strftime('%d/%m/%Y')}))"
                logging.info(msg=out_msg)

            # Display the error of retrieving the certificate if there is one
            if cert_infos["error"]:
                out_msg += f"\n  - Reason: `{cert_infos['error']}`"
        except Exception as e:
            out_msg = f"- ⚠️ **Error checking SSL certificate of [{display_name}](https://{hostname})**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    def check_all_certificates(self, is_private: bool, display_only_if_critical: bool=False) -> str:
        """
        Check all SSL certificates configured in the JSON configuration file.

        :param is_private: User permission to check private or public certificates (True for private, False for public).
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        try:
            out_msg: str = ""
            for cert_config in self.config['certificates']:
                if is_private or is_private == cert_config['is_private']:
                    hostname = cert_config['website']
                    display_name = cert_config.get('display_name', hostname)
                    # Verify that warning_remaining_days & critical_remaining_days exist, otherwise use -1
                    warning_remaining_days = cert_config.get('warning_remaining_days', -1)
                    critical_remaining_days = cert_config.get('critical_remaining_days', -1)

                    # We only check what is needed
                    if not display_only_if_critical or (display_only_if_critical and critical_remaining_days != -1):
                        result: str = self._check_certificate(hostname=hostname, display_name=display_name, warning_remaining_days=warning_remaining_days, critical_remaining_days=critical_remaining_days, display_only_if_critical=display_only_if_critical)
                        if result and result != "":
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += f"{result}"

            if out_msg != "":
                out_msg = f"# 🔐 Certificates 🔐\n{out_msg}"

            return out_msg
        except Exception as e:
            return f"⚠️ **Error getting SSL certificates**:\n```sh\n{e}\n```"

    #endregion

    #region System Information

    def get_hostname(self) -> str:
        """
        Get the hostname of the system.

        :return: A string containing the result message.
        """
        out_msg: str = "# 🖥️ Hostname 🖥️\n"
        try:
            hostname = socket.gethostname()
            out_msg += f"- **{hostname}**"
            logging.info(msg=out_msg)
        except Exception as e:
            out_msg += f"⚠️ **Error getting hostname**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    def get_os_details(self) -> str:
        """
        Get the OS details.

        :return: A string containing the result message.
        """
        out_msg: str = "# 🖥️ OS 🖥️\n"

        # Get OS details
        try:
            if os.path.exists(path="/etc/os-release"):
                with open(file="/etc/os-release") as f:
                    os_info = {}
                    for line in f:
                        key, value = line.rstrip().split(sep="=", maxsplit=1)
                        os_info[key] = value.strip('"')
                os_version: str = f"{os_info.get('PRETTY_NAME', 'Unknown OS')}" # type: ignore
                out_msg += f"- **{os_version}**"
            else:
                # Fallback method if /etc/os-release is not available
                os_version = platform.platform()
                out_msg += f"- **{os_version}**"

            logging.info(msg=out_msg)
        except Exception as e:
            out_msg += f"⚠️ **Error getting OS details**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    def get_kernel_version(self) -> str:
        """
        Get the kernel version.

        :return: A string containing the result message.
        """
        out_msg: str = "# 🖥️ Kernel version 🖥️\n"
        try:
            # Get Kernel version
            kernel_version: str = subprocess.check_output(args="uname -r", shell=True).decode().strip()
            out_msg += f"- **{kernel_version}**"
            logging.info(msg=out_msg)
        except Exception as e:
            out_msg += f"⚠️ **Error getting kernel version**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    def get_server_datetime(self) -> str:
        """
        Get the server date and time.

        :return: A string containing the result message.
        """
        out_msg: str = "# 🕒 Server datetime 🕒\n"
        try:
            # Get server date and time
            current_datetime: str = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
            out_msg += f"- **{current_datetime}**"
            logging.info(msg=out_msg)
        except Exception as e:
            out_msg += f"⚠️ **Error getting server datetime**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    #endregion

    #region Users

    def get_connected_users(self) -> str:
        """
        Get the connected users.

        :return: A string containing the result message.
        """
        out_msg: str = "# 👥 Connected users 👥\n"
        try:
            # Get connected users
            users = psutil.users()
            if users:
                for user in users:
                    # Show username, IP address and login time
                    out_msg += f"- **{user.name}** (since {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(user.started))})\n"
            else:
                out_msg += "- No user connected"

            logging.info(msg=out_msg)
        except Exception as e:
            out_msg += f"⚠️ **Error getting connected users**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return out_msg

    def _get_recent_user_logins(self, days: int = 7) -> Optional[Dict[str, Set[str]]]:
        """
        Get the recent user logins.

        :param days: The number of days to look back for recent user logins.

        :return: A dictionary containing the recent user logins.
        """
        # Format the date without microseconds (milliseconds)
        past_date: str = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%S')

        try:
            # Fetch the logs since the specified date
            command: str = f"sudo last --ip --hostlast --time-format iso --since '{past_date}' | grep 'pts/'"
            last_output: str = subprocess.check_output(
                args=command,
                shell=True,
                text=True
            ).strip()
        except subprocess.CalledProcessError as e:
            logging.error(msg=f"Error getting recent user logins:\n{e}")
            return None

        logins: List[str] = last_output.splitlines()
        user_ip_dict: Dict[str, Set[str]] = {}

        # Regex pattern to match IP addresses
        ip_pattern: re.Pattern[str] = re.compile(pattern=r'\d+\.\d+\.\d+\.\d+')

        for line in logins:
            parts: List[str] = line.split()
            if len(parts) > 4:  # Ensure the line has enough parts
                username: str = parts[0]
                ip_address: str = parts[-1]

                # Check if IP address is valid and not '0.0.0.0'
                if ip_pattern.match(string=ip_address) and ip_address != '0.0.0.0':
                    if username in user_ip_dict:
                        user_ip_dict[username].add(ip_address)
                    else:
                        user_ip_dict[username] = {ip_address}

        logging.info(msg=f"Recent user logins: {user_ip_dict}")
        return user_ip_dict

    def check_all_recent_user_logins(self, display_only_if_critical: bool=False) -> str:
        """
        Check all recent user logins.

        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        try:
            out_msg: str = ""
            recent_user_connections_config = self.config.get('recent_user_connections', {})

            max_days: int = 7
            allow_all: bool = True
            allowed_ips: List[str] = []

            if recent_user_connections_config:
                max_days = recent_user_connections_config.get('max_days', 7)
                allow_all = recent_user_connections_config.get('allow_all', False)
                if not allow_all:
                    allowed_ips = recent_user_connections_config.get('allowed_ips', [])
            else:
                logging.warning(msg="No recent_user_connections config found, using default values")

            user_ip_dict: Optional[Dict[str, Set[str]]] = self._get_recent_user_logins(days=max_days)

            if user_ip_dict is None:
                out_msg += "⚠️ **Error getting recent user logins**"
                logging.error(msg=out_msg)
            else:
                for user, ip_addresses in user_ip_dict.items():
                    ip_str: str = ', '.join(ip_addresses)
                    # if at least one ip not allowed, display as critical
                    if not allow_all and any(ip not in allowed_ips for ip in ip_addresses):
                        if out_msg != "":
                            out_msg += "\n"

                        # Display in bold the invalid ips
                        ip_str = ', '.join([f"**{ip} not allowed**" if ip not in allowed_ips else ip for ip in ip_addresses])

                        out_msg += f"- 🚨 **{user}** ({ip_str})"

                        logging.warning(msg=out_msg)
                    elif not display_only_if_critical:
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += f"- ✅ **{user}** ({ip_str})"
                        logging.info(msg=out_msg)

            if out_msg != "":
                out_msg = f"# 👥 User logins since {max_days} days 👥\n{out_msg}"

            return out_msg
        except Exception as e:
            return f"⚠️ **Error getting recent user logins**:\n```sh\n{e}\n```"

    #endregion

    #region Ports

    def _is_port_in_required_state(self, display_name: str, port: int, host: str = "localhost", timeout_in_sec: float = 2, want_port_to_be_open: bool = True) -> Tuple[bool, str]:
        """
        Check if a specific port is in the required state (open or closed).

        :param display_name: The name of the port to display in the output message.
        :param port: The port number to check.
        :param host: The host to check the port.
        :param timeout_in_sec: The timeout in seconds to check the port.
        :param want_port_to_be_open: If True, the port should be open, otherwise it should be closed.

        :return: A tuple containing a boolean indicating if the port is in the required state and a string containing the result message.
        """
        out_msg: str = ""

        res: bool = False
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout_in_sec)
            res_port_open: bool = sock.connect_ex((host, port)) == 0
            res = res_port_open == want_port_to_be_open

            if res_port_open:
                if want_port_to_be_open:
                    out_msg = f"✅🔓 {display_name} (Port {port}) **open**"
                    logging.info(msg=out_msg)
                else:
                    out_msg = f"❌🔓 {display_name} (Port {port}) **open (should be closed)**"
                    logging.warning(msg=out_msg)
            else:
                if want_port_to_be_open:
                    out_msg = f"❌🔒 {display_name} (Port {port}) **closed**"
                    logging.warning(msg=out_msg)
                else:
                    out_msg = f"✅🔒 {display_name} (Port {port}) **closed (and should be closed)**"
                    logging.info(msg=out_msg)

            sock.close()
        except Exception as e:
            out_msg = f"⚠️ **Error checking {display_name} port**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)

        return res, out_msg

    async def check_all_ports(self, is_private: bool, display_only_if_critical: bool=False) -> str:
        """
        Check all ports configured in the JSON configuration file (and restart the service if the port is down and service_name_to_restart added in config file).

        :param is_private: User permission to check private or public ports (True for private, False for public).
        :param display_only_if_critical: If True, the string result will only be returned if there is an error during execution.

        :return: A string containing the result message.
        """
        try:
            out_msg: str = ""
            for port_config in self.config['ports']:
                if is_private or is_private == port_config['is_private']:
                    port: int = port_config['port']
                    display_name: str = port_config.get('display_name', f"Port {port}")
                    host: str = port_config.get('host', 'localhost')
                    timeout_in_sec: float = port_config.get('timeout_in_sec', 10)
                    want_port_to_be_open: bool = port_config.get('want_port_to_be_open', True)

                    service_name_to_restart: str = ""
                    if want_port_to_be_open:
                        service_name_to_restart = port_config.get('service_name_to_restart', "")

                    result, result_msg = self._is_port_in_required_state(port=port, host=host, timeout_in_sec=timeout_in_sec, want_port_to_be_open=want_port_to_be_open, display_name=display_name)
                    if result_msg != "" and (not display_only_if_critical or not result):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += f"- {result_msg}"

                    if (not result) and service_name_to_restart != "":
                        if out_msg != "":
                            out_msg += "\n"

                        restart_res: str = await self.restart_service(is_private=is_private, service_name=service_name_to_restart, force_restart=False)
                        out_msg += f"  - {restart_res}"

            if out_msg != "":
                out_msg = f"# 🛡️ Ports 🛡️\n{out_msg}"

            return out_msg
        except Exception as e:
            return f"⚠️ **Error checking ports**:\n```sh\n{e}\n```"

    #endregion

    #region Processes

    async def get_ordered_processes(self, get_non_consuming_processes: bool = False, order_by_ram: bool = True) -> str:
        """
        Get the ordered list of processes by memory and CPU usage.

        :param get_non_consuming_processes: If True, get all processes, otherwise only get processes consuming resources.
        :param order_by_ram: If True, order by RAM usage, otherwise order by CPU usage.

        :return: A string containing the result message.
        """
        try:
            processes = []

            # To get meaningful results, we need to ask cpu percent and wait a bit to get valid cpu_percent values on second iteration
            for dummy_process in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time', 'cmdline']):
                try:
                    # First call to cpu_percent to initialize it
                    dummy_process.cpu_percent(interval=None)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue

            if order_by_ram:
                await asyncio.sleep(delay=1)
            else:
                # Let's get more accurate CPU percent values if we are ordering by CPU usage
                await asyncio.sleep(delay=5)

            # Then we can get the processes
            for process in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time', 'cmdline']):
                try:
                    create_time = datetime.fromtimestamp(process.info['create_time']).strftime("%Y-%m-%d %H:%M:%S")

                    cmdline = ' '.join(process.info['cmdline'])  # Join the command line arguments
                    # Remove extra spaces
                    cmdline = re.sub(r'\s+', ' ', cmdline).strip()
                    if len(cmdline) > 60:
                        cmdline = cmdline[:60] + '...'  # Truncate and add ellipsis

                    processes.append({ # type: ignore
                        'pid': process.info['pid'],
                        'name': process.info['name'],
                        'username': process.info['username'],
                        'cpu_percent': process.info['cpu_percent'],
                        'memory': process.info['memory_info'].rss,  # Resident Set Size (RSS) memory
                        'create_time': create_time,
                        'cmdline': cmdline
                    })
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            # Sort processes by memory usage, then by CPU usage, both in descending order
            processes.sort(key=lambda proc: (proc['memory'] if order_by_ram else proc['cpu_percent'], # type: ignore
                                            proc['cpu_percent'] if order_by_ram else proc['memory'],
                                            proc['create_time']), reverse=True)

            full_res: str = ""
            for proc in processes: # type: ignore
                if not get_non_consuming_processes and proc['cpu_percent'] == 0 and proc['memory'] == 0:
                    continue

                res: str = f"- PID **{proc['pid']}**: {proc['name']} ("

                if proc['cpu_percent'] > 0:
                    res += f"CPU {proc['cpu_percent']}%, "

                if proc['memory'] > 0:
                    res += f"RAM {proc['memory'] // (1024 * 1024)} MB, "

                res += f"👤 {proc['username']}, "
                res += f"⏰ {proc['create_time']}"

                if proc['cmdline'] != "":
                    res += f", 📄 `{proc['cmdline']}`"

                res += ")"

                if full_res != "":
                    full_res += "\n"
                full_res += res

            if full_res != "":
                full_res = f"# 🔄 Processes 🔄\n{full_res}"

            logging.info(msg=full_res)
            return full_res
        except Exception as e:
            out_msg = f"⚠️ **Error getting ordered processes**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    async def kill_process(self, pid: int, timeout_in_sec: int = 10) -> str:
        """
        Kills a process with the specified PID.
        1. Tries to terminate the process gracefully
        2. If the process is still running after the timeout, tries to kill it forcefully

        :param pid: The process ID to kill
        :param timeout_in_sec: The timeout in seconds to wait for the process to terminate gracefully

        :return: A message indicating the result of the operation

        IMPORTANT:
        - The script must be allowed to use "sudo /bin/kill" without password prompt
        (e.g., by adding a sudoers file in /etc/sudoers.d/ with the following content: echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /bin/kill" >> /etc/sudoers.d/USERNAME_HERE)
        """
        try:
            out_msg: str = ""
            process = psutil.Process(pid=pid)

            # Check if process exists
            if not process.is_running():
                out_msg = f"❌ **PID process {pid} not found**."
                logging.error(msg=out_msg)
                return out_msg

            process_name: str = process.name()
            process_username: str = process.username()
            process_cpu_percent: float = process.cpu_percent()
            process_memory: int = process.memory_info().rss // (1024 * 1024)
            process_create_time: str = datetime.fromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")

            process_cmdline: str = ' '.join(process.cmdline())
            process_cmdline = re.sub(r'\s+', ' ', process_cmdline).strip()
            if len(process_cmdline) > 60:
                process_cmdline = process_cmdline[:60] + '...'

            # Attempt to terminate the process
            terminate_command: str = f"sudo /bin/kill -TERM {pid}"
            result_terminate, _ = await self.execute_and_verify(command=terminate_command, display_name=f"stop process {pid} ({process_name})", show_only_std_and_exception=False, timeout_in_sec=timeout_in_sec, display_only_if_critical=False)

            if result_terminate == True:
                out_msg = f"✅ **Process {pid} ({process_name}) stopped with success** (nicely)).\n"
            elif result_terminate == False:
                # Termination did not complete in time or failed
                out_msg = f"⚠️ **Stopping nicely {pid} ({process_name}) failed**.\n"
            else:
                out_msg = f"⚠️ **Stopping nicely {pid} ({process_name}) expired**.\n"

                # Attempt to kill the process
                kill_command: str = f"sudo /bin/kill -KILL {pid}"
                _, strerror_kill = await self.execute_and_verify(command=kill_command, display_name=f"kill process {pid} ({process_name})", show_only_std_and_exception=True, timeout_in_sec=timeout_in_sec, display_only_if_critical=False)
                out_msg += strerror_kill

            if process_cpu_percent > 0:
                out_msg += f"- Used CPU by this process: {process_cpu_percent}%\n"
            if process_memory > 0:
                out_msg += f"- Used RAM by this process: {process_memory} MB\n"
            out_msg += f"- 👤 User: {process_username}\n"
            out_msg += f"- ⏰ Launched at {process_create_time}\n"
            out_msg += f"- 📄 Command: `{process_cmdline}`"

            logging.info(msg=out_msg)
            return out_msg
        except psutil.NoSuchProcess:
            out_msg = f"❌ **PID process {pid} doesn't exist anymore**.\n"
            logging.error(msg=out_msg)
            return out_msg
        except psutil.AccessDenied:
            out_msg = f"❌ **Access denied to stop PID process {pid}**. Execute this script with user allowed to access this process.\n"
            logging.error(msg=out_msg)
            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Erro while stopping PID {pid}**:\n```sh\n{e}\n```"
            logging.error(msg=out_msg)
            return out_msg

    #endregion

    # region Network Information

    def get_network_info(self) -> str:
        """
        Get the network information.

        :return: A string containing the result message.
        """
        try:
            interfaces = psutil.net_if_addrs()
            stats = psutil.net_if_stats()
            network_usage: str = ""

            for interface in interfaces:
                if interface in self.excluded_interfaces or interface not in stats:
                    continue

                ip_addresses = []
                for snic in interfaces[interface]:
                    if snic.family == socket.AF_INET:
                        ip_addresses.append(snic.address) # type: ignore

                # Get network stats
                net_stats = psutil.net_io_counters(pernic=True).get(interface, None)
                if net_stats is None:
                    continue

                # Convert bytes to GB for readability
                receive_bytes: float = net_stats.bytes_recv / (1024 ** 3)
                transmit_bytes: float = net_stats.bytes_sent / (1024 ** 3)

                ip_str: str = ", ".join(ip_addresses) if ip_addresses else "N/A" # type: ignore

                if network_usage != "":
                    network_usage += "\n"
                network_usage += f"- {interface} ({ip_str}): ⬇️ {receive_bytes:,.2f} GB, ⬆️ {transmit_bytes:,.2f} GB"

            if network_usage != "":
                network_usage = f"# 🌐 Network usage 🌐\n{network_usage}"

            logging.info(msg=network_usage)
            return network_usage
        except Exception as e:
            out_msg = f"⚠️ **Error getting network information**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    #endregion

    #region Commands

    async def _execute_command(self, command: str, display_name: str, show_content_if_success: bool, show_content_if_issue: bool, is_content_json: bool, timeout_in_sec: int, display_only_if_critical: bool) -> str:
        try:
            out_msg: str = ""

            # Execute the command
            start_time: float = time.time()
            res, res_msg = await self.execute_and_verify(command=command, display_name=display_name, show_only_std_and_exception=True, timeout_in_sec=timeout_in_sec, display_only_if_critical=display_only_if_critical, is_stdout_json=is_content_json)
            end_time: float = time.time()

            if res == True:
                readable_duration: str = "{:.2f}".format(end_time - start_time)
                out_msg = f"✅ **{display_name} executed with success** in {readable_duration}sec."
                logging.info(msg=out_msg)

                if show_content_if_success:
                    if res_msg != "":
                        out_msg += f"\n{res_msg}"

            elif res == False:
                out_msg = f"⚠️ **{display_name} failed to execute**."
                logging.warning(msg=out_msg)

                if show_content_if_issue:
                    if res_msg != "":
                        out_msg += f"\n{res_msg}"

            else:
                out_msg = f"⚠️ **{display_name} expired**."
                logging.warning(msg=out_msg)

            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error while executing {display_name}**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    async def execute_command(self, is_private: bool, command_name: str) -> str:
        try:
            out_msg: str = ""
            display_name: str = command_name
            for command_config_key in self.config['commands'].keys():
                if command_config_key == command_name:
                    display_name = self.config['commands'][command_config_key]['display_name']
                    command: str = self.config['commands'][command_config_key]['command']
                    is_private_cmd: bool = self.config['commands'][command_config_key]['is_private']

                    if is_private or is_private == is_private_cmd:
                        show_content_if_success: bool = self.config['commands'][command_config_key].get('show_content_if_success', False)
                        show_content_if_issue: bool = self.config['commands'][command_config_key].get('show_content_if_issue', False)
                        is_content_json: bool = self.config['commands'][command_config_key].get('is_content_json', False)
                        timeout_in_sec: int = self.config['commands'][command_config_key].get('timeout_in_sec', 10)

                        res: str = await self._execute_command(command=command, display_name=display_name, show_content_if_success=show_content_if_success,
                                                               show_content_if_issue=show_content_if_issue, is_content_json=is_content_json,
                                                               timeout_in_sec=timeout_in_sec, display_only_if_critical=False)
                        if res != "":
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += f"{res}"
                    else:
                        out_msg = f"⚠️ **Command {display_name} is not allowed**"
                        logging.warning(msg=out_msg)

                    if out_msg != "":
                        out_msg = f"# 📜 Command {display_name} 📜\n{out_msg}"

                    return out_msg

            out_msg = f"⚠️ **Command {display_name} not found**"
            logging.warning(msg=out_msg)
            return out_msg
        except Exception as e:
            return f"⚠️ **Error executing command {command_name}**:\n```sh\n{e}\n```"

    async def execute_all_commands(self, is_private: bool, is_scheduled_tasks_for_issues: bool=False, is_scheduled_tasks_for_infos: bool=False, display_only_if_critical: bool=False) -> str:
        try:
            out_msg: str = ""

            for command_config_key in self.config['commands'].keys():
                if is_private or is_private == self.config['commands'][command_config_key]['is_private']:
                    display_name: str = self.config['commands'][command_config_key]['display_name']
                    command: str = self.config['commands'][command_config_key]['command']
                    show_content_if_success: bool = self.config['commands'][command_config_key].get('show_content_if_success', False)
                    show_content_if_issue: bool = self.config['commands'][command_config_key].get('show_content_if_issue', False)
                    is_content_json: bool = self.config['commands'][command_config_key].get('is_content_json', False)
                    timeout_in_sec: int = self.config['commands'][command_config_key].get('timeout_in_sec', 10)

                    if is_scheduled_tasks_for_issues and not self.config['commands'][command_config_key].get('execute_in_scheduled_tasks_for_issues', False):
                        continue
                    if is_scheduled_tasks_for_infos and not self.config['commands'][command_config_key].get('execute_in_scheduled_tasks_for_infos', False):
                        continue

                    res: str = await self._execute_command(command=command, display_name=display_name, show_content_if_success=show_content_if_success, # type: ignore
                                                           show_content_if_issue=show_content_if_issue, is_content_json=is_content_json,
                                                           timeout_in_sec=timeout_in_sec, display_only_if_critical=display_only_if_critical)
                    if res != "":
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += f"{res}"

            if out_msg != "":
                out_msg = f"# 📜 Commands 📜\n{out_msg}"

            return out_msg
        except Exception as e:
            return f"⚠️ **Error executing commands**:\n```sh\n{e}\n```"

    async def list_commands(self, is_private: bool) -> str:
        try:
            out_msg: str = "# 📜 Commands 📜\n"
            for command_config_key in self.config['commands'].keys():
                if is_private or is_private == self.config['commands'][command_config_key]['is_private']:
                    display_name: str = self.config['commands'][command_config_key]['display_name']
                    out_msg += f"- `{command_config_key}`: {display_name}\n"

            logging.info(msg=out_msg)
            return out_msg
        except Exception as e:
            out_msg = f"⚠️ **Error listing commands**:\n```sh\n{e}\n```"
            logging.exception(msg=out_msg)
            return out_msg

    #endregion

    #region Scheduled Tasks

    async def schedule_task(self, handle_error_message: Callable[[str], Awaitable[None]], is_private: bool) -> None:
        """
        Schedule task to check for issues periodically.
        This function doesn't return anything, it will run indefinitely.

        :param handle_error_message: The function to handle the error message.
        :param is_private: User permission to check private or public services (True for private, False for public).
        """
        logging.info(msg=f"Starting {'private' if is_private else 'public'} scheduled tasks every {self.duration_in_sec_wait_between_each_schedule_task_execution}sec for error handling purpose...")

        if not self.allow_scheduled_tasks_check_for_issues:
            raise Exception("Scheduled tasks are not allowed")

        logging.info(msg=f"Waiting for 45 seconds before starting the execution of {'private' if is_private else 'public'} scheduled tasks to allow the discord bot and linux server to be ready...")
        await asyncio.sleep(delay=45)  # Sleep for 45 sec before lauching the scheduled tasks (to allow the lib to be ready)

        datetime_last_disk_usage_error_displayed: Optional[datetime] = None
        datetime_last_folder_usage_error_displayed: Optional[datetime] = None
        datetime_last_cpu_usage_error_displayed: Optional[datetime] = None
        datetime_last_ram_usage_error_displayed: Optional[datetime] = None
        datetime_last_swap_usage_error_displayed: Optional[datetime] = None
        datetime_last_cpu_temperature_error_displayed: Optional[datetime] = None
        datetime_last_ping_error_displayed: Optional[datetime] = None
        datetime_last_websites_error_displayed: Optional[datetime] = None
        datetime_last_certificates_error_displayed: Optional[datetime] = None
        datetime_last_user_logins_error_displayed: Optional[datetime] = None
        datetime_last_port_error_displayed: Optional[datetime] = None
        datetime_last_services_error_displayed: Optional[datetime] = None
        datetime_last_commands_error_displayed: Optional[datetime] = None
        need_to_check_uptime: bool = True # No need to check uptime every time (since once ok, it can't be wrong)

        if not self.start_scheduled_tasks_immediately:
            logging.info(msg=f"Waiting for {self.duration_in_sec_wait_between_each_schedule_task_execution} seconds before starting the execution of {'private' if is_private else 'public'} scheduled tasks...")
            await asyncio.sleep(delay=self.duration_in_sec_wait_between_each_schedule_task_execution)

        while True:
            out_msg: str = ""
            logging.info(msg="-----------------------------------------------")
            logging.info(msg="Checking services status and all disk usage, CPU, RAM, Swap, CPU temperature and ping of websites periodically...")
            try:
                # Services status
                msg: str = await self.check_all_services_status(is_private=is_private, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_services_error_displayed is None or ((datetime.now() - datetime_last_services_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_services_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Services critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_services_error_displayed is not None:
                    msg="✅ **All services returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_services_error_displayed = None
                else:
                    logging.info(msg="- ✅ Private services are up and running.")

                # Disk usage
                msg = self.check_all_disk_usage(is_private=is_private, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_disk_usage_error_displayed is None or ((datetime.now() - datetime_last_disk_usage_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_disk_usage_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Disk usage critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_disk_usage_error_displayed is not None:
                    msg="✅ **Disk space returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_disk_usage_error_displayed = None
                else:
                    logging.info(msg="- ✅ All disk usage are OK.")

                # Folder usage
                msg = self.check_all_folder_usage(is_private=is_private, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_folder_usage_error_displayed is None or ((datetime.now() - datetime_last_folder_usage_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_folder_usage_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Folder usage critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_folder_usage_error_displayed is not None:
                    msg="✅ **Folder space returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_folder_usage_error_displayed = None
                else:
                    logging.info(msg="- ✅ All folder usage are OK.")

                # Certificates
                msg = self.check_all_certificates(is_private=is_private, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_certificates_error_displayed is None or ((datetime.now() - datetime_last_certificates_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_certificates_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Certificates critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_certificates_error_displayed is not None:
                    msg="✅ **Certificates returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_certificates_error_displayed = None
                else:
                    logging.info(msg="- ✅ Certificates are OK.")

                # Ping
                msg = await self.ping_all_websites(is_private=is_private, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_ping_error_displayed is None or ((datetime.now() - datetime_last_ping_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_ping_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Ping critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_ping_error_displayed is not None:
                    msg="✅ **Website ping returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_ping_error_displayed = None
                else:
                    logging.info(msg="- ✅ Ping of all websites are OK.")

                # Websites availability (GET request)
                msg = await self.check_all_websites(is_private=is_private, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_websites_error_displayed is None or ((datetime.now() - datetime_last_websites_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_websites_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Websites critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_websites_error_displayed is not None:
                    msg="✅ **Websites returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_websites_error_displayed = None
                else:
                    logging.info(msg="- ✅ All websites availability (GET requests) are OK.")

                # Ports
                msg = await self.check_all_ports(is_private=is_private, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_port_error_displayed is None or ((datetime.now() - datetime_last_port_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_port_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Ports critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_port_error_displayed is not None:
                    msg="✅ **Port returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_port_error_displayed = None
                else:
                    logging.info(msg="- ✅ All ports are OK.")

                # Commands
                msg = await self.execute_all_commands(is_private=is_private, is_scheduled_tasks_for_issues=True, is_scheduled_tasks_for_infos=False, display_only_if_critical=True)
                if msg != "":
                    logging.warning(msg=msg)
                    if datetime_last_commands_error_displayed is None or ((datetime.now() - datetime_last_commands_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_commands_error_displayed = datetime.now()
                    else:
                        logging.warning(msg="Commands critical but already notified less than 12 hours ago, not notifying...")
                elif datetime_last_commands_error_displayed is not None:
                    msg="✅ **Commands returned to normal state**"
                    logging.info(msg=msg)
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg
                    datetime_last_commands_error_displayed = None
                else:
                    logging.info(msg="- ✅ All commands are OK.")

                # User logins
                if is_private:
                    msg = self.check_all_recent_user_logins(display_only_if_critical=True)
                    if msg != "":
                        logging.warning(msg=msg)
                        if datetime_last_user_logins_error_displayed is None or ((datetime.now() - datetime_last_user_logins_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += msg
                            datetime_last_user_logins_error_displayed = datetime.now()
                        else:
                            logging.warning(msg="User logins critical but already notified less than 12 hours ago, not notifying...")
                    elif datetime_last_user_logins_error_displayed is not None:
                        msg="✅ **Last user logins returned to normal state**"
                        logging.info(msg=msg)
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_user_logins_error_displayed = None
                    else:
                        logging.info(msg="- ✅ All user logins are OK.")

                # CPU
                if is_private:
                    msg = self.check_cpu_usage(display_only_if_critical=True)
                    if msg != "":
                        logging.warning(msg=msg)
                        if datetime_last_cpu_usage_error_displayed is None or ((datetime.now() - datetime_last_cpu_usage_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += msg
                            datetime_last_cpu_usage_error_displayed = datetime.now()
                        else:
                            logging.warning(msg="CPU usage critical but already notified less than 12 hours ago, not notifying...")
                    elif datetime_last_cpu_usage_error_displayed is not None:
                        msg = "✅ **CPU usage returned to normal state**"
                        logging.info(msg=msg)
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_cpu_usage_error_displayed = None
                    else:
                        logging.info(msg="- ✅ CPU usage is OK.")

                # RAM
                if is_private:
                    msg = self.check_ram_usage(display_only_if_critical=True)
                    if msg != "":
                        logging.warning(msg=msg)
                        if datetime_last_ram_usage_error_displayed is None or ((datetime.now() - datetime_last_ram_usage_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += msg
                            datetime_last_ram_usage_error_displayed = datetime.now()
                        else:
                            logging.warning(msg="RAM usage critical but already notified less than 12 hours ago, not notifying...")
                    elif datetime_last_ram_usage_error_displayed is not None:
                        msg = "✅ **RAM usage returned to normal state**"
                        logging.info(msg=msg)
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_ram_usage_error_displayed = None
                    else:
                        logging.info(msg="- ✅ RAM usage is OK.")

                # Swap
                if is_private:
                    msg = self.check_swap_usage(display_only_if_critical=True)
                    if msg != "":
                        logging.warning(msg=msg)
                        if datetime_last_swap_usage_error_displayed is None or ((datetime.now() - datetime_last_swap_usage_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += msg
                            datetime_last_swap_usage_error_displayed = datetime.now()
                        else:
                            logging.warning(msg="Swap usage critical but already notified less than 12 hours ago, not notifying...")
                    elif datetime_last_swap_usage_error_displayed is not None:
                        msg = "✅ **SWAP usage returned to normal state**"
                        logging.info(msg=msg)
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_swap_usage_error_displayed = None
                    else:
                        logging.info(msg="- ✅ Swap usage is OK.")

                # CPU temperature
                if is_private:
                    msg = self.check_cpu_temperature(display_only_if_critical=True)
                    if msg != "":
                        logging.warning(msg=msg)
                        if datetime_last_cpu_temperature_error_displayed is None or ((datetime.now() - datetime_last_cpu_temperature_error_displayed).total_seconds() > self.max_duration_seconds_showing_same_error_again_in_scheduled_tasks):
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += msg
                            datetime_last_cpu_temperature_error_displayed = datetime.now()
                        else:
                            logging.warning(msg="CPU temperature critical but already notified less than 12 hours ago, not notifying...")
                    elif datetime_last_cpu_temperature_error_displayed is not None:
                        msg = "✅ **CPU temperature returned to normal state**"
                        logging.info(msg=msg)
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg
                        datetime_last_cpu_temperature_error_displayed = None
                    else:
                        logging.info(msg="- ✅ CPU temperature is OK.")

                # Uptime
                if is_private:
                    if need_to_check_uptime:
                        msg = self.check_uptime(display_only_if_critical=True)
                        need_to_check_uptime = False
                        if msg != "":
                            logging.warning(msg=msg)
                            if out_msg != "":
                                out_msg += "\n"
                            out_msg += msg
                        else:
                            logging.info(msg="- ✅ Uptime is OK.")
            except Exception as e:
                out_msg = f"**Internal error during periodic server check task**:\n```sh\n{e}\n```"
                logging.exception(msg=out_msg)

            logging.info(msg="-----------------------------------------------")

            if out_msg != "":
                # Send the message
                await handle_error_message(out_msg)

            logging.info(msg=f"Waiting {self.duration_in_sec_wait_between_each_schedule_task_execution} seconds before next execution of {'private' if is_private else 'public'} scheduled tasks...")
            await asyncio.sleep(delay=self.duration_in_sec_wait_between_each_schedule_task_execution)

    async def schedule_task_show_info(self, show_message: Callable[[str], Awaitable[None]], is_private: bool) -> None:
        """
        Schedule task to show system information periodically.
        This function doesn't return anything, it will run indefinitely.

        :param show_message: The function to show the message.
        :param is_private: User permission to check private or public services (True for private, False for public).
        """
        logging.info(msg=f"Starting {'private' if is_private else 'public'} scheduled tasks every {self.duration_in_sec_wait_between_each_schedule_task_show_info_execution}sec for information purpose...")

        if not self.allow_scheduled_task_show_info:
            raise Exception("Scheduled show info tasks are not allowed")

        logging.info(msg=f"Waiting for 45 seconds before starting the execution of {'private' if is_private else 'public'} show info scheduled tasks to allow the discord bot and linux server to be ready...")
        await asyncio.sleep(delay=45)

        if not self.start_scheduled_task_show_info_immediately:
            logging.info(msg=f"Waiting for {self.duration_in_sec_wait_between_each_schedule_task_show_info_execution} seconds before starting the execution of {'private' if is_private else 'public'} show info scheduled tasks...")
            await asyncio.sleep(delay=self.duration_in_sec_wait_between_each_schedule_task_show_info_execution)

        while True:
            try:
                out_msg: str = ""
                logging.info(msg="-----------------------------------------------")

                # Services status
                msg: str = await self.check_all_services_status(is_private=is_private, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # Disk usage
                msg = self.check_all_disk_usage(is_private=is_private, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # Folder usage
                msg = self.check_all_folder_usage(is_private=is_private, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # Certificates
                msg = self.check_all_certificates(is_private=is_private, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # Ping
                msg = await self.ping_all_websites(is_private=is_private, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # Websites availability (GET request)
                msg = await self.check_all_websites(is_private=is_private, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # Ports
                msg = await self.check_all_ports(is_private=is_private, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # Commands
                msg = await self.execute_all_commands(is_private=is_private, is_scheduled_tasks_for_issues=False, is_scheduled_tasks_for_infos=True, display_only_if_critical=False)
                if msg != "":
                    if out_msg != "":
                        out_msg += "\n"
                    out_msg += msg

                # User logins
                if is_private:
                    msg = self.check_all_recent_user_logins(display_only_if_critical=False)
                    if msg != "":
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg

                # CPU
                if is_private:
                    msg = self.check_cpu_usage(display_only_if_critical=False)
                    if msg != "":
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg

                # RAM
                if is_private:
                    msg = self.check_ram_usage(display_only_if_critical=False)
                    if msg != "":
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg

                # Swap
                if is_private:
                    msg = self.check_swap_usage(display_only_if_critical=False)
                    if msg != "":
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg

                # CPU temperature
                if is_private:
                    msg = self.check_cpu_temperature(display_only_if_critical=False)
                    if msg != "":
                        if out_msg != "":
                            out_msg += "\n"
                        out_msg += msg

                if out_msg != "":
                    out_msg = f"# System state at {time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())}\n{out_msg}"
                    await show_message(out_msg)

                logging.info(msg="-----------------------------------------------")
            except Exception as e:
                out_msg = f"**Internal error during periodic server show info task**:\n```sh\n{e}\n```"
                logging.exception(msg=out_msg)

            logging.info(msg=f"Waiting {self.duration_in_sec_wait_between_each_schedule_task_show_info_execution} seconds before next execution of {'private' if is_private else 'public'} show info scheduled tasks...")
            await asyncio.sleep(delay=self.duration_in_sec_wait_between_each_schedule_task_show_info_execution)

    #endregion
