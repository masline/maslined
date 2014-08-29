from django.conf.urls import patterns, url

urlpatterns = patterns('store.views',
	url(r'^$', 'index', name='index'),
	url(r'^(services|about|news)$', 'other', name='other'),
	url(r'^linecard$', 'linecard', name='linecard'),
	url(r'^contact$', 'contact', name='contact'),
	url(r'^catalog$', 'catalog', name='catalog'),
	url(r'p/([^/]*)$', 'product', name='product')
)