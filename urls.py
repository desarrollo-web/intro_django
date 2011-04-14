from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^snippets$', 'pastebin.views.manage', name='snippet_list'),
    url(r'^snippets/new$', 'pastebin.views.create', name='snippet_create'),
    url(r'^snippets/(?P<snippet_id>\d+)$', 'pastebin.views.show', name='snippet_show'),
)
