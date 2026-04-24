#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-/home/cskang/miniconda3/envs/dj5/bin/python}"
ENV_FILE="${ENV_FILE:-/etc/webdesign/webdesign.env}"

cd "$ROOT_DIR"

if [[ -f "$ENV_FILE" ]]; then
    set -a
    # shellcheck disable=SC1090
    source "$ENV_FILE"
    set +a
fi

"$PYTHON_BIN" manage.py check
"$PYTHON_BIN" manage.py compilemessages
"$PYTHON_BIN" manage.py collectstatic --noinput

sudo install -d -m 755 /etc/webdesign
if [[ ! -f /etc/webdesign/webdesign.env ]]; then
    sudo install -o root -g cskang -m 640 deploy/webdesign.env.example /etc/webdesign/webdesign.env
fi

sudo install -m 644 deploy/gunicorn_webdesign.service /etc/systemd/system/gunicorn_webdesign.service
sudo install -m 644 deploy/gunicorn_webdesign.socket /etc/systemd/system/gunicorn_webdesign.socket
sudo install -m 644 deploy/nginx_webdesign.conf /etc/nginx/sites-available/webdesign
sudo ln -snf /etc/nginx/sites-available/webdesign /etc/nginx/sites-enabled/webdesign

sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn_webdesign.socket
sudo systemctl restart gunicorn_webdesign.service
sudo nginx -t
sudo systemctl reload nginx

echo "Redeploy completed for webdesign.thesysm.com"
