#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$DIR/../src/solucao.py"

status=0
for in_file in "$DIR"/*.in; do
    base="$(basename "$in_file" .in)"
    out_file="$DIR/$base.out"
    if [[ ! -f "$out_file" ]]; then
        echo "SKIP $base (sem .out)"
        continue
    fi
    actual="$(python3 "$SRC" < "$in_file")"
    expected="$(cat "$out_file")"
    if [[ "$actual" == "$expected" ]]; then
        echo "OK   $base"
    else
        echo "FAIL $base"
        echo "  esperado: $expected"
        echo "  obtido:   $actual"
        status=1
    fi
done

exit $status
