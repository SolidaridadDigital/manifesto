from django.contrib.sites.models import Site

name_develop = 'Solidaridad Digital Desarrollo'
domain_develop = 'localhost:8000'
name_production = 'Solidaridad Digital'
domain_production = 'www.digitalsolidarity.org'

try:
    site = Site.objects.get(pk=1)
    site.name = name_production
    site.domain = domain_production
    site.save()
except Exception:
    Site.objects.create(id=1,name=name_production,domain=domain_production)
try:
    site = Site.objects.get(pk=2)
    site.name = name_develop
    site.domain = domain_develop
    site.save()
except Exception:
    Site.objects.create(id=2,name=name_develop,domain=domain_develop)
