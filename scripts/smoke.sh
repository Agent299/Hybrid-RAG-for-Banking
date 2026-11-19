#!/bin/sh
set -eu
base_url=${API_BASE_URL:-http://127.0.0.1:8000}
curl --fail --silent --show-error --max-time 10 "${base_url%/}/health/live"
printf "\n"
