from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^all_signers/$', views.all_signers, name = 'all_signers'),
    url(r'^email_unique/$', views.email_unique, name = 'email_unique'),
)
