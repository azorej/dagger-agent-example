#!/bin/bash

# STANDARD PREAMBLE: BEGIN (do not edit)

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "${SCRIPT_DIR}/common.sh"

# STANDARD PREAMBLE: END (do not edit)

if [ -z ${1+x} ] ; then
    log_error "Absent argument: {HOST_USER}"
    exit 1
fi
HOST_USER="$1"

if [ -z ${2+x} ] ; then
    log_error "Absent argument: {WORKSPACE_PATH}"
    exit 1
fi
WORKSPACE_PATH="$2"

sudo chown -R "$HOST_USER":"$HOST_USER" "/home/${HOST_USER}/.cache"
# Don't try to change owner for git directories
ls -A "$WORKSPACE_PATH" | egrep -vx '.git(hub)?' | xargs -I{} sudo chown -R "$HOST_USER" "${WORKSPACE_PATH}/{}"

git config --global --add safe.directory "$WORKSPACE_PATH"

cd "$WORKSPACE_PATH/test_agent"
pre-commit install

uname -a