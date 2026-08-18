#!/usr/bin/env bash
set -euo pipefail
cd /home/ubuntu/ecofarm_knowledge_html
exec python3 -m http.server "${ECOFARM_KB_PORT:-8090}" --bind 0.0.0.0
