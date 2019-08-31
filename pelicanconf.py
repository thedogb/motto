#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '旁白'
SITENAME = 'Motto'
SITESUBTITLE = ''
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {"en": "%b/%d/%Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "true"},
    }
}

PLUGIN_PATHS = ["plugins/pelican-plugins"]
PLUGINS = [
    "extract_toc",
    "just_table",
    "liquid_tags.img",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

DEFAULT_LANG = 'zh'
THEME = 'theme/elegant'
TYPOGRIFY = True
DEFAULT_PAGINATION = False

DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = "Motto"
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"

SLUGIFY_SOURCE = 'basename' # 使用文件名作为url


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

# Social widget
SOCIAL = (
        ('Github', '#'),
        ('RSS', SITEURL + '/feeds/all.atom.xml'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Landing Page

LANDING_PAGE_TITLE = "Welcom to Motto!!"

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
SHARE_POST_INTRO = "Like this post? Share on:"

