from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'views.index', name = 'index'),
)
