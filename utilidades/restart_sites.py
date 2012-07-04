from django.contrib.sites.models import Site

# datos de los sitios para desarrollo y produccion
# esto es para que al mandar los mails de confirmacion las URL sean correctas
name_develop = 'Solidaridad Digital Desarrollo'
domain_develop = 'localhost:8000'
name_production = 'Solidaridad Digital'
domain_production = 'www.digitalsolidarity.org'


try: # si existe un sitio con id=1 en la base de datos se modifica con los datos de produccion
    site = Site.objects.get(pk=1)
    site.name = name_production
    site.domain = domain_production
    site.save()
except Exception: # si no existe se crea un nuevo sitio
    Site.objects.create(id=1,name=name_production,domain=domain_production)
try: # si existe un sitio con id=2 en la base de datos se modifica con los datos de desarrollo
    site = Site.objects.get(pk=2)
    site.name = name_develop
    site.domain = domain_develop
    site.save()
except Exception: # si no existe se crea un nuevo sitio
    Site.objects.create(id=2,name=name_develop,domain=domain_develop)