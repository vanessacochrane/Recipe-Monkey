from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication,OAuthAuthentication
from piston.doc import documentation_view

from handlers import RecipeHandler

#auth = OAuthAuthentication()
#ad = { 'authentication': auth }
ad={}
recipe_resource = Resource(handler=RecipeHandler, **ad)
#arbitrary_resource = Resource(handler=ArbitraryDataHandler, **ad)

urlpatterns = patterns('',

    url(r'^recipe/$', recipe_resource), 

    url(r'^recipe/(?P<recipe_id>[^/]+)/$', recipe_resource), 
    
    # automated documentation
        url(r'^$', documentation_view),
)

urlpatterns += patterns(
    'piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token'),
)
