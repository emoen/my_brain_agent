#!/usr/bin/env bash
# Source this file to load environment variables:
#   source load_env.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -f "$SCRIPT_DIR/.env" ]]; then
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
    echo "✓ Environment variables loaded from .env"
else
    echo "✗ .env file not found in $SCRIPT_DIR" >&2
    return 1 2>/dev/null || exit 1
fi
