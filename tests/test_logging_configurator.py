"""Test `logging_configurator` package."""

import os.path
from tempfile import TemporaryDirectory
import os
import shutil
import sys


def test_common_scenario():
    """Test common scenario where we configured logging to a file, and to stdout and stderr.

    Note that errors, warnings, and exception traceback should appear in the log file and in stderr but not in stdout.
    """

    with TemporaryDirectory(prefix="logging_configurator_test") as temp_dir_path:
        log_file_path = os.path.join(temp_dir_path, "log.txt")

        script_path = os.path.join(temp_dir_path, "script.py")
        stdout_path = os.path.join(temp_dir_path, "stdout.txt")
        stderr_path = os.path.join(temp_dir_path, "stderr.txt")
        shutil.copyfile(os.path.join(os.path.dirname(__file__), "script.py"), script_path)

        cmd = f"{sys.executable} {script_path} > {stdout_path} 2> {stderr_path}"
        os.system(cmd)

        with open(log_file_path, "r") as f:
            actual_log_file_content = f.readlines()

        with open(stdout_path, "r") as f:
            actual_stdout_content = f.readlines()

        with open(stderr_path, "r") as f:
            actual_stderr_content = f.readlines()

        assert actual_log_file_content != actual_stdout_content
        assert actual_log_file_content == actual_stdout_content + actual_stderr_content
