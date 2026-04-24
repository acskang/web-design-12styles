# WebDesignStyle12 Agents Guide

## Purpose
This repository is a Django showroom project for browsing 12 web design styles.

The core app is `showroom`.
It renders:
- the gallery home page
- per-style detail pages
- language switching for English and Korean

Project-specific guidance in this file should be used together with:
- `~/.codex/AGENTS.md`
- `~/.codex/docs/workflow.md`
- `~/.codex/docs/django.md`
- `~/.codex/docs/verification.md`
- `~/.codex/docs/reporting.md`

## Read First
1. `docs/architecture.md`
2. `docs/testing.md`
3. `docs/runbook.md`

## Project Workflow
1. Scan `design12/settings.py`, `design12/urls.py`, `showroom/urls.py`, `showroom/views.py`, `showroom/data.py`, and `templates/showroom/`.
2. Keep changes narrow and centered on the requested surface.
3. Prefer the smallest useful verification first.
4. Use `scripts/verify.sh` for broader verification when appropriate.
5. If work touches one style entry, inspect the matching gallery/detail rendering path as well.

## Do Not
Unless explicitly requested:
- do not rewrite the project structure
- do not add packages
- do not create migrations casually
- do not make broad settings changes
- do not bulk-edit `showroom/data.py` unless the task truly requires it
- do not assume tests exist; verify what is present first

## Django Rules
- `manage.py` is at the repo root and uses `design12.settings`.
- Root URLs live in `design12/urls.py`.
- Showroom routes live in `showroom/urls.py`.
- Keep view logic light; style data definitions belong in `showroom/data.py`.
- Run `python3 manage.py check` after Django-facing changes when practical.

## Template Rules
- Shared layout is in `templates/showroom/base.html`.
- Home and detail pages extend the base template.
- Preserve `{% load static i18n %}` and the existing block structure unless the task requires change.
- Keep URL names stable: `showroom:home` and `showroom:detail`.
- Preserve static asset paths under `static/`.

## Data Rules
- `showroom/data.py` is the source of truth for style records.
- When editing a style entry, preserve the fields expected by templates and views.
- Avoid changing multiple style entries unless the request clearly requires batch edits.

## i18n Rules
- English and Korean are enabled in `design12/settings.py`.
- Translation files are under `locale/ko/LC_MESSAGES/`.
- Wrap new user-facing strings with `gettext_lazy`, `{% trans %}`, or `{% blocktrans %}` as appropriate.
- If strings change, note whether `django.po` and compiled messages may need updating.

## Done When
- requested files are updated
- project docs still match the current repo structure
- verification was run and reported clearly
- any unverified assumption is called out explicitly

## Final Response Format
Prefer this structure:

- Summary
- Files changed
- Commands run
- Verification
- Risks / follow-ups
