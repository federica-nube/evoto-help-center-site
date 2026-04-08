#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from html import escape, unescape
from pathlib import Path, PurePosixPath
from textwrap import dedent
from typing import Any
from urllib.parse import quote, urlsplit, urlunsplit

try:
    import markdown as markdown_lib
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "The Python 'markdown' package is required to build the Evoto help center."
    ) from exc


from normalize_spaces_markdown import normalize_markdown

ROOT = Path(__file__).resolve().parents[1]
SPACES_DIR = (ROOT / os.environ.get("HELP_CENTER_SPACES_DIR", "spaces")).resolve()
OUTPUT_DIR = ROOT / "help-center-dist"
STATIC_DIR = OUTPUT_DIR / "static"
SITE_NAME = "Evoto Learning Center"
SITE_SHORT_NAME = "Evoto"
SITE_SECTION_LABEL = "Learning Center"
OFFICIAL_SITE_URL = "https://www.evoto.ai/"
OFFICIAL_DOWNLOAD_URL = "https://www.evoto.ai/download"
OFFICIAL_PRICING_URL = "https://www.evoto.ai/payment"
OFFICIAL_BLOG_URL = "https://blog.evoto.ai/"
OFFICIAL_WEBINAR_URL = "https://www.evoto.ai/webinar"
OFFICIAL_FORUM_URL = "https://forum.evoto.ai/"
OFFICIAL_HELP_URL = "https://www.evoto.ai/help"
OFFICIAL_SUPPORT_ARTICLE_URL = "https://support.evoto.ai/understanding-evoto-credits-and-pricing/"
OFFICIAL_SIGNIN_URL = "https://www.evoto.ai/login"
OFFICIAL_PRODUCT_DESKTOP_URL = "https://www.evoto.ai/ai-photo-editor"
OFFICIAL_PRODUCT_IPAD_URL = "https://www.evoto.ai/ipad"
OFFICIAL_PRODUCT_MOBILE_URL = "https://www.evoto.ai/evoto-mobile"
OFFICIAL_PRODUCT_INSTANT_URL = "https://instant.evoto.ai/"
OFFICIAL_PRODUCT_VIDEO_URL = "https://video.evoto.ai/"
OFFICIAL_VIDEO_URL = OFFICIAL_PRODUCT_VIDEO_URL
OFFICIAL_TERMS_URL = "https://res.evoto.ai/ui/www/policy/terms.html"
OFFICIAL_PRIVACY_URL = "https://res.evoto.ai/ui/www/policy/privacy.html"
OFFICIAL_COOKIE_URL = "https://res.evoto.ai/ui/www/policy/cookies.html"
OFFICIAL_LOGO_SVG = "https://res.evoto.ai/ui/www/images/pages/common/evoto-logo.svg"
OFFICIAL_OG_IMAGE = "https://res.evoto.ai/ui/www/images/pages/newHome/twitter_image.png"
OFFICIAL_TRUSTPILOT_IMAGE = "https://res.evoto.ai/ui/www/images/pages/newHome/footer-trustpilot.png"
OFFICIAL_CONTACT_EMAIL = "contactus@evoto.ai"
OFFICIAL_LEGAL_NAME = "TRUESIGHT TECHNOLOGY INC."
OFFICIAL_ADDRESS = "149 Commonwealth Drive, Suite 1049 Menlo Park, CA 94025, USA"
DEFAULT_SEO_DESCRIPTION = (
    "Official Evoto support hub for setup guides, product tutorials, pricing answers, "
    "workflow troubleshooting, and help across Evoto Desktop, Mobile, iPad, and Instant."
)
SOCIAL_LINKS = [
    ("Instagram", "https://www.instagram.com/evotoai/"),
    ("Facebook", "https://www.facebook.com/evotoai"),
    ("YouTube", "https://www.youtube.com/channel/UC7uxVJnyLLxjfAKRtmDk8Kg"),
    ("Reddit", "https://www.reddit.com/r/EvotoAI/"),
    ("TikTok", "https://www.tiktok.com/@evotoaitk?lang=en"),
    ("LinkedIn", "https://www.linkedin.com/company/evoto-ai/posts/?feedView=all"),
]


def normalize_base_path(value: str) -> str:
    cleaned = value.strip().strip("/")
    return f"/{cleaned}" if cleaned else ""


BASE_PATH = normalize_base_path(os.environ.get("HELP_CENTER_BASE_PATH", ""))
SITE_ORIGIN = (
    os.environ.get("HELP_CENTER_SITE_ORIGIN", "").rstrip("/")
    or {
        "/evoto-help-center-site": "https://federica-nube.github.io",
    }.get(BASE_PATH, "")
)

LANGUAGE_LABELS = {
    "en": "English",
    "es": "Español",
    "ja": "日本語",
    "ko": "한국어",
    "pt-br": "Português (Brasil)",
    "vi": "Tiếng Việt",
    "zh-hant": "繁體中文",
}

LANGUAGE_ORDER = ["en", "es", "ja", "ko", "pt-br", "vi", "zh-hant"]

