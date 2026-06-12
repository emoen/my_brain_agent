#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_ACTIVATE="$SCRIPT_DIR/../.venv/bin/activate"

if [[ -z "${VIRTUAL_ENV:-}" ]]; then
  if [[ -f "$VENV_ACTIVATE" ]]; then
    echo "[ENV] No active virtual environment detected. Activating $VENV_ACTIVATE"
    # shellcheck disable=SC1090
    source "$VENV_ACTIVATE"
  else
    echo "[ERR] Could not find virtual environment at $VENV_ACTIVATE"
    echo "      Create it first: python3 -m venv ../.venv"
    exit 1
  fi
else
  echo "[ENV] Using active virtual environment: $VIRTUAL_ENV"
fi

python "$SCRIPT_DIR/ingest_chapters.py" "$@"
