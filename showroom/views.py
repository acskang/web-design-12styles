from urllib.parse import quote, urlparse

from django.http import Http404
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .data import STYLE_DATA, STYLE_LOOKUP

SITE_PREVIEW_THEMES = {
    "minimalism": [
        ("#f8f4ef", "#111111"),
        ("#ece5da", "#5f5648"),
        ("#ffffff", "#cfc4b4"),
    ],
    "neo-brutalism": [
        ("#ffe352", "#111111"),
        ("#ff6f6f", "#111111"),
        ("#4e8cff", "#ffffff"),
    ],
    "glassmorphism": [
        ("#f08cc6", "#ffffff"),
        ("#8ea7ff", "#ffffff"),
        ("#78f0d0", "#15353a"),
    ],
    "neumorphism": [
        ("#e6ebf3", "#77839a"),
        ("#f6faff", "#b5c0cf"),
        ("#d4dce8", "#677285"),
    ],
    "swiss-typographic": [
        ("#f1ede7", "#111111"),
        ("#ff6247", "#111111"),
        ("#d7d1c8", "#111111"),
    ],
    "playful-illustration": [
        ("#ff926e", "#111111"),
        ("#8fe0ff", "#111111"),
        ("#8de0b4", "#111111"),
    ],
    "dark-tech-saas": [
        ("#0b1020", "#7af8ff"),
        ("#121a31", "#ffffff"),
        ("#162140", "#77ff9b"),
    ],
    "gradient-aurora": [
        ("#ff807d", "#ffffff"),
        ("#7c7cff", "#ffffff"),
        ("#5ffff0", "#11353b"),
    ],
    "bento-ui": [
        ("#dce7ff", "#21366d"),
        ("#dff7e7", "#21583b"),
        ("#fff0ce", "#62481d"),
    ],
    "editorial-magazine": [
        ("#cab6a3", "#111111"),
        ("#f2ede6", "#3f352b"),
        ("#111111", "#ffffff"),
    ],
    "retro-y2k": [
        ("#8de4ff", "#11243b"),
        ("#f1a8ff", "#41204a"),
        ("#fff5a7", "#50461a"),
    ],
    "material-system-ui": [
        ("#dce7ff", "#23407e"),
        ("#ffffff", "#1c2330"),
        ("#eef3f8", "#708096"),
    ],
}

SITE_CONFIDENCE_LABELS = {
    "minimalism": [("strict", _("Strict")), ("strict", _("Strict")), ("hybrid", _("Hybrid"))],
    "neo-brutalism": [("strict", _("Strict")), ("hybrid", _("Hybrid")), ("adjacent", _("Adjacent"))],
    "glassmorphism": [("strict", _("Strict")), ("strict", _("Strict")), ("strict", _("Strict"))],
    "neumorphism": [("strict", _("Strict")), ("strict", _("Strict")), ("adjacent", _("Adjacent"))],
    "swiss-typographic": [("strict", _("Strict")), ("strict", _("Strict")), ("hybrid", _("Hybrid"))],
    "playful-illustration": [("strict", _("Strict")), ("strict", _("Strict")), ("strict", _("Strict"))],
    "dark-tech-saas": [("strict", _("Strict")), ("strict", _("Strict")), ("strict", _("Strict"))],
    "gradient-aurora": [("strict", _("Strict")), ("strict", _("Strict")), ("strict", _("Strict"))],
    "bento-ui": [("strict", _("Strict")), ("strict", _("Strict")), ("strict", _("Strict"))],
    "editorial-magazine": [("strict", _("Strict")), ("strict", _("Strict")), ("hybrid", _("Hybrid"))],
    "retro-y2k": [("strict", _("Strict")), ("hybrid", _("Hybrid")), ("strict", _("Strict"))],
    "material-system-ui": [("strict", _("Strict")), ("strict", _("Strict")), ("strict", _("Strict"))],
}


def _build_representative_sites(style):
    palette = SITE_PREVIEW_THEMES.get(style["slug"], [("#f3f3f3", "#111111")])
    confidence_labels = SITE_CONFIDENCE_LABELS.get(style["slug"], [])
    enriched_sites = []

    for index, site in enumerate(style.get("representative_sites", [])):
        parsed = urlparse(site["url"])
        domain = parsed.netloc.removeprefix("www.")
        initials = "".join(word[0] for word in site["name"].split()[:2]).upper()
        preview_background, preview_ink = palette[index % len(palette)]
        confidence_key, confidence_label = (
            confidence_labels[index]
            if index < len(confidence_labels)
            else ("hybrid", _("Hybrid"))
        )
        enriched_sites.append(
            {
                **site,
                "domain": domain,
                "initials": initials,
                "rank_label": _("Top pick") if index == 0 else _("Reference"),
                "confidence_key": confidence_key,
                "confidence_label": confidence_label,
                "preview_background": preview_background,
                "preview_ink": preview_ink,
                "screenshot_url": f"https://image.thum.io/get/width/1200/crop/760/{quote(site['url'], safe=':/')}",
            }
        )

    return enriched_sites


def home(request):
    styles = []
    for style in STYLE_DATA:
        sites = _build_representative_sites(style)
        styles.append(
            {
                **style,
                "representative_sites": sites,
                "top_site": sites[0] if sites else None,
                "site_domains": [site["domain"] for site in sites],
            }
        )

    return render(
        request,
        "showroom/home.html",
        {
            "styles": styles,
            "style_count": len(styles),
        },
    )


def detail(request, slug):
    style = STYLE_LOOKUP.get(slug)
    if style is None:
        raise Http404("Style not found.")

    style = {
        **style,
        "representative_sites": _build_representative_sites(style),
    }

    current_index = next(
        index for index, item in enumerate(STYLE_DATA) if item["slug"] == slug
    )
    previous_style = STYLE_DATA[current_index - 1] if current_index > 0 else None
    next_style = (
        STYLE_DATA[current_index + 1]
        if current_index < len(STYLE_DATA) - 1
        else None
    )

    return render(
        request,
        "showroom/detail.html",
        {
            "style": style,
            "previous_style": previous_style,
            "next_style": next_style,
        },
    )