NAV_LINE_RE = re.compile(r"^(?P<indent>\s*)\*\s+\[(?P<title>.+?)\]\((?P<target>[^)]+)\)\s*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
HEADING_RE = re.compile(r"<h([1-6]) id=\"([^\"]+)\">(.*?)</h\1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"\s+")


@dataclass
class NavItem:
    title: str
    source_path: str
    children: list["NavItem"] = field(default_factory=list)
    parent: "NavItem | None" = None


@dataclass
class Page:
    lang: str
    source_path: str
    source_file: Path
    url: str
    output_path: Path
    title: str
    nav_title: str
    meta: dict[str, Any]
    markdown_body: str
    html_body: str = ""
    plain_text: str = ""
    excerpt: str = ""
    headings: list[dict[str, Any]] = field(default_factory=list)
    nav_item: NavItem | None = None
    breadcrumbs: list[NavItem] = field(default_factory=list)
    children: list[NavItem] = field(default_factory=list)
    previous_page: "Page | None" = None
    next_page: "Page | None" = None
    translation_links: dict[str, str] = field(default_factory=dict)


def site_url(path: str) -> str:
    path = path or "/"
    normalized = "/" if path == "/" else f"/{path.lstrip('/')}"
    if BASE_PATH and (normalized == BASE_PATH or normalized.startswith(f"{BASE_PATH}/")):
        return normalized
    return f"{BASE_PATH}{normalized}" if BASE_PATH else normalized


def absolute_site_url(path: str) -> str:
    resolved = path if path.startswith("http://") or path.startswith("https://") else site_url(path)
    return f"{SITE_ORIGIN}{resolved}" if SITE_ORIGIN and resolved.startswith("/") else resolved


def main() -> None:
    build_site()


def build_site() -> None:
    languages = discover_languages()
    if not languages:
        raise SystemExit("No languages found under spaces/.")

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    STATIC_DIR.mkdir(parents=True, exist_ok=True)

    nav_by_lang: dict[str, list[NavItem]] = {}
    nav_index_by_lang: dict[str, dict[str, NavItem]] = {}
    nav_order_by_lang: dict[str, list[str]] = {}
    pages_by_lang: dict[str, dict[str, Page]] = {}
    language_home_urls: dict[str, str] = {}
    translation_groups: dict[str, dict[str, Page]] = defaultdict(dict)

    for lang in languages:
        nav_items = parse_summary(lang)
        nav_index: dict[str, NavItem] = {}
        nav_order: list[str] = []
        index_navigation(nav_items, nav_index, nav_order)
        pages = load_pages(lang, nav_index)

        nav_by_lang[lang] = nav_items
        nav_index_by_lang[lang] = nav_index
        nav_order_by_lang[lang] = nav_order
        pages_by_lang[lang] = pages
        language_home_urls[lang] = pages.get("README.md", next(iter(pages.values()))).url

        for page in pages.values():
            translation_group = str(page.meta.get("translation_group", "")).strip()
            if translation_group:
                translation_groups[translation_group][lang] = page

    page_url_lookup = {
        lang: {page.source_path: page.url for page in pages.values()}
        for lang, pages in pages_by_lang.items()
    }

    for lang in languages:
        enrich_pages(
            lang=lang,
            pages=pages_by_lang[lang],
            nav_index=nav_index_by_lang[lang],
            nav_order=nav_order_by_lang[lang],
            page_url_lookup=page_url_lookup,
            translation_groups=translation_groups,
            language_home_urls=language_home_urls,
        )

    write_shared_assets()
    write_search_index(pages_by_lang, nav_index_by_lang)
    write_language_pages(languages, pages_by_lang, nav_by_lang, language_home_urls)
    write_root_pages(languages, pages_by_lang, nav_by_lang, language_home_urls)

    total_pages = sum(len(pages) for pages in pages_by_lang.values())
    print(f"Built {total_pages} pages across {len(languages)} languages into {OUTPUT_DIR}")


def discover_languages() -> list[str]:
    found = [path.name for path in SPACES_DIR.iterdir() if path.is_dir()]
    ordered = [lang for lang in LANGUAGE_ORDER if lang in found]
    ordered.extend(sorted(lang for lang in found if lang not in ordered))
    return ordered


def parse_summary(lang: str) -> list[NavItem]:
    summary_path = SPACES_DIR / lang / "SUMMARY.md"
    if not summary_path.exists():
        return []

    roots: list[NavItem] = []
    stack: list[NavItem] = []

    for line in summary_path.read_text(encoding="utf-8").splitlines():
        match = NAV_LINE_RE.match(line)
        if not match:
            continue

        indent = len(match.group("indent").replace("\t", "    "))
        level = indent // 4
        item = NavItem(
            title=clean_text(match.group("title")),
            source_path=normalize_source_path(match.group("target")),
        )

        while len(stack) > level:
            stack.pop()

        if stack:
            item.parent = stack[-1]
            stack[-1].children.append(item)
        else:
            roots.append(item)

        stack.append(item)

    return roots


def index_navigation(items: list[NavItem], index: dict[str, NavItem], order: list[str]) -> None:
    for item in items:
        index[item.source_path] = item
        order.append(item.source_path)
        index_navigation(item.children, index, order)


def load_pages(lang: str, nav_index: dict[str, NavItem]) -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for source_file in sorted((SPACES_DIR / lang).rglob("*.md")):
        if source_file.name == "SUMMARY.md":
            continue

        source_path = source_file.relative_to(SPACES_DIR / lang).as_posix()
        raw_markdown = source_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(normalize_markdown(raw_markdown, source_path))
        nav_item = nav_index.get(source_path)
        title = (
            str(meta.get("title", "")).strip()
            or (nav_item.title if nav_item else "")
            or extract_first_heading(body)
            or source_file.stem.replace("-", " ").replace("_", " ").title()
        )
        url = build_page_url(lang, source_path)
        output_path = build_output_path(lang, source_path)

        pages[source_path] = Page(
            lang=lang,
            source_path=source_path,
            source_file=source_file,
            url=url,
            output_path=output_path,
            title=clean_text(title),
            nav_title=nav_item.title if nav_item else clean_text(title),
            meta=meta,
            markdown_body=body.strip(),
        )

    return pages


def enrich_pages(
    *,
    lang: str,
    pages: dict[str, Page],
    nav_index: dict[str, NavItem],
    nav_order: list[str],
    page_url_lookup: dict[str, dict[str, str]],
    translation_groups: dict[str, dict[str, Page]],
    language_home_urls: dict[str, str],
) -> None:
    ordered_paths = [source_path for source_path in nav_order if source_path in pages]
    unordered_paths = sorted(source_path for source_path in pages if source_path not in nav_order)
    full_order = ordered_paths + unordered_paths

    for index, source_path in enumerate(full_order):
        page = pages[source_path]
        page.nav_item = nav_index.get(source_path)
        page.breadcrumbs = breadcrumb_items(page.nav_item)
        page.children = page.nav_item.children if page.nav_item else []
        if index > 0:
            page.previous_page = pages[full_order[index - 1]]
        if index + 1 < len(full_order):
            page.next_page = pages[full_order[index + 1]]

        translation_group = str(page.meta.get("translation_group", "")).strip()
        if translation_group and translation_group in translation_groups:
            page.translation_links = {
                language: translation_groups[translation_group].get(language, None).url
                if translation_groups[translation_group].get(language)
                else language_home_urls[language]
                for language in page_url_lookup
            }
        else:
            page.translation_links = fallback_translation_links(
                page=page,
                page_url_lookup=page_url_lookup,
                language_home_urls=language_home_urls,
            )

        html_body, headings = render_markdown(
            page=page,
            page_url_lookup=page_url_lookup,
        )
        page.html_body = html_body
        page.headings = headings
        page.plain_text = html_to_text(html_body)
        page.excerpt = build_excerpt(remove_title_prefix(page.plain_text, page.title))


def breadcrumb_items(nav_item: NavItem | None) -> list[NavItem]:
    items: list[NavItem] = []
    current = nav_item
    while current is not None:
        items.append(current)
        current = current.parent
    return list(reversed(items))


def fallback_translation_links(
    *,
    page: Page,
    page_url_lookup: dict[str, dict[str, str]],
    language_home_urls: dict[str, str],
) -> dict[str, str]:
    links: dict[str, str] = {}
    for language, lookup in page_url_lookup.items():
        links[language] = lookup.get(page.source_path, language_home_urls[language])
    return links


def render_markdown(
    *,
    page: Page,
    page_url_lookup: dict[str, dict[str, str]],
) -> tuple[str, list[dict[str, Any]]]:
    renderer = markdown_lib.Markdown(
        extensions=[
            "extra",
            "fenced_code",
            "tables",
            "sane_lists",
            "toc",
        ],
        extension_configs={
            "toc": {"permalink": False},
        },
    )
    html_body = renderer.convert(page.markdown_body)
    html_body = normalize_html_block(html_body)
    html_body = rewrite_links_and_images(
        html_body=html_body,
        current_source_path=page.source_path,
        lang=page.lang,
        page_url_lookup=page_url_lookup,
    )
    html_body = stylize_tables(html_body)
    html_body = add_heading_anchors(html_body)
    headings = extract_headings(html_body)
    return html_body, headings


def normalize_html_block(html_body: str) -> str:
    replacements = {
        "<h7>": '<span class="micro-heading">',
        "</h7>": "</span>",
        "<h8>": '<span class="micro-heading">',
        "</h8>": "</span>",
    }
    for original, replacement in replacements.items():
        html_body = html_body.replace(original, replacement)
    return html_body


def rewrite_links_and_images(
    *,
    html_body: str,
    current_source_path: str,
    lang: str,
    page_url_lookup: dict[str, dict[str, str]],
) -> str:
    def replace_anchor(match: re.Match[str]) -> str:
        prefix, href, suffix = match.groups()
        resolved = resolve_href(
            href=href,
            current_source_path=current_source_path,
            lang=lang,
            page_url_lookup=page_url_lookup,
        )
        attrs = suffix
        if href.startswith("http://") or href.startswith("https://"):
            attrs = attrs[:-1] + ' target="_blank" rel="noreferrer">' if attrs.endswith(">") else attrs
        return f'{prefix}{escape(resolved, quote=True)}{attrs}'

    def replace_image(match: re.Match[str]) -> str:
        prefix, src, suffix = match.groups()
        resolved = resolve_href(
            href=src,
            current_source_path=current_source_path,
            lang=lang,
            page_url_lookup=page_url_lookup,
        )
        attrs = suffix
        if 'loading="' not in attrs:
            if attrs.endswith("/>"):
                attrs = attrs[:-2] + ' loading="lazy" />'
            elif attrs.endswith(">"):
                attrs = attrs[:-1] + ' loading="lazy">'
        return f'{prefix}{escape(resolved, quote=True)}{attrs}'

    html_body = re.sub(r'(<a\s+[^>]*href=")([^"]+)(".*?>)', replace_anchor, html_body)
    html_body = re.sub(r'(<img\s+[^>]*src=")([^"]+)(".*?>)', replace_image, html_body)
    return html_body


def stylize_tables(html_body: str) -> str:
    html_body = html_body.replace("<table>", '<div class="table-wrap"><table>')
    html_body = html_body.replace("</table>", "</table></div>")
    return html_body


def add_heading_anchors(html_body: str) -> str:
    def replace(match: re.Match[str]) -> str:
        level, heading_id, inner_html = match.groups()
        anchor = (
            f'<a class="heading-anchor" href="#{heading_id}" aria-label="Link to this section">#</a>'
        )
        return f'<h{level} id="{heading_id}">{inner_html}{anchor}</h{level}>'

    return HEADING_RE.sub(replace, html_body)


def extract_headings(html_body: str) -> list[dict[str, Any]]:
    headings: list[dict[str, Any]] = []
    for level, heading_id, inner_html in HEADING_RE.findall(html_body):
        title = clean_text(html_to_text(inner_html))
        if not title:
            continue
        headings.append(
            {
                "level": int(level),
                "id": heading_id,
                "title": title,
            }
        )
    return headings


def resolve_href(
    *,
    href: str,
    current_source_path: str,
    lang: str,
    page_url_lookup: dict[str, dict[str, str]],
) -> str:
    href = href.strip()
    if not href:
        return href
    if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
        return href

    split = urlsplit(href)
    if split.scheme or href.startswith("//"):
        return href
    suffix = urlunsplit(("", "", "", split.query, split.fragment))

    if split.path.endswith(".md"):
        candidates = []
        if split.path.startswith(".") or split.path.startswith(".."):
            candidates.append(normalize_source_path(str(PurePosixPath(current_source_path).parent / split.path)))
        else:
            candidates.append(normalize_source_path(split.path))
            candidates.append(normalize_source_path(str(PurePosixPath(current_source_path).parent / split.path)))
        for candidate in unique(candidates):
            target = page_url_lookup[lang].get(candidate)
            if target:
                return f"{target}{suffix}"

    if split.path.startswith("/"):
        return f"{site_url(split.path)}{suffix}"

    return href


def write_shared_assets() -> None:
    (STATIC_DIR / "site.css").write_text(build_css(), encoding="utf-8")
    (STATIC_DIR / "site.js").write_text(build_javascript(), encoding="utf-8")
    (STATIC_DIR / "favicon.svg").write_text(build_favicon(), encoding="utf-8")


def write_search_index(
    pages_by_lang: dict[str, dict[str, Page]],
    nav_index_by_lang: dict[str, dict[str, NavItem]],
) -> None:
    records: list[dict[str, Any]] = []
    for lang, pages in pages_by_lang.items():
        for page in pages.values():
            nav_item = nav_index_by_lang[lang].get(page.source_path)
            records.append(
                {
                    "title": page.nav_title or page.title,
                    "url": page.url,
                    "excerpt": summarize_page(page),
                    "lang": lang,
                    "langLabel": LANGUAGE_LABELS.get(lang, lang),
                    "section": breadcrumb_label(nav_item),
                }
            )
    (OUTPUT_DIR / "search-index.json").write_text(
        json.dumps(records, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def write_language_pages(
    languages: list[str],
    pages_by_lang: dict[str, dict[str, Page]],
    nav_by_lang: dict[str, list[NavItem]],
    language_home_urls: dict[str, str],
) -> None:
    for lang in languages:
        for page in pages_by_lang[lang].values():
            page.output_path.parent.mkdir(parents=True, exist_ok=True)
            page.output_path.write_text(
                render_doc_page(
                    page=page,
                    nav_items=nav_by_lang[lang],
                    languages=languages,
                    language_home_urls=language_home_urls,
                    pages_by_lang=pages_by_lang,
                ),
                encoding="utf-8",
            )


def write_root_pages(
    languages: list[str],
    pages_by_lang: dict[str, dict[str, Page]],
    nav_by_lang: dict[str, list[NavItem]],
    language_home_urls: dict[str, str],
) -> None:
    english_root = pages_by_lang.get("en", {}).get("README.md")
    feature_cards = [
        {
            "title": "Evoto Desktop",
            "url": site_url("/en/evoto-desktop/"),
            "excerpt": "Experience the full power of Evoto with advanced editing tools and complete workflow control.",
            "badge_icon_key": "desktop",
        },
        {
            "title": "Evoto iPad",
            "url": site_url("/en/evoto-ipad/"),
            "excerpt": "Edit anytime, anywhere with powerful tools designed for on-the-go creativity.",
            "badge_icon_key": "ipad",
        },
        {
            "title": "Evoto Mobile",
            "url": site_url("/en/evoto-mobile/"),
            "excerpt": "AI-powered portrait retouching at your fingertips.",
            "badge_icon_key": "mobile",
        },
        {
            "title": "Evoto Instant",
            "url": site_url("/en/evoto-instant/"),
            "excerpt": "Shoot. Cull. Edit. Proof. Done - in an Instant.",
            "badge_icon_key": "instant",
        },
        {
            "title": "Evoto Video",
            "url": OFFICIAL_VIDEO_URL,
            "excerpt": "Transform your video look in one click, and refine portraits with just a swipe.",
            "badge_icon_key": "video",
        },
        {
            "title": "Account",
            "url": site_url("/en/account-settings/"),
            "excerpt": "Account FAQs, Account Settings & Security, Account Troubleshooting, Account Management",
            "badge_icon_key": "account",
        },
        {
            "title": "Price",
            "url": site_url("/en/price-billing/"),
            "excerpt": "Evoto Credits, Subscription Plans, Pay-as-You-Go Plan, Coupon & Promo Codes FAQs, Pricing FAQs, and more",
            "badge_icon_key": "price",
        },
        {
            "title": "FAQ",
            "url": site_url("/en/faq/"),
            "excerpt": "Installation FAQs, Edit FAQs, Import & Export FAQs, Miscellaneous FAQs, Additional Resources & Support, and more",
            "badge_icon_key": "faq",
        },
        {
            "title": "Tips & Tricks",
            "url": site_url("/en/tips-tricks/"),
            "excerpt": "Editing Workflow, Feature Related, Setting Guides",
            "badge_icon_key": "tips",
        },
    ]

    total_pages = sum(len(pages) for pages in pages_by_lang.values())
    intro = english_root.excerpt if english_root else "Browse every Evoto product guide in one multilingual knowledge base."
    (OUTPUT_DIR / "index.html").write_text(
        render_root_page(
            languages=languages,
            language_home_urls=language_home_urls,
            feature_cards=feature_cards,
            intro=intro,
            total_pages=total_pages,
        ),
        encoding="utf-8",
    )
    search_dir = OUTPUT_DIR / "search"
    search_dir.mkdir(parents=True, exist_ok=True)
    (search_dir / "index.html").write_text(
        render_search_page(languages, language_home_urls),
        encoding="utf-8",
    )
    (OUTPUT_DIR / "404.html").write_text(
        render_not_found_page(languages, language_home_urls),
        encoding="utf-8",
    )


def render_head_meta(
    *,
    title: str,
    description: str,
    url: str,
    page_type: str,
    noindex: bool = False,
) -> str:
    canonical_url = absolute_site_url(url)
    robots = "noindex,nofollow" if noindex else "index,follow,max-image-preview:large"
    schema_payload = build_schema_payload(
        title=title,
        description=description,
        canonical_url=canonical_url,
        page_type=page_type,
    )
    return dedent(
        f"""\
        <title>{escape(title)}</title>
        <meta name="description" content="{escape(description)}" />
        <meta name="application-name" content="{SITE_NAME}" />
        <meta name="robots" content="{robots}" />
        <meta name="theme-color" content="#141414" />
        <link rel="canonical" href="{escape(canonical_url)}" />
        <meta property="og:site_name" content="{SITE_SHORT_NAME}" />
        <meta property="og:type" content="{page_type}" />
        <meta property="og:title" content="{escape(title)}" />
        <meta property="og:description" content="{escape(description)}" />
        <meta property="og:url" content="{escape(canonical_url)}" />
        <meta property="og:image" content="{OFFICIAL_OG_IMAGE}" />
        <meta property="og:image:alt" content="Evoto official brand image" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="{escape(title)}" />
        <meta name="twitter:description" content="{escape(description)}" />
        <meta name="twitter:image" content="{OFFICIAL_OG_IMAGE}" />
        <script type="application/ld+json">{json.dumps(schema_payload, ensure_ascii=False, separators=(",", ":"))}</script>
        """
    )


def build_schema_payload(
    *,
    title: str,
    description: str,
    canonical_url: str,
    page_type: str,
) -> list[dict[str, Any]]:
    website_schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": absolute_site_url("/"),
        "description": DEFAULT_SEO_DESCRIPTION,
        "publisher": {"@id": absolute_site_url("/#/schema/organization")},
    }
    if SITE_ORIGIN:
        website_schema["potentialAction"] = {
            "@type": "SearchAction",
            "target": f"{absolute_site_url('/search/')}?q={{search_term_string}}",
            "query-input": "required name=search_term_string",
        }

    organization_schema = {
        "@context": "https://schema.org",
        "@id": absolute_site_url("/#/schema/organization"),
        "@type": "Organization",
        "name": SITE_SHORT_NAME,
        "legalName": OFFICIAL_LEGAL_NAME,
        "url": OFFICIAL_SITE_URL,
        "logo": OFFICIAL_LOGO_SVG,
        "image": OFFICIAL_OG_IMAGE,
        "email": OFFICIAL_CONTACT_EMAIL,
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "Customer Service",
            "email": OFFICIAL_CONTACT_EMAIL,
        },
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "149 Commonwealth Drive, Suite 1049",
            "addressLocality": "Menlo Park",
            "addressRegion": "CA",
            "postalCode": "94025",
            "addressCountry": "US",
        },
        "sameAs": [url for _, url in SOCIAL_LINKS],
    }

    page_schema = {
        "@context": "https://schema.org",
        "@type": "Article" if page_type == "article" else "WebPage",
        "name": title,
        "headline": title,
        "description": description,
        "url": canonical_url,
        "isPartOf": {"@id": absolute_site_url("/")},
        "publisher": {"@id": absolute_site_url("/#/schema/organization")},
        "image": OFFICIAL_OG_IMAGE,
    }
    return [website_schema, organization_schema, page_schema]


def render_brand_mark(href: str) -> str:
    return (
        f'<a class="brand-mark" href="{escape(href)}">'
        f'<img src="{OFFICIAL_LOGO_SVG}" alt="Evoto" class="brand-mark__logo" />'
        "</a>"
    )


def render_nav_link(label: str, url: str) -> str:
    attrs = ' target="_blank" rel="noreferrer"' if url.startswith("http") else ""
    return f'<a href="{escape(url)}"{attrs}>{escape(label)}</a>'


def render_flat_resource_link(label: str, url: str) -> str:
    attrs = ' target="_blank" rel="noreferrer"' if url.startswith("http") else ""
    return f'<a class="browse-link" href="{escape(url)}"{attrs}>{escape(label)}</a>'


def render_product_badge_icon(icon_key: str) -> str:
    """
    Inline SVG icons for product cards.
    Use currentColor so `.feature-card__badge { color: var(--accent) }` controls icon color.
    """
    icon_key = (icon_key or "").strip().lower()
    common = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    if icon_key == "desktop":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <rect x="3.5" y="5.5" width="17" height="11" rx="1.8" {common} />
              <path d="M8 19.2h8" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "ipad":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <rect x="3.4" y="5.3" width="17.2" height="13.4" rx="2.6" {common} />
              <path d="M9.8 8.3h4.4" {common} />
              <path d="M12 16.5h0" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "mobile":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <rect x="7.5" y="2.8" width="9" height="18.4" rx="2.4" {common} />
              <path d="M10.2 5.8h3.6" {common} />
              <path d="M11.1 18.5h1.8" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "instant":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <path d="M13 2 5 14h7l-1 8 8-12h-7l1-8Z" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "video":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <rect x="3.5" y="6" width="17" height="12" rx="2.2" {common} />
              <path d="M11 10.2v3.6l3.2-1.8L11 10.2Z" fill="currentColor" stroke="none" />
            </svg>
            """
        ).format(common=common)
    if icon_key == "account":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <path d="M16.6 7.8a4.6 4.6 0 1 1-9.2 0 4.6 4.6 0 0 1 9.2 0Z" {common} />
              <path d="M4.8 20.2c1.9-3.4 5.1-5.1 7.2-5.1s5.3 1.7 7.2 5.1" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "price":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <path d="M10.4 3.8h4.2l5.2 5.2a2.2 2.2 0 0 1 0 3.1l-6.7 6.7a2.2 2.2 0 0 1-3.1 0L4.2 13a2.2 2.2 0 0 1 0-3.1l6.2-6.1Z" {common} />
              <path d="M14.8 8.1h0" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "faq":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <path d="M7.2 18.2 5 19V7.2A2.2 2.2 0 0 1 7.2 5h9.6A2.2 2.2 0 0 1 19 7.2v6.1a2.2 2.2 0 0 1-2.2 2.2H9.4l-2.2 2.7Z" {common} />
              <path d="M10.1 9.2a2.2 2.2 0 0 1 4.2.9c0 1.5-1.6 1.8-1.9 2.6" {common} />
              <path d="M12.4 14.8h0" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "tips":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <path d="M8.1 10.2a3.9 3.9 0 1 1 7.8 0c0 1.7-.9 2.7-2 3.7-.7.6-1.2 1.3-1.3 2.3h-1c-.1-1-.6-1.7-1.3-2.3-1.1-1-2-2-2-3.7Z" {common} />
              <path d="M10 19.2h4" {common} />
              <path d="M10.6 21h2.8" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "webinar":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <rect x="4.6" y="6.2" width="14.8" height="10.2" rx="2.2" {common} />
              <path d="M19.4 9.2l2.4-1.6v8.8l-2.4-1.6V9.2Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" />
            </svg>
            """
        ).format(common=common)
    if icon_key == "forum":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <path d="M7.4 16.8 5 18V7.4A2.4 2.4 0 0 1 7.4 5h9.2A2.4 2.4 0 0 1 19 7.4v5.8a2.4 2.4 0 0 1-2.4 2.4H9.8l-2.4 1.2Z" {common} />
              <path d="M9 9.2h6" {common} />
              <path d="M9 12h4.2" {common} />
            </svg>
            """
        ).format(common=common)
    if icon_key == "contact":
        return dedent(
            """\
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
              <rect x="4.8" y="6.6" width="14.4" height="10.8" rx="2.2" {common} />
              <path d="M6.6 8.4 12 12.2l5.4-3.8" {common} />
            </svg>
            """
        ).format(common=common)
    # Fallback: simple circle
    return dedent(
        """\
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
          <circle cx="12" cy="12" r="8" {common} />
        </svg>
        """
    ).format(common=common)


def render_site_footer(
    *,
    current_label: str = "Languages",
    language_options: list[tuple[str, str]] | None = None,
) -> str:
    def render_social_icon(label: str) -> str:
        key = (label or "").strip().lower()
        common = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
        # Minimal, legible outline glyphs (brand-agnostic).
        if key == "instagram":
            return (
                f'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
                f'<rect x="6" y="6" width="12" height="12" rx="3" {common} />'
                f'<path d="M10.4 12a1.6 1.6 0 1 0 3.2 0 1.6 1.6 0 0 0-3.2 0Z" {common} />'
                f'<path d="M16.2 7.8h0" {common} />'
                f"</svg>"
            )
        if key == "facebook":
            return (
                f'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
                f'<path d="M14 8.5h2V6h-2c-1.7 0-3 1.4-3 3v2H9v2.6h2V20h2.8v-6.4h2L17 11h-3.2V9c0-.3.2-.5.4-.5Z" fill="currentColor" stroke="none" />'
                f"</svg>"
            )
        if key == "youtube":
            return (
                f'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
                f'<rect x="5" y="7.2" width="14" height="9.6" rx="2.2" {common} />'
                f'<path d="M11 10.2v3.6l3.2-1.8L11 10.2Z" fill="currentColor" stroke="none" />'
                f"</svg>"
            )
        if key == "reddit":
            return (
                f'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
                f'<path d="M7.2 14.2c0 2.4 2.2 4.3 4.8 4.3s4.8-1.9 4.8-4.3c0-2.2-2-4-4.8-4s-4.8 1.8-4.8 4Z" {common} />'
                f'<path d="M9.8 13.7h0" {common} />'
                f'<path d="M14.2 13.7h0" {common} />'
                f'<path d="M10.2 16c.6.5 1.1.7 1.8.7s1.2-.2 1.8-.7" {common} />'
                f"</svg>"
            )
        if key == "tiktok":
            return (
                f'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
                f'<path d="M14 5.4c1 1.3 2.2 2.1 3.6 2.3v2.4c-1.4-.2-2.7-.9-3.6-1.8v5.6a4.6 4.6 0 1 1-3.6-4.5v2.6a2.2 2.2 0 1 0 1.4 2.1V4.8h2.2V5.4Z" fill="currentColor" stroke="none" />'
                f"</svg>"
            )
        if key == "linkedin":
            return (
                f'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
                f'<rect x="5.4" y="9.6" width="2.6" height="9" rx="0.8" fill="currentColor" stroke="none" />'
                f'<path d="M6.7 7.9a1.4 1.4 0 1 0 0-2.8 1.4 1.4 0 0 0 0 2.8Z" fill="currentColor" stroke="none" />'
                f'<path d="M10.2 9.6h2.4v1.2c.5-.9 1.5-1.4 2.8-1.4 2 0 3.4 1.3 3.4 3.8v5.4h-2.6v-5c0-1.3-.6-2.1-1.7-2.1-1.2 0-1.9.8-1.9 2.1v5h-2.6V9.6Z" fill="currentColor" stroke="none" />'
                f"</svg>"
            )
        return (
            f'<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
            f'<circle cx="12" cy="12" r="8" {common} />'
            f"</svg>"
        )

    social_markup = "".join(
        f'<a class="footer-social" href="{url}" target="_blank" rel="noreferrer" aria-label="{escape(label)}" title="{escape(label)}">{render_social_icon(label)}</a>'
        for label, url in SOCIAL_LINKS
    )
    language_menu = (
        render_language_menu(current_label=current_label, options=language_options or [], compact=True)
        if language_options
        else ""
    )
    return dedent(
        f"""\
        <footer class="site-footer">
          <div class="footer-shell">
            <div class="footer-main">
              <div class="footer-left">
                <div class="footer-brand">
                  <img src="{OFFICIAL_LOGO_SVG}" alt="Evoto" class="footer-brand__logo" />
                  <div class="footer-brand__copy">
                    <p class="footer-kicker">Get Evoto Free App</p>
                    <h2>{SITE_NAME}</h2>
                    <p>Official support, tutorials, and troubleshooting for the complete Evoto photography workflow.</p>
                    <div class="footer-app-buttons">
                      <a class="footer-app-button footer-app-button--desktop" href="{OFFICIAL_DOWNLOAD_URL}" target="_blank" rel="noreferrer">Desktop</a>
                      <a class="footer-app-button footer-app-button--ipad" href="{OFFICIAL_PRODUCT_IPAD_URL}" target="_blank" rel="noreferrer">iPad</a>
                      <a class="footer-app-button footer-app-button--mobile" href="{OFFICIAL_PRODUCT_MOBILE_URL}" target="_blank" rel="noreferrer">Mobile</a>
                    </div>
                  </div>
                </div>
              </div>
              <div class="footer-right">
                <div class="footer-grid">
                  <section class="footer-column">
                    <h3>Features</h3>
                    <a href="{site_url('/en/evoto-desktop/portrait-retouching/')}">Portrait Retouching</a>
                    <a href="{site_url('/en/evoto-desktop/color-adjustment/feature-introduction-ai-color-match/')}">AI Color Match</a>
                    <a href="{site_url('/en/evoto-desktop/background-adjustments/backdrop-changer/')}">AI Background Remover</a>
                    <a href="{site_url('/en/evoto-desktop/portrait-retouching/full-body-reshape/')}">AI Body Editor</a>
                    <a href="{site_url('/en/evoto-desktop/how-to-start/how-to-use-sync-the-feature-effect/')}">Batch Editing</a>
                  </section>
                  <section class="footer-column">
                    <h3>Resources</h3>
                    <a href="{OFFICIAL_BLOG_URL}" target="_blank" rel="noreferrer">Blog</a>
                    <a href="{OFFICIAL_WEBINAR_URL}" target="_blank" rel="noreferrer">Webinar</a>
                    <a href="{OFFICIAL_FORUM_URL}" target="_blank" rel="noreferrer">Forum</a>
                    <a href="{site_url('/')}">Learning Center</a>
                  </section>
                  <section class="footer-column">
                    <h3>Company</h3>
                    <a href="{OFFICIAL_SITE_URL}" target="_blank" rel="noreferrer">About Us</a>
                    <a href="{OFFICIAL_PRICING_URL}" target="_blank" rel="noreferrer">Pricing</a>
                    <a href="{OFFICIAL_DOWNLOAD_URL}" target="_blank" rel="noreferrer">Download</a>
                    <a href="{OFFICIAL_HELP_URL}" target="_blank" rel="noreferrer">Contact Us</a>
                  </section>
                </div>
              </div>
            </div>
            <div class="footer-bottom">
              <div class="footer-meta">
                <p>© 2026 Truesight Technology Inc. | 149 COMMONWEALTH DRIVE, SUITE 1049 MENLO PARK, CA 94025, USA</p>
                <div class="footer-legal-links">
                  <a href="{OFFICIAL_TERMS_URL}" target="_blank" rel="noreferrer">Terms of Use</a>
                  <a href="{OFFICIAL_PRIVACY_URL}" target="_blank" rel="noreferrer">Privacy Policy</a>
                  <a href="{OFFICIAL_COOKIE_URL}" target="_blank" rel="noreferrer">Cookie Policy</a>
                </div>
              </div>
              <div class="footer-utilities">
                {language_menu}
              </div>
              <div class="footer-socials">
                {social_markup}
              </div>
            </div>
          </div>
        </footer>
        """
    )


def render_doc_page(
    *,
    page: Page,
    nav_items: list[NavItem],
    languages: list[str],
    language_home_urls: dict[str, str],
    pages_by_lang: dict[str, dict[str, Page]],
) -> str:
    source_url = str(page.meta.get("source_url", "")).strip()
    child_cards = render_child_cards(page, pages_by_lang[page.lang])
    toc_markup = render_toc(page.headings)
    prev_next = render_prev_next(page)
    page_title = f"{page.title} | {SITE_NAME}"
    page_description = page.excerpt or DEFAULT_SEO_DESCRIPTION
    footer_language_options = [
        (LANGUAGE_LABELS.get(lang, lang), page.translation_links.get(lang, language_home_urls[lang]))
        for lang in languages
    ]

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="{escape(page.lang)}" data-base-path="{escape(BASE_PATH)}">
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            {render_head_meta(title=page_title, description=page_description, url=page.url, page_type="article")}
            <link rel="icon" href="{site_url('/static/favicon.svg')}" type="image/svg+xml" />
            <link rel="stylesheet" href="{site_url('/static/site.css')}" />
          </head>
          <body class="doc-body">
            <div class="site-bg"></div>
            <div class="doc-shell">
              {render_sidebar(page, nav_items, pages_by_lang[page.lang])}
              <div class="doc-main">
                {render_topbar(page, languages, language_home_urls)}
                <main class="article-wrap">
                  <section class="article-card">
                    <div class="eyebrow-row">
                      <span class="eyebrow-chip">{escape(LANGUAGE_LABELS.get(page.lang, page.lang))}</span>
                      <span class="eyebrow-chip subtle">Knowledge Base</span>
                    </div>
                    <div class="breadcrumb-row">
                      {render_breadcrumbs(page)}
                    </div>
                    <header class="article-header">
                      <h1>{escape(page.title)}</h1>
                      <p>{escape(page.excerpt or "Browse this Evoto knowledge base article.")}</p>
                    </header>
                    <div class="article-meta">
                      {render_source_link(source_url)}
                      <a href="{site_url('/search/')}" class="meta-link">Search all articles</a>
                      <a href="{OFFICIAL_DOWNLOAD_URL}" class="meta-link" target="_blank" rel="noreferrer">Download Evoto</a>
                    </div>
                    <article class="markdown-body">
                      {page.html_body}
                    </article>
                    {child_cards}
                    {prev_next}
                  </section>
                </main>
              </div>
              {toc_markup}
            </div>
            {render_site_footer(current_label=LANGUAGE_LABELS.get(page.lang, page.lang), language_options=footer_language_options)}
            <script src="{site_url('/static/site.js')}" defer></script>
          </body>
        </html>
        """
    )


