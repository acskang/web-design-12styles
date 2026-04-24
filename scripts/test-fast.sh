#!/usr/bin/env bash
set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR" || exit 1

has_tests() {
    find . \
        -path './.git' -prune -o \
        -path './.venv' -prune -o \
        -type d -name tests -print -quit | grep -q .
}

has_test_files() {
    find . \
        -path './.git' -prune -o \
        -path './.venv' -prune -o \
        -type f \( -name 'test*.py' -o -name '*_test.py' \) -print -quit | grep -q .
}

if ! command -v pytest >/dev/null 2>&1; then
    echo "pytest is not installed in the current environment."
    exit 0
fi

if ! has_tests && ! has_test_files; then
    echo "No test suite was found. Nothing to run."
    exit 0
fi

if [[ $# -gt 0 ]]; then
    pytest -q "$@"
else
    pytest -q
fi
