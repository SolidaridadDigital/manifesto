#-*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from allauth.account.forms import SignupForm
from signers.models import SignerProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
import csv


def index(request):
    # se abre el archivo con los datos de los paises
    with open('../utilidades/iso3166.csv', 'rb') as file_countries:
        countries = [(row['Code'], row['English']) for row in csv.DictReader(file_countries)] # se obtiene el codigo y el nombre del pais en ingles
    countries2 = []
    for country in countries:
        countries2.append(country[1]) # se agregan los nombres de los paises en la lista
    # se retorna un response para que renderize index.html y se agrega al contexto el formulario para firmar y la lista de paises
    return render_to_response('index.html', {'form': SignupForm(),'countries':countries2}, context_instance = RequestContext(request))

def all_signers(request):
    # se obtienen todos los firmantes ordenado por la fecha en que firmaron
    users = User.objects.filter(is_active=True).order_by('-date_joined')
    # se agregan los firmantes al contexto
    return render_to_response('signers.html', {'users': users}, context_instance = RequestContext(request))

# si el mail del formulario de firmante esa usado retorna false, si no, true
def email_unique(request):
    if request.is_ajax():
        if request.method == 'GET':
            email = request.GET['email']
            if exist_email(email):
                return HttpResponse("false")
    return HttpResponse("true")

# busca en la base de datos si existe un usuario que tenga usado el email
def exist_email(email):
    try:
        User.objects.get(email=email)
        return True
    except Exception:
        return False
