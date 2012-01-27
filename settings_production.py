from recipemonkey.settings import *

DEBUG = True

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'recipemonkey.search_sites'
HAYSTACK_WHOOSH_PATH = '/usr/local/web/django/www/production/recipemonkey/whoosh_index/'


INSTALLED_APPS = INSTALLED_APPS + ('haystack',)
STATIC_ROOT = '/usr/local/web/django/www/production/recipemonkey/static'
MEDIA_ROOT = '/usr/local/web/django/www/production/recipemonkey/media'
TEMPLATE_DIRS = ('/usr/local/web/django/www/production/recipemonkey/recipemonkeyapp/templates')

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'recipemonkey'             # Or path to database file if using sqlite3.
DATABASE_USER = 'recipemonkey'             # Not used with sqlite3.
DATABASE_PASSWORD = 'recipemonkey'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

