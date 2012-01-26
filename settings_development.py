from recipemonkey.settings import *

DEBUG = True

MEDIA_ROOT = 'media'
STATIC_ROOT = 'static'

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'recipemonkey.search_sites'
HAYSTACK_WHOOSH_PATH = './whoosh_index/'


INSTALLED_APPS = INSTALLED_APPS + ('haystack',)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'recipemonkey.db'
