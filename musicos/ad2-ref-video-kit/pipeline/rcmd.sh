#!/bin/bash
S="$(cd "$(dirname "$0")" && pwd)"
rm -f "$S/done.txt"; echo "$@" > "$S/cmd.txt"
for i in $(seq 1 ${RCMD_TIMEOUT:-120}); do [ -f "$S/done.txt" ] && { cat "$S/done.txt"; echo; exit 0; }; sleep 1; done
echo "TIMEOUT waiting for: $@"; exit 1
