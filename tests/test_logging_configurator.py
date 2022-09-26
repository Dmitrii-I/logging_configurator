"""Test `logging_configurator` package."""

import os.path
from tempfile import TemporaryDirectory, NamedTemporaryFile
import os
import shutil
import sys
from pathlib import Path
from logging_configurator import configure_logging


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


def test_directory_creation():
    """Test that `configure_logging` creates necessary directory tree to save the log file.

    For example calling `configure(path="~/foo/bar/log.log")` should not fail if directory tree ~/foo/bar does not
    exist. Instead ,the directory tree should be created automatically.
    """
    with TemporaryDirectory() as td:
        path = Path(td) / Path("foo/bar.log")
        assert not os.path.exists(path=path)
        configure_logging(path=path)
        assert os.path.exists(path=path)
