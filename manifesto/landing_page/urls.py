from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # url del index
    url(r'^$', views.index, name = 'index'),
    # url no usada, anteriormente iba a una vista que mostraba todos los signers
    url(r'^all_signers/$', views.all_signers, name = 'all_signers'),
    # url para revisar via AJAX que el mail ingresado por un usuario no este usado
    url(r'^email_unique/$', views.email_unique, name = 'email_unique'),
)
