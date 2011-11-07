from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

(r'^$',include('recipemonkeyapp.urls')),

(r'^recipemonkeyapp/', include('recipemonkeyapp.urls')),

(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    )




