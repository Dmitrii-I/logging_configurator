"""Setup configuration"""

import os.path
import sys
from setuptools import setup, Command, find_packages
from shutil import rmtree


class UploadCommand(Command):
    """ Shamelessly copied from Kenneth Reitz. """

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine…")
        os.system("twine upload dist/*")

        sys.exit()


package_name = "logging_configurator"

meta = {}
with open("src/logging_configurator/__init__.py") as f:
    for line in f:
        try:
            exec(line, meta)
        except ModuleNotFoundError:
            pass

setup(
    author="Dmitrii Izgurskii",
    author_email="izgurskii@gmail.com",
    cmdclass={"upload": UploadCommand},
    description="One-liner logging configurator for Python.",
    keywords="logging",
    license="MIT",
    long_description="Configure logging in one line and fogetaboutit.",
    name=package_name,
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["contrib", "docs", "*test*"]),
    python_requires=">=3.6.0",
    url="https://github.com/Dmitrii-I/logging-configurator",
    version=meta["__version__"],
    include_package_data=True,
)
