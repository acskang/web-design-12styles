# Runbook

## Local Run
This repository appears to be a plain Django project driven by `manage.py`.

If you use a local virtualenv, activate it first.
Otherwise run commands with the Python environment that already has Django installed.

If the repository later adopts `uv`, `poetry`, `pipenv`, or another runner, prefer that project-local standard.

## Dev Server
```bash
python3 manage.py runserver
```

## Common Commands
```bash
python3 manage.py check
python3 manage.py runserver
pytest -q
scripts/verify.sh
scripts/test-fast.sh
```

## Templates, Static, Env
- Shared templates live under `templates/showroom/`.
- Source static assets live under `static/`.
- Collected static output is currently in `staticfiles/`.
- Example deploy environment file: `deploy/webdesign.env.example`.

## Environment Notes
Settings read environment variables such as:
- `DJANGO_DEBUG`
- `DJANGO_SECRET_KEY`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DJANGO_SQLITE_PATH`

## i18n Commands
```bash
python3 manage.py makemessages -l ko
python3 manage.py compilemessages
```

## Project Notes
- Root settings module: `design12.settings`
- Root URLs: `design12/urls.py`
- Showroom routes: `showroom/urls.py`
- Database defaults to SQLite at `db.sqlite3` unless `DJANGO_SQLITE_PATH` overrides it
