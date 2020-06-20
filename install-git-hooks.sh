#!/usr/bin/env bash

POSIXLY_CORRECT=1 set -o errexit && set -o nounset && set -o pipefail && unset POSIXLY_CORRECT
ln -sf pre-push.sh .git/hooks/pre-push
