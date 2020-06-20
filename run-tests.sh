#!/usr/bin/env bash

POSIXLY_CORRECT=1 set -o errexit && set -o nounset && set -o pipefail && unset POSIXLY_CORRECT

./test-shell-scripts-with-shellcheck.sh
./check-formatting-with-black.sh

./recreate-venv.sh

source .venv/bin/activate
pytest -vv --log-cli-level=DEBUG tests/
