from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.conf import settings

urlpatterns = patterns('recipemonkeyapp.views.views',

(r'^$','index'),

)

urlpatterns += patterns('recipemonkeyapp.views.recipe',
	(r'^recipe/(?P<recipe_id>\d+)/$', 'detail'),
	(r'^recipe/$', 'index'),
	(r'^recipe/(?P<id>\d+)/barcode.png/$', 'barcodeimg'),
	(r'^recipe/scan/(?P<id>\d+)/$', 'scan'),
	
)

urlpatterns += patterns('recipemonkeyapp.views.planner',
	(r'^planner/(?P<planner_id>\d+)/$', 'calendar'),
)


urlpatterns += patterns('recipemonkeyapp.views.groceryitem',
    (r'^groceryitem/$', 'index'),
    (r'^groceryitem/labels/$', 'labels'),

	(r'^groceryitem/(?P<id>\d+)/$', 'detail'),
	(r'^groceryitem/(?P<id>\d+)/barcode.png/$', 'barcodeimg'),
	(r'^groceryitem/scan/(?P<id>\d+)/$', 'scan'),
)

urlpatterns += patterns('recipemonkeyapp.views.storage',
	(r'^storage/$', 'index'),
	
)


