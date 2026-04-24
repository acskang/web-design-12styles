#!/usr/bin/env bash
set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR" || exit 1

run_step() {
    local label="$1"
    shift
    echo "==> $label"
    "$@"
}

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

echo "Repository: $ROOT_DIR"

if [[ -f manage.py ]]; then
    if command -v python3 >/dev/null 2>&1; then
        run_step "python3 manage.py check" python3 manage.py check || exit 1
    else
        echo "skip: python3 not found"
    fi
else
    echo "skip: manage.py not found"
fi

if command -v pytest >/dev/null 2>&1; then
    if has_tests || has_test_files; then
        run_step "pytest -q" pytest -q || exit 1
    else
        echo "skip: no tests directory or test files found"
    fi
else
    echo "skip: pytest not found"
fi

if command -v ruff >/dev/null 2>&1; then
    echo "==> ruff check ."
    ruff check . || exit 1
else
    echo "skip: ruff not found"
fi

echo "verify complete"
