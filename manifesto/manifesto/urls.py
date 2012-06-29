from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'holamundo.views.index', name="index"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('landing_page.urls')),
    url(r'^cases/list', 'cases.views.all_cases', name="all_cases"),
    url(r'^cases/', 'cases.views.case_submit', name="case_submit"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
)
