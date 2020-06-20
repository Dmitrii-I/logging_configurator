#!/usr/bin/env bash

POSIXLY_CORRECT=1 set -o errexit && set -o nounset && set -o pipefail && unset POSIXLY_CORRECT

echo Test shell scripts with shellcheck
files="$(find -L ./ -iname '*.sh')"
for f in $files; do
    echo "Test $f with shellcheck"
    shellcheck --external-sources "$f"
    echo PASSED
done
echo PASSED
