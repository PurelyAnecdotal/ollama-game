#!/bin/bash

set -euo pipefail

ollama serve &

ollama pull llama3.2:1b