def render_root_page(
    *,
    languages: list[str],
    language_home_urls: dict[str, str],
    feature_cards: list[dict[str, str]],
    intro: str,
    total_pages: int,
) -> str:
    products_dropdown_links = [
        ("Evoto Desktop", OFFICIAL_PRODUCT_DESKTOP_URL),
        ("Evoto iPad", OFFICIAL_PRODUCT_IPAD_URL),
        ("Evoto Mobile", OFFICIAL_PRODUCT_MOBILE_URL),
        ("Evoto Instant", OFFICIAL_PRODUCT_INSTANT_URL),
        ("Evoto Video", OFFICIAL_PRODUCT_VIDEO_URL),
    ]

    products_dropdown_items_markup = "".join(
        f'<a class="primary-nav-dropdown__item" href="{escape(url)}" target="_blank" rel="noreferrer">{escape(label)}</a>'
        for label, url in products_dropdown_links
    )

    learning_center_home = site_url("/")
    learning_center_item_markup = (
        f'<a class="primary-nav-dropdown__item primary-nav-dropdown__item--current" '
        f'href="{escape(learning_center_home)}" aria-current="page">Learning Center</a>'
    )
    resources_dropdown_links = [
        ("Blog", OFFICIAL_BLOG_URL),
        ("Webinar", OFFICIAL_WEBINAR_URL),
        ("Forum", OFFICIAL_FORUM_URL),
    ]
    resources_dropdown_items_markup = learning_center_item_markup + "".join(
        f'<a class="primary-nav-dropdown__item" href="{escape(url)}" target="_blank" rel="noreferrer">{escape(label)}</a>'
        for label, url in resources_dropdown_links
    )

    primary_nav_markup = "".join(
        [
            f"""
            <details class="primary-nav-dropdown">
              <summary class="primary-nav-dropdown__summary">
                <span class="primary-nav-dropdown__summary-label">Products</span>
                <span class="primary-nav-dropdown__caret" aria-hidden="true"></span>
              </summary>
              <div class="primary-nav-dropdown__list">
                {products_dropdown_items_markup}
              </div>
            </details>
            """,
            f"""
            <details class="primary-nav-dropdown primary-nav-dropdown--resources">
              <summary class="primary-nav-dropdown__summary">
                <span class="primary-nav-dropdown__summary-label">Resources</span>
                <span class="primary-nav-dropdown__caret" aria-hidden="true"></span>
              </summary>
              <div class="primary-nav-dropdown__list">
                {resources_dropdown_items_markup}
              </div>
            </details>
            """,
            render_nav_link("Pricing", OFFICIAL_PRICING_URL),
            render_nav_link("Download", OFFICIAL_DOWNLOAD_URL),
            f'<a class="sign-in-button" href="{escape(OFFICIAL_SIGNIN_URL)}">Sign in</a>',
        ]
    )

    product_links = feature_cards
    topic_links = []
    popular_links = [
        ("AI Color Match", site_url("/en/evoto-desktop/color-adjustment/feature-introduction-ai-color-match/")),
        ("Skin Retouching", site_url("/en/evoto-desktop/portrait-retouching/skin-retouching/")),
        ("Pricing FAQ", site_url("/en/price-billing/pricing-faqs/pricing-faq/")),
        ("Tethered Shooting", site_url("/en/evoto-desktop/tethered-shooting/")),
    ]
    product_markup = "".join(
        f'<a class="browse-link" href="{escape(card["url"])}">{escape(card["title"])}</a>'
        for card in product_links
    )
    product_card_markup = "".join(
        f"""
        <a class="feature-card feature-card--product" href="{escape(card['url'])}">
          <span class="feature-card__badge">{render_product_badge_icon(card.get('badge_icon_key', 'desktop'))}</span>
          <strong>{escape(card['title'])}</strong>
          <p>{escape(card['excerpt'])}</p>
        </a>
        """
        for card in product_links
    )
    learning_resources_cards = [
        {
            "title": "Evoto Webinar",
            "url": OFFICIAL_WEBINAR_URL,
            "excerpt": "Explore live and on-demand sessions to sharpen your editing workflow.",
            "badge_icon_key": "webinar",
            "cta": "Read More",
        },
        {
            "title": "Evoto Community Forum",
            "url": OFFICIAL_FORUM_URL,
            "excerpt": "Explore updates, share your experiences with other users, and help make Evoto stronger.",
            "badge_icon_key": "forum",
            "cta": "Read More",
        },
    ]
    contact_entry = {
        "title": "Can’t find what you want? Still have questions?",
        "url": OFFICIAL_HELP_URL,
        "excerpt": "",
        "badge_icon_key": "contact",
        "cta": "Contact Us",
    }
    learning_resources_markup = "".join(
        f"""
        <a class="learning-link learning-link--{escape(card['title'].strip().lower())}" href="{escape(card['url'])}" target="_blank" rel="noreferrer">
          <span class="learning-link__icon">{render_product_badge_icon(card.get('badge_icon_key', 'circle'))}</span>
          <span class="learning-link__text">
            <strong>{escape(card['title'])}</strong>
            <span class="learning-link__desc">{escape(card['excerpt'])}</span>
          </span>
          <span class="learning-link__cta">{escape(card.get('cta') or 'Learn more')}</span>
        </a>
        """
        for card in learning_resources_cards
    )
    contact_entry_markup = f"""
        <a class="contact-entry" href="{escape(contact_entry['url'])}" target="_blank" rel="noreferrer">
          <span class="contact-entry__icon">{render_product_badge_icon(contact_entry.get('badge_icon_key', 'circle'))}</span>
          <div class="contact-entry__body">
            <strong>{escape(contact_entry['title'])}</strong>
            <p>{escape(contact_entry['excerpt'])}</p>
          </div>
          <span class="contact-entry__cta">{escape(contact_entry.get('cta') or 'Contact')}</span>
        </a>
    """
    topic_markup = "".join(
        f'<a class="browse-link" href="{escape(card["url"])}">{escape(card["title"])}</a>'
        for card in topic_links
    )
    resource_markup = "".join(
        render_flat_resource_link(label, url)
        for label, url in [
            ("Official Site", OFFICIAL_SITE_URL),
            ("Download", OFFICIAL_DOWNLOAD_URL),
            ("Pricing", OFFICIAL_PRICING_URL),
            ("Blog", OFFICIAL_BLOG_URL),
            ("Webinar", OFFICIAL_WEBINAR_URL),
            ("Support Search", site_url("/search/")),
        ]
    )
    popular_markup = "".join(
        f'<a class="popular-link" href="{escape(url)}">{escape(label)}</a>'
        for label, url in popular_links
    )
    page_title = f"{SITE_NAME} | Official Support, Tutorials & Troubleshooting"
    page_description = (
        "Official Evoto help center with setup guides, troubleshooting, pricing answers, and workflow tutorials "
        "for Desktop, Mobile, iPad, and Instant."
    )

    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en" data-base-path="{escape(BASE_PATH)}">
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            {render_head_meta(title=page_title, description=page_description, url=site_url('/'), page_type="website")}
            <link rel="icon" href="{site_url('/static/favicon.svg')}" type="image/svg+xml" />
            <link rel="stylesheet" href="{site_url('/static/site.css')}" />
          </head>
          <body class="landing-body">
            <div class="site-bg"></div>
            <main class="landing-shell">
              <header class="landing-topbar">
                {render_brand_mark(site_url('/'))}
                <nav class="hero-primary-nav" aria-label="Hero navigation">
                  {primary_nav_markup}
                </nav>
              </header>
              <section class="landing-hero learning-hero">
                <div class="hero-copy learning-hero__panel">
                  <h1>Learning Center</h1>
                  <p>{escape(intro)}</p>
                  <form class="search-form search-form--landing" action="{site_url('/search/')}" method="get">
                    <label class="search-input">
                      <span class="sr-only">Search Evoto help articles</span>
                      <input
                        type="search"
                        name="q"
                        placeholder="Enter your search term"
                        data-search-input
                        autocomplete="off"
                      />
                    </label>
                    <button type="submit" class="search-button search-button--dark">Search</button>
                    <div class="search-results" data-search-results></div>
                  </form>
                  <div class="popular-strip">
                    <span class="popular-label">Popular:</span>
                    <div class="popular-links">
                      {popular_markup}
                    </div>
                  </div>
                </div>
              </section>

              <section class="landing-section" id="support-areas">
                <div class="section-heading section-heading--compact">
                  <h2>Choose an Evoto workspace</h2>
                </div>
                <div class="feature-grid feature-grid--products">
                  {product_card_markup}
                </div>
              </section>

              <section class="landing-section" id="learning-resources">
                <div class="learning-resources">
                  <div class="learning-resources__header">
                    <h2>More learning resources</h2>
                    <p>Explore webinars, community discussions, and hands-on support to keep improving your workflow.</p>
                  </div>
                  <div class="learning-resources__grid">
                    {learning_resources_markup}
                  </div>
                </div>
                <div class="learning-resources__contact-standalone">
                  {contact_entry_markup}
                </div>
              </section>
            </main>
            {render_site_footer(current_label="Languages", language_options=[(LANGUAGE_LABELS.get(lang, lang), language_home_urls[lang]) for lang in languages])}
            <script src="{site_url('/static/site.js')}" defer></script>
          </body>
        </html>
        """
    )


def render_search_page(languages: list[str], language_home_urls: dict[str, str]) -> str:
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en" data-base-path="{escape(BASE_PATH)}">
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            {render_head_meta(title=f"Search | {SITE_NAME}", description=DEFAULT_SEO_DESCRIPTION, url=site_url('/search/'), page_type="website", noindex=True)}
            <link rel="icon" href="{site_url('/static/favicon.svg')}" type="image/svg+xml" />
            <link rel="stylesheet" href="{site_url('/static/site.css')}" />
          </head>
          <body class="search-body">
            <div class="site-bg"></div>
            <main class="search-shell">
              <div class="topbar topbar--search">
                {render_brand_mark(site_url('/'))}
                <div class="topbar-actions">
                  <a class="meta-link" href="{language_home_urls.get('en', site_url('/en/'))}">Open English Home</a>
                </div>
              </div>
              <section class="search-page-card">
                <span class="hero-kicker">Official Search</span>
                <h1>Search the {SITE_NAME}</h1>
                <p>Search across all languages, products, setup guides, FAQ entries, and workflow tips.</p>
                <form class="search-form search-form--page" action="{site_url('/search/')}" method="get">
                  <label class="search-input">
                    <span class="sr-only">Search Evoto articles</span>
                    <input
                      type="search"
                      name="q"
                      placeholder="Try 'wireless tethering', 'skin retouching', 'credits', 'export'..."
                      data-search-input
                      autocomplete="off"
                    />
                  </label>
                  <button type="submit" class="search-button">Search</button>
                  <div class="search-results" data-search-results></div>
                </form>
                <div class="search-results-page" data-search-page-results></div>
              </section>
            </main>
            {render_site_footer(current_label="Languages", language_options=[(LANGUAGE_LABELS.get(lang, lang), language_home_urls[lang]) for lang in languages])}
            <script src="{site_url('/static/site.js')}" defer></script>
          </body>
        </html>
        """
    )


