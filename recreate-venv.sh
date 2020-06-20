#!/usr/bin/env bash

POSIXLY_CORRECT=1 set -o errexit && set -o nounset && set -o pipefail && unset POSIXLY_CORRECT

cd ~/logging_configurator

echo 'Re-create venv in `.venv` directory'
rm -rf .venv
/usr/bin/python3.6 -m venv --copies .venv

echo "Install pip, wheel, setuptools, and pip-tools."
# shellcheck disable=SC1090
source .venv/bin/activate
pip install 'pip>=20.1.1' --upgrade
pip install wheel --upgrade
pip install setuptools --upgrade
pip install pip-tools --upgrade

pip-sync

pip install -e ./ --upgrade

pip check
