#!/bin/bash

set -euo pipefail

if ! command -v uv &> /dev/null
then
    pip install uv
fi

uv venv

source .venv/bin/activate

uv pip install .

if ! command -v ollama &> /dev/null
then
    curl -fsSL https://ollama.com/install.sh | sh
fi