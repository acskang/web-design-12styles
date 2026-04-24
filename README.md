# web-design-12styles

A Django showroom project for browsing 12 web design styles with English and Korean language support.

## Overview

- Gallery home page that lists 12 design styles
- Detail page for each style with visual cues, recipe, and representative sites
- Language switching through Django i18n

## Tech Stack

- Python
- Django
- SQLite by default
- Static assets served from `static/`

## Local Run

Activate your virtual environment first if needed, then run:

```bash
python3 manage.py check
python3 manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Project Structure

- `design12/`: Django settings and root URL configuration
- `showroom/`: app views, routes, and style data
- `templates/showroom/`: shared layout and page templates
- `static/`: source CSS, JS, and images
- `locale/`: Korean translation files
- `docs/`: architecture, testing, and runbook notes

## Verification

Useful project commands:

```bash
python3 manage.py check
pytest -q
scripts/test-fast.sh
scripts/verify.sh
```

## Repository

GitHub: <https://github.com/acskang/web-design-12styles>