def render_not_found_page(languages: list[str], language_home_urls: dict[str, str]) -> str:
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en" data-base-path="{escape(BASE_PATH)}">
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            {render_head_meta(title=f"Page Not Found | {SITE_NAME}", description=DEFAULT_SEO_DESCRIPTION, url=site_url('/404.html'), page_type="website", noindex=True)}
            <link rel="icon" href="{site_url('/static/favicon.svg')}" type="image/svg+xml" />
            <link rel="stylesheet" href="{site_url('/static/site.css')}" />
          </head>
          <body class="search-body">
            <div class="site-bg"></div>
            <main class="search-shell">
              <section class="search-page-card">
                <span class="hero-kicker">404</span>
                <h1>This page is not in the generated help center</h1>
                <p>Use search or jump back into one of the published language spaces.</p>
                <form class="search-form search-form--page" action="{site_url('/search/')}" method="get">
                  <label class="search-input">
                    <span class="sr-only">Search Evoto articles</span>
                    <input
                      type="search"
                      name="q"
                      placeholder="Search the help center..."
                      data-search-input
                      autocomplete="off"
                    />
                  </label>
                  <button type="submit" class="search-button">Search</button>
                  <div class="search-results" data-search-results></div>
                </form>
              </section>
            </main>
            {render_site_footer(current_label="Languages", language_options=[(LANGUAGE_LABELS.get(lang, lang), language_home_urls[lang]) for lang in languages])}
            <script src="{site_url('/static/site.js')}" defer></script>
          </body>
        </html>
        """
    )


def render_sidebar(page: Page, nav_items: list[NavItem], pages: dict[str, Page]) -> str:
    root_page = pages.get("README.md")
    brand_url = root_page.url if root_page else build_page_url(page.lang, "README.md")
    return dedent(
        f"""\
        <aside class="sidebar" data-sidebar>
          <div class="sidebar-card">
            {render_brand_mark(brand_url)}
            <button class="sidebar-toggle" type="button" data-sidebar-close>Close</button>
          </div>
          <nav class="sidebar-nav" aria-label="Sidebar navigation">
            {render_nav_tree(nav_items, page, pages)}
          </nav>
        </aside>
        """
    )


def render_nav_tree(nav_items: list[NavItem], current_page: Page, pages: dict[str, Page]) -> str:
    return f'<ul class="nav-tree">{render_nav_items(nav_items, current_page, pages)}</ul>'


def render_nav_items(nav_items: list[NavItem], current_page: Page, pages: dict[str, Page]) -> str:
    chunks: list[str] = []
    for item in nav_items:
        target_page = pages.get(item.source_path)
        if not target_page:
            continue
        descendant_active = is_descendant_active(item, current_page.source_path)
        active_class = " active" if current_page.source_path == item.source_path else ""
        open_class = " open" if descendant_active else ""
        children_markup = ""
        if item.children:
            children_markup = f'<ul class="nav-tree nested">{render_nav_items(item.children, current_page, pages)}</ul>'
        chunks.append(
            f"""
            <li class="nav-item{open_class}">
              <a class="nav-link{active_class}" href="{escape(target_page.url)}">{escape(item.title)}</a>
              {children_markup}
            </li>
            """
        )
    return "".join(chunks)


def is_descendant_active(item: NavItem, current_source_path: str) -> bool:
    if item.source_path == current_source_path:
        return True
    return any(is_descendant_active(child, current_source_path) for child in item.children)


def render_topbar(page: Page, languages: list[str], language_home_urls: dict[str, str]) -> str:
    return dedent(
        f"""\
        <header class="topbar">
          <div class="topbar-left">
            <button class="sidebar-toggle" type="button" data-sidebar-open>Menu</button>
            {render_brand_mark(site_url('/'))}
          </div>
          <form class="search-form search-form--inline" action="{site_url('/search/')}" method="get">
            <label class="search-input">
              <span class="sr-only">Search Evoto articles</span>
              <input type="search" name="q" placeholder="Search the knowledge base..." data-search-input autocomplete="off" />
            </label>
            <div class="search-results" data-search-results></div>
          </form>
        </header>
        """
    )


def render_language_menu(
    *,
    current_label: str,
    options: list[tuple[str, str]],
    compact: bool = False,
) -> str:
    items = "".join(
        f'<a class="language-menu__item" href="{escape(url)}">{escape(label)}</a>'
        for label, url in options
    )
    compact_class = " compact" if compact else ""
    return (
        f'<details class="language-menu{compact_class}">'
        f'<summary class="language-menu__button">{escape(current_label)}</summary>'
        f'<div class="language-menu__list">{items}</div>'
        "</details>"
    )


def render_breadcrumbs(page: Page) -> str:
    if not page.breadcrumbs:
        return f'<a href="{escape(build_page_url(page.lang, "README.md"))}">{escape(LANGUAGE_LABELS.get(page.lang, page.lang))}</a>'
    crumbs = []
    for item in page.breadcrumbs:
        target_url = page.url if item.source_path == page.source_path else build_page_url(page.lang, item.source_path)
        crumbs.append(f'<a href="{escape(target_url)}">{escape(item.title)}</a>')
    return '<span class="breadcrumbs">' + '<span class="breadcrumbs__separator">/</span>'.join(crumbs) + "</span>"


def render_source_link(source_url: str) -> str:
    if not source_url:
        return ""
    return f'<a href="{escape(source_url)}" class="meta-link" target="_blank" rel="noreferrer">View original article</a>'


def render_child_cards(page: Page, pages: dict[str, Page]) -> str:
    items = []
    for child in page.children:
        target_page = pages.get(child.source_path)
        if not target_page:
            continue
        items.append(
            f"""
            <a class="section-card" href="{escape(target_page.url)}">
              <span class="section-card__badge">{escape(child.title[:1].upper())}</span>
              <strong>{escape(child.title)}</strong>
              <p>{escape(target_page.excerpt or "Open this Evoto help section.")}</p>
            </a>
            """
        )
    if not items:
        return ""
    return (
        '<section class="section-grid-wrap">'
        '<div class="section-grid-wrap__header"><h2>Browse This Section</h2><p>Jump directly into the related articles and subsections.</p></div>'
        f'<div class="section-grid">{"".join(items)}</div>'
        "</section>"
    )


def render_prev_next(page: Page) -> str:
    cards = []
    if page.previous_page:
        cards.append(
            f"""
            <a class="pager-card" href="{escape(page.previous_page.url)}">
              <span class="pager-card__eyebrow">Previous</span>
              <strong>{escape(page.previous_page.nav_title or page.previous_page.title)}</strong>
            </a>
            """
        )
    if page.next_page:
        cards.append(
            f"""
            <a class="pager-card" href="{escape(page.next_page.url)}">
              <span class="pager-card__eyebrow">Next</span>
              <strong>{escape(page.next_page.nav_title or page.next_page.title)}</strong>
            </a>
            """
        )
    if not cards:
        return ""
    return f'<nav class="pager-row" aria-label="Article pagination">{"".join(cards)}</nav>'


def render_toc(headings: list[dict[str, Any]]) -> str:
    if len(headings) < 2:
        return '<aside class="toc"><div class="toc-card"><p class="toc-empty">Use the sidebar and search to keep moving through the knowledge base.</p></div></aside>'

    links = "".join(
        f'<a class="toc-link toc-level-{heading["level"]}" href="#{escape(heading["id"])}">{escape(heading["title"])}</a>'
        for heading in headings
    )
    return (
        '<aside class="toc">'
        '<div class="toc-card">'
        '<p class="toc-title">On This Page</p>'
        f'<nav class="toc-links">{links}</nav>'
        "</div>"
        "</aside>"
    )


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    block, body = match.groups()
    result: dict[str, Any] = {}
    current_list_key: str | None = None

    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue

        list_match = re.match(r"^\s*-\s+(.*)$", line)
        if list_match and current_list_key:
            result.setdefault(current_list_key, []).append(parse_scalar(list_match.group(1)))
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not key_match:
            current_list_key = None
            continue

        key, value = key_match.groups()
        if value == "":
            result[key] = []
            current_list_key = key
        else:
            result[key] = parse_scalar(value)
            current_list_key = None

    return result, body


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if not value:
        return ""
    if value.startswith('"') and value.endswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def extract_first_heading(markdown_body: str) -> str:
    for line in markdown_body.splitlines():
        if line.startswith("# "):
            return clean_text(line[2:].strip())
    return ""


def normalize_source_path(path: str) -> str:
    cleaned = path.strip().split("#", 1)[0].split("?", 1)[0]
    cleaned = cleaned.lstrip("/")
    normalized = str(PurePosixPath(cleaned))
    if normalized == ".":
        return "README.md"
    return normalized


def build_page_url(lang: str, source_path: str) -> str:
    relative = PurePosixPath(source_path)
    if source_path == "README.md":
        raw_parts = [lang]
    elif relative.name == "README.md":
        raw_parts = [lang, *relative.parts[:-1]]
    else:
        raw_parts = [lang, *relative.parts[:-1], relative.stem]
    quoted = "/".join(quote(part) for part in raw_parts if part)
    return site_url(f"/{quoted}/")


def build_output_path(lang: str, source_path: str) -> Path:
    relative = PurePosixPath(source_path)
    if source_path == "README.md":
        directory = OUTPUT_DIR / lang
    elif relative.name == "README.md":
        directory = OUTPUT_DIR / lang / Path(*relative.parts[:-1])
    else:
        directory = OUTPUT_DIR / lang / Path(*relative.parts[:-1]) / relative.stem
    return directory / "index.html"


def html_to_text(html_body: str) -> str:
    text = TAG_RE.sub(" ", html_body)
    text = text.replace("&nbsp;", " ")
    return clean_text(unescape(text))


def clean_text(text: str) -> str:
    text = TAG_RE.sub("", text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\bwp:[\w/-]+\b", " ", text)
    text = re.sub(r"(?<![A-Za-z0-9])#(?![A-Za-z0-9])", " ", text)
    return WHITESPACE_RE.sub(" ", text).strip()


def build_excerpt(text: str, limit: int = 180) -> str:
    text = clean_text(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,.;:") + "…"


def summarize_page(page: Page | None, limit: int = 160) -> str:
    if page is None:
        return ""
    if page.children:
        preview = ", ".join(child.title for child in page.children[:5])
        if len(page.children) > 5:
            preview += ", and more"
        return build_excerpt(preview, limit=limit)
    return page.excerpt


def remove_title_prefix(text: str, title: str) -> str:
    normalized_text = clean_text(text)
    normalized_title = clean_text(title)
    if not normalized_title:
        return normalized_text
    if normalized_text == normalized_title:
        return normalized_text
    if normalized_text.startswith(normalized_title):
        trimmed = normalized_text[len(normalized_title) :].lstrip(" :-#|")
        return trimmed or normalized_text
    return normalized_text


def breadcrumb_label(nav_item: NavItem | None) -> str:
    if not nav_item:
        return ""
    return " / ".join(item.title for item in breadcrumb_items(nav_item)[:-1])


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        output.append(item)
    return output


def build_css() -> str:
    return dedent(
        """\
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
          --bg: #fbfaf8;
          --bg-soft: rgba(255, 255, 255, 0.9);
          --bg-panel: rgba(255, 255, 255, 0.82);
          --bg-panel-strong: rgba(255, 255, 255, 0.96);
          --ink: #171717;
          --muted: #71695f;
          --line: rgba(23, 23, 23, 0.1);
          --brand: #ffef9c;
          --brand-strong: #bfa54a;
          --accent: #141414;
          --accent-soft: rgba(255, 224, 80, 0.1);
          --surface-dark: #101010;
          --surface-darker: #0a0a0a;
          --shadow: 0 24px 64px rgba(23, 23, 23, 0.12);
          --radius-xl: 30px;
          --radius-lg: 22px;
          --radius-md: 16px;
          --radius-sm: 12px;
          --font-body: "Inter", "Avenir Next", "Helvetica Neue", "Segoe UI", sans-serif;
          --font-head: "Inter", "Avenir Next", "Helvetica Neue", "Segoe UI", sans-serif;
          --content-width: 1480px;
        }

        * {
          box-sizing: border-box;
        }

        html {
          scroll-behavior: smooth;
        }

        body {
          margin: 0;
          color: var(--ink);
          font-family: var(--font-body);
          background:
            radial-gradient(circle at top left, rgba(255, 224, 80, 0.22), transparent 30%),
            radial-gradient(circle at 82% 18%, rgba(255, 241, 164, 0.18), transparent 26%),
            linear-gradient(180deg, #fff8df 0%, #ffffff 62%);
        }

        a {
          color: var(--accent);
          text-decoration: none;
        }

        a:hover {
          color: var(--accent);
        }

        a:focus-visible,
        button:focus-visible,
        summary:focus-visible,
        input:focus-visible,
        select:focus-visible {
          outline: 2px solid rgba(255, 224, 80, 0.9);
          outline-offset: 2px;
          border-radius: 10px;
        }

        img {
          max-width: 100%;
          border-radius: 16px;
          box-shadow: 0 18px 40px rgba(30, 35, 38, 0.1);
        }

        .site-bg {
          position: fixed;
          inset: 0;
          pointer-events: none;
          background:
            linear-gradient(135deg, rgba(255, 255, 255, 0.42), transparent 38%),
            radial-gradient(circle at 16% 14%, rgba(255, 224, 80, 0.18), transparent 24%),
            radial-gradient(circle at 82% 8%, rgba(255, 241, 164, 0.16), transparent 20%);
          z-index: -1;
        }

        .doc-shell {
          max-width: var(--content-width);
          margin: 0 auto;
          padding: 24px;
          display: grid;
          grid-template-columns: 320px minmax(0, 1fr) 250px;
          gap: 22px;
          align-items: start;
        }

        .landing-shell,
        .search-shell {
          max-width: var(--content-width);
          margin: 0 auto;
          padding: 36px 40px 80px;
        }

        .sidebar,
        .toc {
          position: sticky;
          top: 24px;
        }

        .sidebar-card,
        .toc-card,
        .article-card,
        .hero-panel,
        .search-page-card,
        .topbar,
        .language-card,
        .feature-card,
        .section-card,
        .pager-card,
        .stat-card {
          background: var(--bg-panel);
          backdrop-filter: blur(16px);
          border: 1px solid var(--line);
          box-shadow: var(--shadow);
        }

        .sidebar {
          max-height: calc(100vh - 48px);
          overflow: auto;
        }

        .sidebar-card {
          border-radius: var(--radius-xl);
          padding: 22px;
          margin-bottom: 16px;
        }

        .brand-mark {
          display: inline-flex;
          align-items: center;
          gap: 12px;
          font-size: 1rem;
          font-weight: 600;
          letter-spacing: 0.02em;
          color: var(--ink);
        }

        .brand-mark::before {
          display: none;
        }

        .brand-mark__logo {
          width: 96px;
          max-height: 28px;
          object-fit: contain;
          border-radius: 0;
          box-shadow: none;
        }

        .sidebar-copy,
        .toc-empty,
        .feature-card p,
        .language-card__code,
        .search-page-card p,
        .stat-card span,
        .section-card p,
        .article-header p {
          color: var(--muted);
        }

        .sidebar-nav {
          background: var(--bg-panel);
          border: 1px solid var(--line);
          border-radius: var(--radius-xl);
          padding: 18px;
          box-shadow: var(--shadow);
        }

        .nav-tree,
        .nav-tree ul {
          list-style: none;
          margin: 0;
          padding: 0;
        }

        .nav-tree.nested {
          margin-top: 10px;
          margin-left: 14px;
          padding-left: 12px;
          border-left: 1px solid rgba(21, 33, 38, 0.08);
        }

        .nav-item + .nav-item {
          margin-top: 8px;
        }

        .nav-link {
          display: block;
          padding: 10px 12px;
          border-radius: 12px;
          color: var(--muted);
          line-height: 1.35;
        }

        .nav-link:hover,
        .nav-link.active {
          background: rgba(255, 224, 80, 0.18);
          color: var(--accent);
        }

        .doc-main {
          min-width: 0;
        }

        .topbar {
          border-radius: 999px;
          padding: 14px 18px;
          display: flex;
          align-items: center;
          gap: 16px;
          justify-content: space-between;
        }

        .topbar-left {
          display: flex;
          align-items: center;
          gap: 12px;
        }

        .landing-topbar {
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: 28px;
          min-height: 56px;
          padding: 0;
          border-radius: 0;
          background: transparent;
          border: 0;
          box-shadow: none;
        }

        .landing-topbar .brand-mark {
          flex: 0 0 auto;
          gap: 3px;
        }

        .landing-topbar .brand-mark__logo {
          width: 114px;
          max-height: 34px;
        }

        .landing-topbar .brand-mark__text {
          font-size: 1.1rem;
          font-weight: 500;
          line-height: 1;
          letter-spacing: 0;
        }

        .landing-topbar .hero-primary-nav {
          flex: 1 1 auto;
        }

        .hero-topbar {
          display: grid;
          grid-template-columns: auto 1fr auto;
          align-items: center;
          gap: 24px;
          margin-bottom: 26px;
        }

        .hero-topbar .brand-mark__text {
          color: white;
        }

        .hero-topbar .brand-mark__logo {
          filter: brightness(0) invert(1);
          border-radius: 0;
          box-shadow: none;
        }

        .hero-topbar-actions {
          display: flex;
          justify-content: flex-end;
        }

        .hero-primary-nav {
          display: flex;
          justify-content: flex-end;
          gap: 30px;
          flex-wrap: nowrap;
          align-items: center;
        }

        .hero-primary-nav a:not(.sign-in-button):not(.primary-nav-dropdown__item):not(.primary-nav-dropdown__item--current) {
          color: rgba(20, 20, 20, 0.72);
          font-size: 1.1rem;
          font-weight: 500;
          transition: color 0.2s ease;
          line-height: 1;
          display: inline-flex;
          align-items: center;
        }

        .hero-primary-nav a:not(.sign-in-button):not(.primary-nav-dropdown__item):not(.primary-nav-dropdown__item--current):hover {
          color: rgba(20, 20, 20, 1);
        }

        .primary-nav-dropdown {
          position: relative;
        }

        .primary-nav-dropdown__summary {
          list-style: none;
          display: inline-flex;
          align-items: center;
          gap: 8px;
          cursor: pointer;
          line-height: 1;
        }

        .primary-nav-dropdown__summary::-webkit-details-marker {
          display: none;
        }

        .primary-nav-dropdown__summary-label {
          color: rgba(20, 20, 20, 0.72);
          font-size: 1.1rem;
          font-weight: 500;
          transition: color 0.2s ease;
          user-select: none;
        }

        .primary-nav-dropdown__summary:hover .primary-nav-dropdown__summary-label {
          color: rgba(20, 20, 20, 1);
        }

        .primary-nav-dropdown__caret {
          flex-shrink: 0;
          width: 0;
          height: 0;
          border-left: 5px solid transparent;
          border-right: 5px solid transparent;
          border-top: 6px solid rgba(20, 20, 20, 0.72);
          transform: translateY(0px);
        }

        .primary-nav-dropdown[open] .primary-nav-dropdown__caret,
        .primary-nav-dropdown__summary:hover .primary-nav-dropdown__caret {
          border-top-color: rgba(20, 20, 20, 1);
        }

        .primary-nav-dropdown__list {
          display: none;
          position: absolute;
          top: calc(100% + 12px);
          left: 0;
          min-width: 240px;
          padding: 8px;
          border-radius: 16px;
          background: #ffffff;
          border: 1px solid rgba(23, 23, 23, 0.08);
          box-shadow:
            0 4px 24px rgba(23, 23, 23, 0.08),
            0 16px 48px rgba(23, 23, 23, 0.12);
          z-index: 50;
        }

        .primary-nav-dropdown[open] .primary-nav-dropdown__list {
          display: flex;
          flex-direction: column;
          gap: 2px;
          align-items: stretch;
        }

        .primary-nav-dropdown--resources .primary-nav-dropdown__list {
          min-width: 280px;
        }

        .primary-nav-dropdown__item {
          color: #171717;
          font-size: 1rem;
          font-weight: 500;
          padding: 12px 14px;
          border-radius: 12px;
          transition: background 0.15s ease, color 0.15s ease;
          display: block;
          width: 100%;
          text-decoration: none;
          line-height: 1.3;
        }

        .primary-nav-dropdown__item:hover,
        .primary-nav-dropdown__item:focus-visible {
          background: rgba(23, 23, 23, 0.06);
          color: #0a0a0a;
          outline: none;
        }

        .primary-nav-dropdown__item--current {
          cursor: default;
          color: rgba(23, 23, 23, 0.42);
        }

        .primary-nav-dropdown__item--current:hover,
        .primary-nav-dropdown__item--current:focus-visible {
          background: transparent;
          color: rgba(23, 23, 23, 0.42);
        }

        .sign-in-button {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          padding: 12px 20px;
          border-radius: 999px;
          background: #141414;
          color: white;
          font-weight: 600;
          font-size: 1.08rem;
          transition: opacity 0.2s ease;
        }

        .sign-in-button:hover {
          opacity: 0.95;
          color: white;
        }

        .topbar-actions {
          display: flex;
          align-items: center;
          gap: 10px;
          flex-wrap: wrap;
          margin-left: auto;
        }

        .topbar--search {
          border-radius: var(--radius-xl);
          justify-content: space-between;
          margin-bottom: 20px;
        }

        .sidebar-toggle {
          display: none;
          border: 0;
          border-radius: 999px;
          padding: 10px 14px;
          font: inherit;
          font-weight: 600;
          cursor: pointer;
          color: white;
          background: linear-gradient(135deg, var(--brand), var(--accent));
        }

        .search-form {
          position: relative;
          width: 100%;
        }

        .search-form--inline {
          max-width: 420px;
        }

        .search-form--hero,
        .search-form--page {
          max-width: 760px;
        }

        .search-input {
          display: block;
          width: 100%;
        }

        .search-input input {
          width: 100%;
          border-radius: 999px;
          border: 1px solid rgba(21, 33, 38, 0.12);
          background: rgba(255, 255, 255, 0.82);
          color: var(--ink);
          padding: 15px 18px;
          font: inherit;
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.55);
        }

        .search-form--hero,
        .search-form--page {
          display: flex;
          align-items: center;
          gap: 12px;
          flex-wrap: wrap;
        }

        .search-form--hero .search-input,
        .search-form--page .search-input {
          flex: 1 1 420px;
        }

        .search-button {
          border: 0;
          border-radius: 999px;
          padding: 15px 22px;
          font: inherit;
          font-weight: 600;
          cursor: pointer;
          color: var(--accent);
          background: linear-gradient(135deg, #fff1a4, var(--brand));
          box-shadow: 0 18px 32px rgba(255, 224, 80, 0.28);
        }

        .search-results {
          position: absolute;
          left: 0;
          right: 0;
          top: calc(100% + 12px);
          display: none;
          border-radius: 20px;
          padding: 10px;
          background: rgba(255, 255, 255, 0.96);
          border: 1px solid var(--line);
          box-shadow: var(--shadow);
          z-index: 30;
        }

        .search-results.is-visible {
          display: block;
        }

        .search-result-item {
          display: block;
          padding: 12px 14px;
          border-radius: 14px;
          color: inherit;
        }

        .search-result-item:hover {
          background: rgba(255, 224, 80, 0.14);
        }

        .search-result-item strong,
        .feature-card strong,
        .section-card strong,
        .pager-card strong,
        .language-card__label {
          display: block;
          font-size: 1rem;
          color: var(--ink);
          font-weight: 600;
        }

        .search-result-item span {
          display: block;
          color: var(--muted);
          margin-top: 4px;
          font-size: 0.92rem;
        }

        .article-wrap {
          padding-top: 18px;
        }

        .article-card,
        .search-page-card {
          border-radius: var(--radius-xl);
          padding: clamp(22px, 3vw, 36px);
        }

        .article-header h1,
        .landing-hero h1,
        .search-page-card h1,
        .section-heading h2 {
          margin: 0;
          font-family: var(--font-head);
          font-size: clamp(2.2rem, 4vw, 4.3rem);
          line-height: 0.95;
          letter-spacing: -0.03em;
          font-weight: 600;
        }

        .search-page-card h1,
        .section-heading h2 {
          font-size: clamp(2rem, 3vw, 3rem);
          line-height: 1.02;
        }

        .article-header p,
        .landing-hero p,
        .search-page-card p {
          max-width: 760px;
          font-size: 1.04rem;
          line-height: 1.7;
        }

        .eyebrow-row {
          display: flex;
          gap: 10px;
          flex-wrap: wrap;
          margin-bottom: 16px;
        }

        .eyebrow-chip {
          display: inline-flex;
          align-items: center;
          border-radius: 999px;
          padding: 8px 12px;
          font-size: 0.88rem;
          font-weight: 600;
          letter-spacing: 0.02em;
          color: var(--accent);
          background: rgba(255, 224, 80, 0.24);
        }

        .eyebrow-chip.subtle {
          color: var(--accent);
          background: rgba(255, 224, 80, 0.32);
        }

        .hero-kicker {
          display: inline-block;
          margin-bottom: 16px;
          color: var(--accent);
          font-size: 0.88rem;
          font-weight: 600;
          letter-spacing: 0.08em;
          text-transform: uppercase;
        }

        .hero-brand {
          display: flex;
          align-items: center;
          gap: 14px;
          margin-bottom: 16px;
          flex-wrap: wrap;
        }

        .hero-brand__logo {
          width: 118px;
          max-height: 32px;
          object-fit: contain;
        }

        .hero-links {
          display: flex;
          gap: 12px;
          flex-wrap: wrap;
          margin: 20px 0 26px;
        }

        .hero-link {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          min-width: 168px;
          border-radius: 999px;
          padding: 14px 20px;
          font-weight: 600;
          transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
        }

        .hero-link:hover {
          transform: translateY(-1px);
        }

        .hero-link--primary {
          color: var(--accent);
          background: linear-gradient(135deg, #fff1a4, var(--brand));
          box-shadow: 0 18px 32px rgba(255, 224, 80, 0.28);
        }

        .hero-link--secondary {
          color: var(--accent);
          background: rgba(255, 255, 255, 0.92);
          border: 1px solid rgba(23, 23, 23, 0.12);
        }

        .breadcrumb-row {
          margin-bottom: 18px;
        }

        .breadcrumbs {
          display: inline-flex;
          align-items: center;
          flex-wrap: wrap;
          gap: 8px;
          color: var(--muted);
          font-size: 0.92rem;
        }

        .breadcrumbs__separator {
          color: rgba(21, 33, 38, 0.34);
        }

        .article-meta {
          display: flex;
          gap: 14px;
          flex-wrap: wrap;
          margin-bottom: 26px;
        }

        .meta-link {
          display: inline-flex;
          align-items: center;
          gap: 8px;
          border-radius: 999px;
          padding: 9px 12px;
          color: var(--ink);
          background: rgba(255, 255, 255, 0.66);
          border: 1px solid rgba(21, 33, 38, 0.1);
        }

        .markdown-body {
          font-size: 1.02rem;
          line-height: 1.78;
        }

        .markdown-body > :first-child {
          margin-top: 0;
        }

        .markdown-body h1,
        .markdown-body h2,
        .markdown-body h3,
        .markdown-body h4,
        .markdown-body h5,
        .markdown-body h6 {
          position: relative;
          margin-top: 1.8em;
          margin-bottom: 0.65em;
          font-family: var(--font-head);
          line-height: 1.08;
          color: var(--ink);
          font-weight: 600;
        }

        .markdown-body h2 {
          font-size: 1.95rem;
        }

        .markdown-body h3 {
          font-size: 1.42rem;
        }

        .markdown-body p,
        .markdown-body ul,
        .markdown-body ol,
        .markdown-body blockquote,
        .markdown-body table {
          margin-top: 0;
          margin-bottom: 1.15em;
        }

        .markdown-body ul,
        .markdown-body ol {
          padding-left: 1.25rem;
        }

        .markdown-body li + li {
          margin-top: 0.4em;
        }

        .markdown-body code {
          padding: 0.15em 0.42em;
          border-radius: 8px;
          background: rgba(21, 33, 38, 0.08);
          font-family: "SFMono-Regular", "Menlo", monospace;
          font-size: 0.92em;
        }

        .markdown-body pre {
          overflow: auto;
          padding: 18px;
          border-radius: 18px;
          background: #132025;
          color: #f4efe8;
        }

        .markdown-body pre code {
          padding: 0;
          background: transparent;
          color: inherit;
        }

        .markdown-body blockquote {
          padding: 14px 18px;
          border-left: 4px solid var(--accent);
          background: rgba(207, 110, 67, 0.08);
          border-radius: 0 16px 16px 0;
        }

        .table-wrap {
          overflow-x: auto;
          margin-bottom: 1.2em;
        }

        .markdown-body table {
          width: 100%;
          border-collapse: collapse;
          min-width: 520px;
          background: rgba(255, 255, 255, 0.72);
          border-radius: 16px;
          overflow: hidden;
        }

        .markdown-body th,
        .markdown-body td {
          padding: 12px 14px;
          border-bottom: 1px solid rgba(21, 33, 38, 0.08);
          text-align: left;
          vertical-align: top;
        }

        .markdown-body th {
          background: rgba(11, 107, 99, 0.08);
          font-weight: 600;
        }

        .micro-heading {
          display: inline-block;
          color: var(--accent);
          font-weight: 600;
          letter-spacing: 0.04em;
          text-transform: uppercase;
        }

        .heading-anchor {
          opacity: 0;
          margin-left: 0.45rem;
          color: rgba(20, 20, 20, 0.56);
          transition: opacity 0.15s ease;
        }

        .markdown-body h2:hover .heading-anchor,
        .markdown-body h3:hover .heading-anchor,
        .markdown-body h4:hover .heading-anchor {
          opacity: 1;
        }

        .section-grid-wrap {
          margin-top: 40px;
          padding-top: 28px;
          border-top: 1px solid rgba(21, 33, 38, 0.08);
        }

        .section-grid-wrap__header h2 {
          margin-bottom: 6px;
          font-family: var(--font-head);
          font-size: 1.8rem;
        }

        .section-grid,
        .feature-grid,
        .language-grid,
        .stat-row,
        .pager-row {
          display: grid;
          gap: 16px;
        }

        .section-grid,
        .feature-grid {
          grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        }

        .stat-card,
        .feature-card,
        .section-card,
        .pager-card {
          border-radius: 20px;
          padding: 18px;
        }

        .stat-card strong {
          display: block;
          font-size: 2rem;
          font-family: var(--font-head);
          line-height: 1;
          margin-bottom: 8px;
          font-weight: 600;
        }

        .feature-card,
        .section-card,
        .pager-card {
          color: inherit;
        }

        .feature-card:hover,
        .section-card:hover,
        .pager-card:hover {
          transform: translateY(-2px);
          transition: transform 0.2s ease, box-shadow 0.2s ease;
          box-shadow: 0 32px 56px rgba(31, 44, 48, 0.16);
        }

        .feature-card__badge,
        .section-card__badge {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          width: 38px;
          height: 38px;
          border-radius: 14px;
          margin-bottom: 14px;
          font-weight: 600;
          color: var(--accent);
          background: linear-gradient(135deg, #fff1a4, var(--brand));
        }

        .feature-card__badge svg,
        .section-card__badge svg {
          display: block;
          width: 20px;
          height: 20px;
        }

        .pager-row {
          margin-top: 40px;
          grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        }

        .pager-card__eyebrow,
        .toc-title {
          display: block;
          margin-bottom: 8px;
          color: var(--muted);
          font-size: 0.84rem;
          letter-spacing: 0.08em;
          text-transform: uppercase;
        }

        .toc-card {
          border-radius: var(--radius-xl);
          padding: 20px;
        }

        .toc-links {
          display: flex;
          flex-direction: column;
          gap: 10px;
        }

        .toc-link {
          color: var(--muted);
          line-height: 1.35;
        }

        .toc-link:hover {
          color: var(--brand-strong);
        }

        .toc-level-3,
        .toc-level-4,
        .toc-level-5,
        .toc-level-6 {
          padding-left: 12px;
        }

        .landing-hero {
          display: block;
          padding: 28px 0 44px;
        }

        .hero-copy {
          padding: clamp(12px, 2vw, 18px) 0 0;
        }

        .learning-hero__panel {
          position: relative;
          color: var(--accent);
          text-align: center;
          background: transparent;
          border: 0;
          box-shadow: none;
          border-radius: 0;
          padding: 0;
        }

        .learning-hero__panel::before {
          display: none;
        }

        .learning-hero__panel > * {
          position: relative;
          z-index: 1;
        }

        .landing-section {
          margin-top: 16px;
        }

        .landing-hero h1 {
          color: var(--accent);
          margin-top: 12px;
          margin-bottom: 14px;
          font-size: clamp(2.8rem, 5vw, 4.8rem);
        }

        .landing-hero p {
          max-width: 720px;
          margin-left: auto;
          margin-right: auto;
          color: rgba(20, 20, 20, 0.72);
        }

        .search-form--landing {
          display: flex;
          align-items: center;
          gap: 14px;
          justify-content: center;
          flex-wrap: nowrap;
          max-width: 900px;
          margin: 28px auto 0;
        }

        .search-form--landing .search-input {
          flex: 1 1 auto;
        }

        .search-button--dark {
          min-width: 134px;
          color: white;
          background: #141414;
          box-shadow: 0 8px 20px rgba(20, 20, 20, 0.24);
        }

        .popular-strip {
          display: flex;
          align-items: baseline;
          justify-content: center;
          gap: 8px;
          flex-wrap: wrap;
          margin-top: 24px;
        }

        .popular-label {
          color: rgba(20, 20, 20, 0.8);
          font-size: 0.94rem;
          font-weight: 600;
        }

        .popular-links {
          display: flex;
          gap: 12px;
          flex-wrap: wrap;
          justify-content: center;
        }

        .popular-link {
          color: rgba(20, 20, 20, 0.84);
          font-size: 0.94rem;
          text-decoration: underline;
          text-decoration-color: rgba(20, 20, 20, 0.28);
          text-underline-offset: 0.16em;
        }

        .popular-link:hover {
          color: var(--accent);
        }

        .browse-band {
          display: grid;
          gap: 10px;
          margin-top: 34px;
        }

        .browse-row {
          display: grid;
          grid-template-columns: 140px minmax(0, 1fr);
          gap: 20px;
          align-items: start;
          padding: 20px 0;
          border-top: 1px solid rgba(20, 20, 20, 0.1);
        }

        .browse-row:last-child {
          border-bottom: 1px solid rgba(20, 20, 20, 0.1);
        }

        .browse-row__label {
          color: rgba(20, 20, 20, 0.56);
          font-size: 0.86rem;
          font-weight: 500;
          letter-spacing: 0.08em;
          text-transform: uppercase;
        }

        .browse-row__links {
          display: flex;
          gap: 18px;
          flex-wrap: wrap;
        }

        .browse-link {
          color: var(--accent);
          font-size: 1rem;
          font-weight: 500;
          line-height: 1.4;
          padding-bottom: 5px;
          border-bottom: 1px solid rgba(20, 20, 20, 0.12);
        }

        .browse-link:hover {
          border-color: rgba(20, 20, 20, 0.48);
        }

        .section-heading {
          margin-bottom: 22px;
        }

        .section-heading {
          margin-bottom: 18px;
        }

        .section-heading--compact {
          margin-bottom: 18px;
          letter-spacing: -0.01em;
        }

        .feature-grid--products {
          margin-bottom: 40px;
          gap: clamp(28px, 3.5vw, 44px);
          grid-template-columns: repeat(
            auto-fit,
            minmax(min(100%, 340px), 1fr)
          );
          align-items: stretch;
        }

        .feature-card--product {
          background: rgba(255, 255, 255, 0.9);
          border: 1px solid rgba(20, 20, 20, 0.08);
          box-shadow: 0 18px 34px rgba(20, 20, 20, 0.08);
          text-align: center;
          border-radius: 24px;
          padding: clamp(26px, 3vw, 36px) clamp(22px, 2.5vw, 30px)
            clamp(30px, 3.2vw, 40px);
          transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }

        .feature-card--product:hover {
          transform: translateY(-3px);
          box-shadow: 0 24px 46px rgba(20, 20, 20, 0.13);
          border-color: rgba(20, 20, 20, 0.14);
        }

        .feature-card--product .feature-card__badge {
          margin-left: auto;
          margin-right: auto;
          width: 48px;
          height: 48px;
          border-radius: 16px;
          margin-bottom: 18px;
        }

        .feature-card--product .feature-card__badge svg {
          width: 30px;
          height: 30px;
        }

        .feature-card--product strong {
          font-size: 1.18rem;
          margin-bottom: 12px;
          letter-spacing: -0.01em;
        }

        .feature-card--product p {
          font-size: 0.98rem;
          line-height: 1.58;
          max-width: 38ch;
          margin-left: auto;
          margin-right: auto;
          color: rgba(20, 20, 20, 0.62);
        }

        .learning-resources {
          border-radius: 0;
          border: 0;
          background: transparent;
          box-shadow: none;
          padding: 0;
        }

        .learning-resources__header {
          display: grid;
          gap: 8px;
          margin-bottom: 18px;
        }

        .learning-resources__header h2 {
          margin: 0;
        }

        .learning-resources__header p {
          margin: 0;
          color: rgba(20, 20, 20, 0.62);
          line-height: 1.6;
          max-width: 72ch;
        }

        .learning-resources__grid {
          display: grid;
          grid-template-columns: repeat(2, minmax(0, 1fr));
          gap: 14px;
        }

        .learning-resources__contact {
          margin-top: 14px;
        }

        .learning-resources__contact-standalone {
          margin-top: 28px;
          display: flex;
          justify-content: center;
          padding-top: 0;
        }

        .learning-link {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 12px;
          padding: 22px 24px;
          color: #171717;
          text-decoration: none;
          border-radius: 14px;
          border: 1px solid rgba(20, 20, 20, 0.06);
          min-height: 180px;
          transition: transform 0.15s ease, box-shadow 0.15s ease;
        }

        .learning-link:hover {
          transform: translateY(-2px);
          box-shadow: 0 14px 28px rgba(20, 20, 20, 0.12);
        }

        .learning-link--evoto.webinar {
          background: #dce8f8;
        }

        .learning-link--evoto.community.forum {
          background: #e7ddfb;
        }

        a.learning-link[href="https://www.evoto.ai/webinar"] {
          background: #dce8f8;
        }

        a.learning-link[href="https://forum.evoto.ai/"] {
          background: #e7ddfb;
        }

        .learning-link__icon {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          width: 48px;
          height: 48px;
          border-radius: 14px;
          background: rgba(255, 255, 255, 0.6);
        }

        .learning-link--evoto.webinar .learning-link__icon,
        a.learning-link[href="https://www.evoto.ai/webinar"] .learning-link__icon {
          color: #3472b8;
          background: rgba(255, 255, 255, 0.65);
        }

        .learning-link--evoto.community.forum .learning-link__icon,
        a.learning-link[href="https://forum.evoto.ai/"] .learning-link__icon {
          color: #6d4cc9;
          background: rgba(255, 255, 255, 0.65);
        }

        .learning-link__icon svg {
          width: 32px;
          height: 32px;
        }

        .learning-link__text {
          display: grid;
          gap: 8px;
          min-width: 0;
          text-align: center;
        }

        .learning-link__text strong {
          display: block;
          font-size: 1.9rem;
          line-height: 1.05;
        }

        .learning-link__desc {
          display: block;
          color: rgba(20, 20, 20, 0.62);
          line-height: 1.45;
          font-size: 0.95rem;
          max-width: 50ch;
        }

        .learning-link__cta {
          display: inline-flex;
          align-items: center;
          gap: 8px;
          font-weight: 700;
          color: #fff;
          white-space: nowrap;
          margin-top: 2px;
          padding: 9px 20px;
          border-radius: 999px;
          background: #111318;
        }

        .learning-link__cta::after {
          content: "";
        }

        .contact-entry {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 12px;
          width: min(100%, 680px);
          padding: 28px 24px 32px;
          border-radius: 14px;
          border: 1px solid rgba(20, 20, 20, 0.06);
          background:
            linear-gradient(115deg, rgba(255, 239, 200, 0.22) 0%, rgba(255, 244, 218, 0.16) 54%, rgba(255, 248, 230, 0.12) 100%),
            rgba(255, 255, 255, 0.82);
          color: inherit;
          text-decoration: none;
          transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .contact-entry:hover {
          transform: translateY(-2px);
          box-shadow: 0 14px 28px rgba(20, 20, 20, 0.1);
        }

        .contact-entry__icon {
          display: none;
        }

        .contact-entry__icon svg {
          width: 24px;
          height: 24px;
        }

        .contact-entry__body {
          min-width: 0;
          text-align: center;
        }

        .contact-entry__body strong {
          display: block;
          margin: 0;
          font-size: 1.4rem;
          line-height: 1.15;
        }

        .contact-entry__body p {
          display: none;
        }

        .contact-entry__cta {
          display: inline-flex;
          align-items: center;
          gap: 8px;
          padding: 10px 24px;
          border-radius: 999px;
          background: #111318;
          color: #fff;
          font-weight: 700;
          flex-shrink: 0;
        }

        .contact-entry__cta::after {
          content: "";
        }

        @media (prefers-reduced-motion: reduce) {
          *,
          *::before,
          *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
            scroll-behavior: auto !important;
          }
        }

        .search-page-card {
          max-width: 980px;
          margin: 0 auto;
        }

        .search-results-page {
          margin-top: 28px;
          display: grid;
          gap: 14px;
        }

        .search-page-result {
          padding: 18px;
          border-radius: 18px;
          background: rgba(255, 255, 255, 0.7);
          border: 1px solid rgba(21, 33, 38, 0.1);
        }

        .language-menu {
          position: relative;
        }

        .language-menu[open] .language-menu__button {
          background: rgba(255, 224, 80, 0.18);
          border-color: rgba(255, 224, 80, 0.34);
        }

        .language-menu__button {
          list-style: none;
          display: inline-flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
          min-width: 94px;
          border-radius: 999px;
          padding: 10px 14px;
          color: var(--ink);
          background: rgba(255, 255, 255, 0.92);
          border: 1px solid rgba(23, 23, 23, 0.1);
          cursor: pointer;
          font-size: 0.92rem;
          font-weight: 500;
          transition: background 0.2s ease, border-color 0.2s ease;
        }

        .language-menu__button::-webkit-details-marker {
          display: none;
        }

        .language-menu__button::after {
          content: "▾";
          font-size: 0.8rem;
          color: var(--muted);
        }

        .language-menu__list {
          position: absolute;
          right: 0;
          top: calc(100% + 10px);
          min-width: 180px;
          display: grid;
          gap: 6px;
          padding: 10px;
          border-radius: 18px;
          background: rgba(255, 255, 255, 0.98);
          border: 1px solid rgba(23, 23, 23, 0.1);
          box-shadow: var(--shadow);
          z-index: 40;
        }

        .language-menu.compact .language-menu__button {
          min-width: 84px;
          padding: 9px 12px;
        }

        .language-menu__item {
          display: block;
          padding: 10px 12px;
          border-radius: 12px;
          color: var(--ink);
          white-space: nowrap;
        }

        .language-menu__item:hover {
          background: rgba(255, 224, 80, 0.18);
        }

        .inline-utilities {
          display: flex;
          justify-content: flex-end;
          margin-bottom: 16px;
        }

        .search-page-result small {
          display: inline-block;
          margin-bottom: 8px;
          color: var(--brand-strong);
          font-weight: 600;
        }

        .site-footer {
          margin-top: 42px;
          color: rgba(20, 20, 20, 0.8);
          background: #ffffff;
        }

        .footer-shell {
          max-width: var(--content-width);
          margin: 0 auto;
          padding: 36px 40px 28px;
          background: #ffffff;
          font-size: 0.95rem;
        }

        .footer-main {
          display: grid;
          grid-template-columns: 420px minmax(0, 1fr);
          gap: 40px;
          padding-bottom: 22px;
          border-bottom: 1px solid rgba(20, 20, 20, 0.1);
          align-items: start;
        }

        .footer-brand {
          display: flex;
          gap: 14px;
          align-items: flex-start;
          max-width: 100%;
        }

        .footer-brand__logo {
          width: 120px;
          max-height: 36px;
          object-fit: contain;
          filter: none;
          border-radius: 0;
          box-shadow: none;
        }

        .footer-brand__copy h2 {
          margin: 0 0 8px;
          color: var(--accent);
          font-size: inherit;
          line-height: 1.15;
        }

        .footer-brand__copy p,
        .footer-meta p,
        .footer-proof p {
          margin: 0;
          color: rgba(20, 20, 20, 0.62);
          line-height: 1.6;
        }

        .footer-meta p {
          font-size: inherit;
          line-height: 1.45;
        }

        .footer-kicker {
          margin-bottom: 8px !important;
          color: var(--accent) !important;
          font-size: inherit;
          font-weight: 600;
          letter-spacing: 0.08em;
          text-transform: uppercase;
        }

        .footer-app-buttons {
          display: flex;
          gap: 10px;
          flex-wrap: wrap;
          margin-top: 14px;
        }

        .footer-app-button {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          border-radius: 999px;
          padding: 8px 12px;
          color: var(--accent);
          background: rgba(255, 224, 80, 0.3);
          border: 1px solid rgba(20, 20, 20, 0.08);
          font-size: inherit;
          font-weight: 600;
          transition: transform 0.15s ease, box-shadow 0.15s ease, background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease;
        }

        .footer-app-button--desktop {
          background: #ffe35b;
          color: #171717;
          border-color: rgba(20, 20, 20, 0.14);
        }

        .footer-app-button--ipad {
          background: #1d2025;
          color: #fff;
          border-color: #1d2025;
        }

        .footer-app-button--mobile {
          background: #efeff0;
          color: #171717;
          border-color: rgba(20, 20, 20, 0.08);
        }

        .footer-app-button--desktop:hover {
          background: #ffdd3d;
          box-shadow: 0 8px 18px rgba(255, 211, 60, 0.4);
          transform: translateY(-1px);
        }

        .footer-app-button--desktop:active {
          background: #f3d13a;
          transform: translateY(0);
          box-shadow: none;
        }

        .footer-app-button--ipad:hover {
          background: #101216;
          border-color: #101216;
          box-shadow: 0 8px 18px rgba(12, 13, 16, 0.35);
          transform: translateY(-1px);
        }

        .footer-app-button--ipad:active {
          background: #000;
          border-color: #000;
          transform: translateY(0);
          box-shadow: none;
        }

        .footer-app-button--mobile:hover {
          background: #e4e5e8;
          border-color: rgba(20, 20, 20, 0.12);
          box-shadow: 0 8px 18px rgba(20, 20, 20, 0.12);
          transform: translateY(-1px);
        }

        .footer-app-button--mobile:active {
          background: #d9dade;
          transform: translateY(0);
          box-shadow: none;
        }

        .footer-grid {
          display: grid;
          grid-template-columns: repeat(3, minmax(180px, 220px));
          gap: 12px 28px;
          padding: 0;
          justify-content: end;
        }

        .footer-right {
          display: flex;
          justify-content: flex-end;
        }

        .footer-column h3 {
          margin: 0 0 12px;
          color: var(--accent);
          font-size: inherit;
        }

        .footer-column a {
          display: block;
          margin-bottom: 8px;
          color: rgba(20, 20, 20, 0.72);
          font-size: inherit;
        }

        .footer-column a:hover,
        .footer-social:hover {
          color: var(--accent);
        }

        .footer-social:hover {
          background: rgba(255, 224, 80, 0.22);
          border-color: rgba(20, 20, 20, 0.14);
        }

        .footer-bottom {
          padding-top: 28px;
          border-top: 1px solid rgba(20, 20, 20, 0.1);
          display: flex;
          gap: 18px;
          justify-content: space-between;
          align-items: flex-start;
          flex-wrap: wrap;
        }

        .footer-meta {
          max-width: 720px;
          display: grid;
          gap: 4px;
        }

        .footer-legal-links {
          display: flex;
          gap: 28px;
          flex-wrap: wrap;
          margin-top: 2px;
        }

        .footer-legal-links a {
          color: rgba(20, 20, 20, 0.72);
          font-size: inherit;
        }

        .footer-socials {
          display: flex;
          gap: 12px;
          flex-wrap: wrap;
        }

        .footer-utilities {
          display: flex;
          align-items: center;
          gap: 12px;
          flex-wrap: wrap;
        }

        .footer-social {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          width: 44px;
          height: 44px;
          border-radius: 999px;
          color: rgba(20, 20, 20, 0.72);
          border: 1px solid rgba(20, 20, 20, 0.08);
          background: rgba(255, 255, 255, 0.65);
        }

        .footer-social svg {
          width: 24px;
          height: 24px;
        }

        .sr-only {
          position: absolute;
          width: 1px;
          height: 1px;
          padding: 0;
          margin: -1px;
          overflow: hidden;
          clip: rect(0, 0, 0, 0);
          border: 0;
        }

        @media (max-width: 1180px) {
          .doc-shell {
            grid-template-columns: 290px minmax(0, 1fr);
          }

          .toc {
            display: none;
          }
        }

        @media (max-width: 920px) {
          .doc-shell {
            grid-template-columns: 1fr;
          }

          .sidebar {
            position: fixed;
            top: 14px;
            bottom: 14px;
            left: 14px;
            width: min(86vw, 360px);
            z-index: 40;
            transform: translateX(-120%);
            transition: transform 0.2s ease;
          }

          body.nav-open .sidebar {
            transform: translateX(0);
          }

          .sidebar-toggle {
            display: inline-flex;
          }

          .topbar {
            flex-wrap: wrap;
            border-radius: 28px;
          }

          .search-form--inline {
            max-width: none;
            order: 3;
            width: 100%;
          }

          .footer-brand {
            flex-direction: column;
          }

          .topbar-actions {
            width: 100%;
            justify-content: flex-end;
          }

          .landing-topbar {
            flex-direction: column;
            align-items: flex-start;
            gap: 16px;
          }

          .hero-primary-nav {
            justify-content: flex-start;
            gap: 14px;
          }

          .search-form--landing {
            flex-wrap: wrap;
          }

          .search-button--dark {
            width: 100%;
          }

          .browse-row {
            grid-template-columns: 1fr;
            gap: 10px;
          }

          .learning-resources__grid {
            grid-template-columns: 1fr;
          }
        }

        @media (max-width: 640px) {
          .doc-shell,
          .landing-shell,
          .search-shell {
            padding: 16px;
          }

          .article-card,
          .search-page-card {
            padding: 22px;
          }

          .topbar {
            padding: 12px 14px;
          }

          .search-form--hero,
          .search-form--page {
            align-items: stretch;
          }

          .search-button {
            width: 100%;
          }

        .landing-topbar {
            padding: 0;
            gap: 12px;
          }

          .hero-primary-nav {
            gap: 10px 14px;
          }

          .learning-hero__panel {
            text-align: left;
          }

          .landing-hero p {
            margin-left: 0;
            margin-right: 0;
          }

          .popular-strip,
          .popular-links {
            justify-content: flex-start;
          }

          .footer-bottom {
            gap: 14px;
          }

          .footer-shell {
            padding: 26px 16px 22px;
          }
        }

        @media (max-width: 1040px) {
          .footer-main {
            grid-template-columns: 1fr;
            gap: 22px;
          }

          .footer-grid {
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
          }
        }
        """
    )


def build_javascript() -> str:
    return dedent(
        """\
        const BASE_PATH = document.documentElement.dataset.basePath || "";
        const SEARCH_INDEX_URL = `${BASE_PATH}/search-index.json`;

        const state = {
          indexPromise: null,
        };

        function getSearchIndex() {
          if (!state.indexPromise) {
            state.indexPromise = fetch(SEARCH_INDEX_URL).then((response) => response.json());
          }
          return state.indexPromise;
        }

        function normalizeQuery(value) {
          return (value || "").trim().toLowerCase();
        }

        function scoreResult(result, query) {
          const title = result.title.toLowerCase();
          const excerpt = (result.excerpt || "").toLowerCase();
          const section = (result.section || "").toLowerCase();
          let score = 0;
          if (title.includes(query)) score += 6;
          if (title.startsWith(query)) score += 4;
          if (section.includes(query)) score += 3;
          if (excerpt.includes(query)) score += 2;
          return score;
        }

        async function search(query) {
          const normalized = normalizeQuery(query);
          if (!normalized) return [];
          const index = await getSearchIndex();
          return index
            .map((entry) => ({ ...entry, score: scoreResult(entry, normalized) }))
            .filter((entry) => entry.score > 0)
            .sort((a, b) => b.score - a.score || a.title.localeCompare(b.title))
            .slice(0, 8);
        }

        function attachSearchSuggestions() {
          const forms = document.querySelectorAll(".search-form");
          forms.forEach((form) => {
            const input = form.querySelector("[data-search-input]");
            const results = form.querySelector("[data-search-results]");
            if (!input || !results) return;

            input.addEventListener("input", async () => {
              const query = input.value.trim();
              if (query.length < 2) {
                results.classList.remove("is-visible");
                results.innerHTML = "";
                return;
              }

              const matches = await search(query);
              if (!matches.length) {
                results.classList.remove("is-visible");
                results.innerHTML = "";
                return;
              }

              results.innerHTML = matches
                .map(
                  (match) => `
                    <a class="search-result-item" href="${match.url}">
                      <strong>${match.title}</strong>
                      <span>${match.langLabel}${match.section ? " · " + match.section : ""}</span>
                    </a>
                  `
                )
                .join("");
              results.classList.add("is-visible");
            });

            document.addEventListener("click", (event) => {
              if (!form.contains(event.target)) {
                results.classList.remove("is-visible");
              }
            });
          });
        }

        function attachSearchPageResults() {
          const container = document.querySelector("[data-search-page-results]");
          if (!container) return;
          const params = new URLSearchParams(window.location.search);
          const initialQuery = params.get("q") || "";
          const input = document.querySelector("[data-search-input]");
          if (input) input.value = initialQuery;

          const render = async (query) => {
            const normalized = normalizeQuery(query);
            if (!normalized) {
              container.innerHTML = '<p class="toc-empty">Enter a few keywords to search the Evoto help center.</p>';
              return;
            }

            const matches = await search(normalized);
            if (!matches.length) {
              container.innerHTML = '<p class="toc-empty">No results matched this query. Try broader product or feature keywords.</p>';
              return;
            }

            container.innerHTML = matches
              .map(
                (match) => `
                  <a class="search-page-result" href="${match.url}">
                    <small>${match.langLabel}${match.section ? " · " + match.section : ""}</small>
                    <strong>${match.title}</strong>
                    <p>${match.excerpt || "Open this article."}</p>
                  </a>
                `
              )
              .join("");
          };

          render(initialQuery);
        }

        function attachLanguageSwitcher() {
          document.querySelectorAll("[data-language-switch]").forEach((select) => {
            select.addEventListener("change", () => {
              if (select.value) {
                window.location.href = select.value;
              }
            });
          });
        }

        function attachSidebarToggle() {
          document.querySelectorAll("[data-sidebar-open]").forEach((button) => {
            button.addEventListener("click", () => document.body.classList.add("nav-open"));
          });
          document.querySelectorAll("[data-sidebar-close]").forEach((button) => {
            button.addEventListener("click", () => document.body.classList.remove("nav-open"));
          });
        }

        function attachPrimaryNavDropdownExclusive() {
          const nav = document.querySelector(".hero-primary-nav");
          if (!nav) return;
          const dropdowns = nav.querySelectorAll("details.primary-nav-dropdown");
          dropdowns.forEach((details) => {
            details.addEventListener("toggle", () => {
              if (!details.open) return;
              dropdowns.forEach((other) => {
                if (other !== details) other.open = false;
              });
            });
          });
          document.addEventListener("click", (event) => {
            if (!nav.contains(event.target)) {
              dropdowns.forEach((d) => {
                d.open = false;
              });
              return;
            }
            if (!event.target.closest("details.primary-nav-dropdown")) {
              dropdowns.forEach((d) => {
                d.open = false;
              });
            }
          });
        }

        function normalizePathname(pathname) {
          let p = pathname.replace(/\\/index\\.html?$/i, "");
          p = p.replace(/\\/+$/, "");
          return p || "/";
        }

        function learningCenterHrefMatchesCurrentPage(href) {
          if (!href) return false;
          const resolved = new URL(href, window.location.href);
          return normalizePathname(resolved.pathname) === normalizePathname(window.location.pathname);
        }

        function attachLearningCenterHomeNavGuard() {
          document.querySelectorAll("a.primary-nav-dropdown__item--current").forEach((anchor) => {
            anchor.addEventListener("click", (event) => {
              const href = anchor.getAttribute("href");
              if (learningCenterHrefMatchesCurrentPage(href)) {
                event.preventDefault();
              }
            });
          });
        }

        function init() {
          attachSearchSuggestions();
          attachSearchPageResults();
          attachLanguageSwitcher();
          attachSidebarToggle();
          attachPrimaryNavDropdownExclusive();
          attachLearningCenterHomeNavGuard();
        }

        document.addEventListener("DOMContentLoaded", init);
        """
    )


def build_favicon() -> str:
    return dedent(
        """\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
          <defs>
            <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#cf6e43"/>
              <stop offset="100%" stop-color="#0b6b63"/>
            </linearGradient>
          </defs>
          <rect width="64" height="64" rx="18" fill="#f8f2e8"/>
          <path d="M18 18h28v8H27v10h16v8H27v10h-9z" fill="url(#g)"/>
        </svg>
        """
    )


if __name__ == "__main__":
    main()
