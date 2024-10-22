#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# Copyright © 2023 Auromix.                                                   #
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
# Description: Decorator for profiling and analyzing performance of functions #
# Author: Herman Ye                                                           #
###############################################################################

import time
import atexit
import subprocess
import os
import sys
import pstats
import functools
import matplotlib.pyplot as plt
import yappi
from auro_utils import Logger
# auro_logger = Logger(log_level="debug")


class AuroProfiler:
    """AuroProfiler is a decorator class wrapper for yappi profiler.
    It can be used to profile and analyze the performance of functions.
    # https://github.com/sumerc/yappi

    Args:
        function (function): The function to be profiled.
        profile_file_name (str, optional): The name of the profiling results file. Defaults to "profiler_results".
        clock_type (str, optional): The clock type of the profiler. Can be "wall" or "cpu". Defaults to "wall".

    Returns:
        function: The decorated function.

    """
    _initialized = False
    _file_full_path = None
    _main_start_time = None
    _main_count_time = None
    _profiled_functions = []
    _logger = None

    def __init__(self, function, *args, **kwargs):
        """Initialize the profiler.

        Args:
            function (function): The function to be profiled.
            profile_file_name (str, optional): The name of the profiling results file. Defaults to "profiler_results".
            clock_type (str, optional): The clock type of the profiler. Can be "wall" or "cpu". Defaults to "wall".

        Returns:
            function: The decorated function.

        """
        # Get function
        self.function = function
        # Initialize the profiler, logger and exit handler
        if not AuroProfiler._initialized:
            # Count the time spent in main
            AuroProfiler._main_start_time = time.perf_counter()
            # Register the exit handler
            atexit.register(self.exit_handler)
            sys.excepthook = self.analysis_excepthook

            # Set profiler clock type
            # Info@Herman Ye: Clock_type can be "wall" or "cpu"
            # Warning@Herman Ye: Clock_type must be set in the first call of the profiler
            clock_type = kwargs.get('clock_type', 'wall')
            yappi.set_clock_type(clock_type)
            # Set the initialized flag
            AuroProfiler._initialized = True

    def __call__(self, *args, **kwargs):
        """Run the function and get the simple time profiling results.
        """
        # Initialize the logger
        # Warning@Herman Ye: The logger in profiler should be initialized after the logger in the main function
        # to avoid the conflict of the log file path.
        if AuroProfiler._logger is None:
            AuroProfiler._logger = Logger(log_level="debug")
            AuroProfiler._file_full_path = f"{AuroProfiler._logger.logs_directory}/profiler_results.pstats"
            if not os.path.exists(AuroProfiler._logger.logs_directory):
                os.makedirs(AuroProfiler._logger.logs_directory)
        # Log
        AuroProfiler._logger.log_trace(
            f"Profiling function {self.function.__qualname__}...")
        # Start the profiler
        yappi.start()
        # Run the function and get the result
        result = self.function(*args, **kwargs)
        # Stop the profiler
        yappi.stop()
        # Log
        AuroProfiler._logger.log_trace(
            f"Profiling function {self.function.__qualname__} finished.")
        # Get the function profiling results
        func_stats = yappi.get_func_stats()
        # Log the time spent in the function
        func_stat = next(
            (stat for stat in func_stats if (stat[0] == self.function.__qualname__ or stat[0] == self.function.__name__)), None)

        if func_stat is not None:
            AuroProfiler._logger.log_debug(
                f"Function <green>{func_stat[0]}</green> spent <green>{format(func_stat[6], '.6f')}</green> seconds in total.", specific_format=True)
            AuroProfiler._profiled_functions.append(func_stat[0])
        return result

    def analysis_excepthook(self, exc_type, exc_value, exc_traceback):
        """This excepthook is used to unregister the exit handler if an exception occurs
        """
        atexit.unregister(self.exit_handler)
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    def exit_handler(self):
        """Exit handler to stop the profiler and analyze the profiling results.
        """
        # Count the time spent in main
        AuroProfiler._main_count_time = time.perf_counter()-AuroProfiler._main_start_time
        AuroProfiler._logger.log_debug(
            f"Function <red>MAIN</red> spent <green>{format(AuroProfiler._main_count_time, '.6f')}</green> seconds in total.", specific_format=True)
        # Save the function profiling results
        yappi.get_func_stats().save(AuroProfiler._file_full_path, type="pstat")
        AuroProfiler._logger.log_debug(
            f"Profiling results saved to:\n<green>{AuroProfiler._file_full_path}</green>", specific_format=True)
        # Analyze the profiling results into png with gprof2dot
        self._analyze_profile()

    def _analyze_profile(self):
        """Analyze the profiling results into png with gprof2dot and graphviz.
        """
        file_to_analyze = AuroProfiler._file_full_path
        dir_path = os.path.dirname(file_to_analyze)
        try:
            AuroProfiler._logger.log_trace("Analyzing profiling results...")
            # Convert the profiling results into dot file
            gprof2dot_command = f"gprof2dot -f pstats {file_to_analyze} -o {dir_path}/profiler_results.dot"
            subprocess.run(gprof2dot_command, shell=True)
            # Convert the dot file into png
            dot_command = f"dot -Tpng {dir_path}/profiler_results.dot -o {dir_path}/profiler_results.png"
            subprocess.run(dot_command, shell=True)
            # Draw pie chart
            self._draw_pie_chart_and_table()

        except Exception as e:
            # Warning@Herman Ye: gprof2dot and graphviz are required to analyze the profiling results.
            AuroProfiler._logger.log_error(
                f"Failed to analyze profiling results: {e}")
            sys.exit(1)

    def _draw_pie_chart_and_table(self):
        dir_path = os.path.dirname(AuroProfiler._file_full_path)
        p = pstats.Stats(AuroProfiler._file_full_path)
        p.sort_stats('cumulative')
        # Get the time spent in main
        if AuroProfiler._main_count_time is not None:
            total_time = AuroProfiler._main_count_time
        else:
            raise ValueError("Main count time is None")
        cumtime_dict = {}
        ncall_dict = {}
        # Get time spent in profiled functions
        for stat in p.stats.items():
            func_name = stat[0][2]
            cumtime = float(format(stat[1][3], ".6f"))
            ncall = stat[1][0]
            # Ignore time spent less than 0.001s
            if cumtime >= 0.001:
                cumtime_dict[func_name] = cumtime
                ncall_dict[func_name] = ncall
        # Only keep the time spent in profiled functions
        cumtime_dict = dict(
            filter(lambda item: item[0] in AuroProfiler._profiled_functions, cumtime_dict.items()))
        ncall_dict = dict(
            filter(lambda item: item[0] in AuroProfiler._profiled_functions, ncall_dict.items()))
        # Get time spent in other functions
        others_time = float(
            format(total_time-sum(cumtime_dict.values()), '.6f'))
        if others_time < 0:
            total_time = sum(cumtime_dict.values())
            others_time = 0.
            AuroProfiler._logger.log_warning(
                "The total time spent in profiled functions exceeds the total time spent in the main function. "
                "This is due to the inclusion of subcall times in 'ttot', leading to repeated statistics. "
                "As a result, the generated pie chart may not be accurate. Please refer to the table for precise data. "
                "To avoid this, consider avoiding nested usage of the profiler."
            )
        else:
            cumtime_dict['others'] = others_time
            ncall_dict['others'] = 1
        # Sort the cumtime_dict by cumtime
        cumtime_dict = dict(sorted(cumtime_dict.items(),
                            key=lambda item: item[1], reverse=True))
        # Draw pie chart

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = pct*total/100.0
                return '{p:.2f}%\n{v:.3f}s'.format(p=pct, v=val)
            return my_autopct
        fig1, ax1 = plt.subplots()
        ax1.pie(cumtime_dict.values(),
                autopct=make_autopct(cumtime_dict.values()))
        ax1.legend(cumtime_dict.keys(), loc="center left",
                   bbox_to_anchor=(1, 1))
        plt.savefig(os.path.join(dir_path, 'profiler_pie_chart.png'),
                    bbox_inches='tight')

        # Draw table
        fig2, ax2 = plt.subplots()
        ax2.axis('tight')
        ax2.axis('off')
        # Create data for the table
        table_data = []
        for func, cumtime in cumtime_dict.items():
            table_data.append([func, cumtime, ncall_dict[func], format(
                cumtime/ncall_dict[func], '.6f')])
        # Create table
        table = ax2.table(cellText=table_data, colLabels=[
            'Function', 'CumTime', 'Ncalls', 'PerTime'], loc='center')
        table.auto_set_font_size(True)
        table.auto_set_column_width(col=list(range(len(table_data[0]))))
        plt.savefig(os.path.join(dir_path, 'profiler_table.png'),
                    bbox_inches='tight')


def auro_profiler(function):
    """Decorator for profiling and analyzing performance of functions.
    """
    profiler = AuroProfiler(function)

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if yappi.is_running():
            return function(*args, **kwargs)
        else:
            return profiler(*args, **kwargs)

    return wrapper
