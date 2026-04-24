# Architecture

## User Flow
- `/` renders the style gallery.
- `/styles/<slug>/` renders the selected style's explanation, cues, recipe, and reference sites.
- The language switcher posts to Django's `set_language` flow under `/i18n/`.

## Main Pieces
- `showroom/data.py`: source of truth for the 12 style records, translated labels, and representative site metadata.
- `showroom/views.py`: prepares gallery/detail context and enriches representative site data for rendering.
- `templates/showroom/home.html`: renders gallery cards from the `styles` context.
- `templates/showroom/detail.html`: renders a single style plus previous/next navigation.
- `templates/showroom/base.html`: shared shell, fonts, static assets, footer, and language switcher.

## Page Relationship
- `home()` iterates over `STYLE_DATA` and derives display helpers such as `top_site` and `site_domains`.
- Each gallery card links to `detail()` by slug.
- `detail()` reads the same style source through `STYLE_LOOKUP`, then computes previous/next items from `STYLE_DATA`.

## Wiring
- `manage.py` bootstraps Django with `design12.settings`.
- `design12/settings.py` defines installed apps, templates, locale settings, and static configuration.
- `design12/urls.py` mounts Django i18n URLs and includes `showroom.urls`.
- `showroom/urls.py` maps the gallery and detail routes to `showroom.views`.
- Templates render context built in `showroom/views.py`, which reads from `showroom/data.py`.

## i18n Structure
- Default language is `en`.
- Enabled languages are `en` and `ko`.
- `LocaleMiddleware` is enabled.
- Locale files live under `locale/ko/LC_MESSAGES/`.
- Python strings use `gettext_lazy`; templates use `{% trans %}` and `{% blocktrans %}`.
