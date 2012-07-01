#-*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from allauth.account.forms import SignupForm
from signers.models import SignerProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
import csv

def index(request):
    with open('/home/chileagil/manifesto/app/utilidades/iso3166.csv', 'rb') as file_countries:
        countries = [(row['Code'], row['English']) for row in csv.DictReader(file_countries)]
    countries2 = []    
    for country in countries:
        countries2.append(country[1])

    return render_to_response('index.html', {'form': SignupForm(),'countries':countries2}, context_instance = RequestContext(request))

def all_signers(request):
    users = User.objects.filter(is_active=True).order_by('-date_joined')
    return render_to_response('signers.html', {'users': users}, context_instance = RequestContext(request))

def email_unique(request):
    if request.is_ajax():
        if request.method == 'GET':
            email = request.GET['email']
            if exist_email(email):
                return HttpResponse("false")
    return HttpResponse("true")

def exist_email(email):
    try:
        User.objects.get(email=email)
        return True
    except Exception:
        return False
