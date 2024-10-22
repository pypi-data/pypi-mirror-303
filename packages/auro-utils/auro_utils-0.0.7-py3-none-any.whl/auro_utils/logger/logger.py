#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# Copyright © 2023-2024 Auromix.                                              #
#                                                                             #
# Licensed under the Apache License, Version 2.0 (the "License");             #
# You may not use this file except in compliance with the License.            #
# You may obtain a copy of the License at                                     #
#                                                                             #
#     http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS,           #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
# See the License for the specific language governing permissions and         #
# limitations under the License.                                              #
#                                                                             #
# Description: Logger class for console and file.                             #
# Author: Herman Ye                                                           #
###############################################################################


"""
This module defines a Logger class that uses the loguru library for logging.
The Logger class is designed as a singleton, meaning only one instance of this class can exist at a time.
The Logger class provides methods for logging at different levels including trace, debug, info, success, warning, error, critical, and exception.
It also supports logging to both the console and a file. The console log level and the use of file logging can be configured during the initialization of the Logger instance.
The Logger class also provides a method to find the package directory of the script that calls the Logger.
"""

import sys
import os
import time
import inspect


class Logger():
    """
    This is a Logger class that utilizes the loguru library for logging. It is designed as a singleton,
    meaning only one instance of this class can exist at a time. This class provides methods for logging
    at different levels including trace, debug, info, success, warning, error, critical, and exception.
    It also supports logging to both the console and a file. The console log level and the use of file
    logging can be configured during the initialization of the Logger instance.

    https://loguru.readthedocs.io/en/stable/
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        # If the class instance is not created, create one
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            return cls._instance
        # If the class instance is already created, return the created one
        else:
            cls._instance.log_trace(
                "Logger already exists! Return the existing one.")
            cls._instance.log_trace(
                f"[log_level] = [{cls._instance.log_level}]")
            if cls._instance.use_file_log:
                cls._instance.log_trace(
                    f"[log_path] = [{cls._instance.log_path}]")

            return cls._instance

    def __init__(self, log_level: str = "info",
                 use_file_log: bool = False,
                 log_path: str = None,
                 serialize: bool = False
                 ):
        """Init logger.

        Args:
            log_level (str, optional):
                Log level. Defaults to "info".
                Options: [trace, debug, info, success, warning, error, critical].
            use_file_log (bool, optional):
                Whether to use file log. Defaults to False.
            log_path (str, optional):
                Log path. Defaults to None.
            serialize (bool, optional):
                Whether to serialize the log. Defaults to False.
        """
        # If class is already initialized, skip the init
        if Logger._initialized:
            return

        # Init loguru logger
        import loguru
        self._logger = loguru.logger

        # Init default parameters
        self.log_level = log_level
        self.use_file_log = use_file_log
        self.log_path = log_path
        self.serialize = serialize
        self._default_message_tag = None
        self.message_tag = None
        self.logger_level = "TRACE"
        self.diagnose = False
        self.backtrace = False
        self.enqueue = True

        # Get caller file
        caller_file = inspect.stack()[1].filename
        caller_file_name = os.path.splitext(
            os.path.basename(caller_file))[0]

        # Get the directory of the script which calls this function
        script_directory = os.path.dirname(
            os.path.abspath(caller_file))

        # Get the top-level package directory
        package_directory = self.find_package_directory(
            script_directory)

        # Get current time
        current_sys_time = time.strftime(
            "%Y_%m_%d_%H_%M", time.localtime())
        # Get default logs directory
        self.logs_directory = os.path.join(
            package_directory, 'logs', current_sys_time)

        if self.log_level == "trace":
            self.logger_level = "TRACE"
            self.diagnose = True
            self.backtrace = True
        elif self.log_level == "debug":
            self.logger_level = "DEBUG"
            self.diagnose = True
            self.backtrace = True
        elif self.log_level == "info":
            self.logger_level = "INFO"
            self.backtrace = True
        elif self.log_level == "success":
            self.logger_level = "SUCCESS"
            self.backtrace = True
        elif self.log_level == "warning":
            self.logger_level = "WARNING"
            self.backtrace = True
        elif self.log_level == "error":
            self.logger_level = "ERROR"
            self.backtrace = True
        elif self.log_level == "critical":
            self.logger_level = "CRITICAL"
            self.backtrace = True
        else:
            raise ValueError(
                "Log level should be one of [trace, debug, info, success, warning, error, critical]")

        # Remove default logger
        # Try to remove the default handler
        try:
            self._logger.remove(0)
        except Exception:
            # Ignore the error if the handler does not exist
            pass

        # Add console logger
        try:
            self._logger.add(
                sink=sys.stdout,
                level=self.logger_level,
                format="<d><green><b>TIME</b> {time:YYYY-MM-DD HH:mm:ss.SSS} | <b>PID</b> {process}:{thread} | <b>TAG</b> {extra[tag]}</green> </d>  \n<level>[{level}] {message}</level>",
                diagnose=self.diagnose,
                backtrace=self.backtrace,
                enqueue=self.enqueue,
            )
            # Add tag
            self._default_message_tag = f"{caller_file_name}"
            self.message_tag = self._default_message_tag

        except Exception as e:
            print(f"Failed to add console logger: {e}")

        # Add file logger
        if self.use_file_log:

            # Get log path
            if self.log_path is not None:
                # Path check
                if not os.path.exists(self.log_path):
                    self.log_warning(
                        f"Log path does not exist: {self.log_path}")
                    os.makedirs(self.log_path,)
                    self.log_success(f"Log path created: {self.log_path}")

            else:
                self.log_path = package_directory

            # Generate log file directory
            self.logs_directory = os.path.join(
                self.log_path, 'logs', current_sys_time)

            try:
                # Create file log directory
                if not os.path.exists(self.logs_directory):
                    os.makedirs(self.logs_directory)
                # Generate log file name
                file_name = f"{caller_file_name}.log"
                full_path_file_name = os.path.join(
                    self.logs_directory, file_name)
                # Log
                self.log_debug(
                    f"Log file will be saved to: \n{full_path_file_name}")
                # Add file logger
                self._logger.add(
                    sink=full_path_file_name,
                    level=self.logger_level,
                    format="{level}|{time:YYYY-MM-DD HH:mm:ss.SSS}|{file}:{name}:{module}:{function}:{line}|{message}",
                    serialize=True,
                    diagnose=self.diagnose,
                    backtrace=self.backtrace,
                    enqueue=self.enqueue,
                )
            except Exception as e:
                print(f"Failed to add file logger: {e}")

        Logger._initialized = True
        self.log_debug("Logger initialized.")

    def find_package_directory(self, current_directory=os.path.dirname(os.path.abspath(__file__))):
        while True:
            parent_directory = os.path.dirname(current_directory)
            if not os.path.isfile(os.path.join(parent_directory, '__init__.py')):
                return current_directory
            current_directory = parent_directory

    def get_log_path(self):
        return self.log_path

    def check_exception(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, Exception):
                return True

        for key, value in kwargs.items():
            if isinstance(value, Exception):
                return True
        return False

    def __repr__(self):
        if self.use_file_log:
            return f'Logger, log_level={self.log_level}, log_path={self.log_path})'
        return f'Logger, log_level={self.log_level})'

    def log_trace(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)
        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).trace(
                message, *args, **kwargs)
            return

        self._logger.bind(tag=self.message_tag).trace(message, *args, **kwargs)

    def log_debug(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)

        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).debug(
                message, *args, **kwargs)
            return

        self._logger.bind(tag=self.message_tag).debug(message, *args, **kwargs)

    def log_info(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)

        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).info(
                message, *args, **kwargs)
            return

        self._logger.bind(tag=self.message_tag).info(message, *args, **kwargs)

    def log_success(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)

        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).success(
                message, *args, **kwargs)
            return
        self._logger.bind(tag=self.message_tag).success(
            message, *args, **kwargs)

    def log_warning(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)

        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).warning(
                message, *args, **kwargs)
            return

        self._logger.bind(tag=self.message_tag).warning(
            message, *args, **kwargs)

    def log_error(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)

        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).error(
                message, *args, **kwargs)
            return

        if self.check_exception(*args, **kwargs):
            self._logger.bind(tag=self.message_tag).opt(exception=True).error(
                message, *args, **kwargs)
            return
        else:
            self._logger.bind(tag=self.message_tag).error(
                message, *args, **kwargs)
            return

    def log_critical(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)

        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).critical(
                message, *args, **kwargs)
            return

        if self.check_exception(*args, **kwargs):
            self._logger.bind(tag=self.message_tag).opt(exception=True).critical(
                message, *args, **kwargs)
            return
        else:
            self._logger.bind(tag=self.message_tag).critical(
                message, *args, **kwargs)
            return

    def log_exception(self, message, *args, **kwargs):
        self.message_tag = kwargs.pop('tag', self._default_message_tag)

        if kwargs.pop('specific_format', False):
            self._logger.bind(tag=self.message_tag).opt(colors=True).exception(
                message, *args, **kwargs)
            return

        self._logger.bind(tag=self.message_tag).exception(
            message, *args, **kwargs)
