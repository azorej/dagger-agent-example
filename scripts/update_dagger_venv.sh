#!/bin/bash

# STANDARD PREAMBLE: BEGIN (do not edit)

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "${SCRIPT_DIR}/common.sh"

# STANDARD PREAMBLE: END (do not edit)

check_installed uv "https://docs.astral.sh/uv/getting-started/installation/"
check_installed dagger "https://docs.dagger.io/install/"

log_info "Updating Dagger Workspace..."
cd "$REPO_DIR/test_agent/workspace"
dagger develop
uv sync

log_info "Updating Dagger project..."
cd "$REPO_DIR"
dagger develop
uv sync --project test_agent

log_info "Success!"