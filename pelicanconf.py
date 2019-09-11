#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pat McCavana'
SITENAME = 'Rath-Jam-Beau Notebook'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'En'
THEME = 'blue-penguin'
MARKUP = ('md', 'ipynb')


PLUGIN_PATHS = ['./plugins']

PLUGINS = [
    'pelican-ipynb.markup',
    'sitemap' ] 

# Configuration for the "sitemap" plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}

#PLUGINS = [
#    'i18n_subsites',
#    'series',
#    'tag_cloud',
#    'liquid_tags.youtube',
#    'liquid_tags.notebook',
#    'liquid_tags.include_code',
#    'render_math',
#    'pelican-ipynb.markup' ] 


IGNORE_FILES = [".ipynb_checkpoints"]

IPYNB_USE_METACELL = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DISQUS_SITENAME = 'pmccavana-github-io'

GOOGLE_ANALYTICS = 'UA-146513153-1'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True