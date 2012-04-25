"""
API
"""
from django.conf.urls.defaults import *

from tastypie.api import Api
from recipemonkeyapp.api import *

v1_api = Api(api_name='v1')
v1_api.register(SourceResource(), canonical=True)
v1_api.register(RecipeResource(), canonical=True)

urlpatterns = patterns('',
    (r'^', include(v1_api.urls)),
)
