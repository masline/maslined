from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
	url(r'^', include('store.urls', namespace='store')),
    url(r'^admin/', include(admin.site.urls)),
) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
