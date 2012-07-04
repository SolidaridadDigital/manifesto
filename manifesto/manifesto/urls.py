from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'holamundo.views.index', name="index"),
    # URL para que funcione la internacionalizacion
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # incluye las URLS de landing_page
    url(r'^', include('landing_page.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # URLS para el manejo de cuentas (enviar mail de confirmacion, validar usuarios, etc...)
    url(r'^accounts/', include('allauth.urls')),
)
