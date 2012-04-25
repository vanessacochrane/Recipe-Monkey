#Recipe Monkey

Recipe Monkey is a django kitchen management system.  Please see the [main site](http://vanessacochrane.github.com/Recipe-Monkey/) for full documentation.


##Installation

settings.py

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'recipemonkey.search_sites'
HAYSTACK_WHOOSH_PATH = '/usr/local/web/django/www/production/recipemonkey/whoosh_index/'


INSTALLED_APPS = INSTALLED_APPS + ('haystack', 'taggit','tastypie','django_tables2')

search_sites.py

import haystack
haystack.autodiscover()
