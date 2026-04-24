# Testing

## Verification Priority For Small Changes
Prefer the smallest useful verification first:

1. the closest relevant check
2. `python3 manage.py check`
3. targeted page verification
4. `scripts/verify.sh` for broader verification

If automated tests are present, use the closest relevant target first.

## Template Changes
- Run `python3 manage.py check`.
- Start the dev server and load `/` and at least one `/styles/<slug>/` page.
- Confirm `{% url %}`, `{% static %}`, and translation tags still render correctly.
- If `templates/showroom/base.html` changed, verify both the gallery and detail pages.

## View Changes
- Run `python3 manage.py check`.
- Exercise `showroom:home` and one or more `showroom:detail` pages.
- Confirm missing slugs still raise 404.
- Confirm previous/next navigation still works on detail pages.

## `data.py` Changes
For edited style entries, verify that required fields still match what the templates and views expect, including:

- `slug`
- `name`
- `subtitle`
- `thumbnail_image`
- `hero_image`
- `keywords`
- `definition`
- `key_visual_cues`
- `good_for`
- `watch_outs`
- `quick_recipe`
- `representative_sites`

Also:
- load the affected detail page
- confirm cards, labels, and representative site links still render
- check translation wrapping on any new user-facing strings

## Django Check Rule
- Use `python3 manage.py check` as the minimum validation for Django-facing work.
- If `manage.py` is missing, treat Django checks as unavailable instead of guessing another entrypoint.

## Automated Test Rule
- If pytest or another test runner is present, use the closest relevant test target first.
- If no automated tests exist for the affected area, do not overstate confidence.
- Use `scripts/test-fast.sh` when available for targeted execution.

## When There Are No Tests
If automated tests are absent, use the best available fallback verification:
- `python3 manage.py check`
- targeted page loads
- template rendering inspection
- static path inspection
- i18n behavior checks where relevant

## i18n Checks
- Verify new strings are wrapped for translation in Python or templates.
- If translatable strings changed, update `locale/ko/LC_MESSAGES/django.po` when needed.
- Recompile messages if the workflow or deployment requires updated `.mo` files.
- Confirm EN/KO switching still returns the user to a sensible page.

## Reporting
When finishing work, report:
- commands run
- pass/fail or partial verification status
- what remains unverified
