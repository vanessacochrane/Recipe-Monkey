from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.conf import settings

urlpatterns = patterns('recipemonkeyapp.views.views',

    (r'^$','index'),
 #   (r'^barcode/(?P<code>\d+)/$', 'barcodeimg'),
    (r'^barcodes/$', 'barcodes'),
    (r'^scan/(?P<id>\d+)/$', 'scan'),
    (r'^ajax_object_request/$', 'ajax_object_request'),
    (r'^notifications/near_expiry/$', 'send_expiry_notifications'),
	(r'^search/$', 'search'),

)

urlpatterns += patterns('recipemonkeyapp.views.recipe',
	url(r'^recipe/(?P<recipe_id>\d+)/$', 'detail',name='recipe_detail'),
	url(r'^recipe/cook/(?P<recipe_id>\d+)/$', 'cook',name='recipe_cook'),
	url(r'^recipe/add_to_shopping/(?P<recipe_id>\d+)/$', 'add_to_shopping',name='recipe_add_to_shopping'),
	(r'^recipe/$', 'index'),
	(r'^recipe/(?P<id>\d+)/barcode.png/$', 'barcodeimg'),
	(r'^recipe/scan/(?P<id>\d+)/$', 'scan'),
	
)

urlpatterns += patterns('recipemonkeyapp.views.planner',
	(r'^planner/(?P<year>\d+)/(?P<month>\d+)/$', 'calendar'),
	(r'^planner/schedule/(?P<weeknum>\d+)/(?P<startdate>\d+)/$', 'schedule'),
)


urlpatterns += patterns('recipemonkeyapp.views.groceryitem',
    (r'^groceryitem/$', 'index'),
    (r'^groceryitem/labels/$', 'labels'),

	url(r'^groceryitem/(?P<id>\d+)/$', 'detail',name='groceryitem_detail'),
	(r'^groceryitem/(?P<id>\d+)/barcode.png/$', 'barcodeimg'),
	(r'^groceryitem/scan/(?P<id>\d+)/$', 'scan'),
)

urlpatterns += patterns('recipemonkeyapp.views.storage',
	(r'^storage/$', 'index'),
	
)

urlpatterns += patterns('',
   (r'^api/', include('recipemonkeyapp.api.urls')),
)


