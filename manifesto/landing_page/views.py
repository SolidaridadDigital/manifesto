from django.shortcuts import render_to_response
from django.template import RequestContext
from allauth.account.forms import SignupForm
from signers.models import SignerProfile
from django.contrib.auth.models import User

def index(request):
	users = User.objects.all().order_by('-date_joined')[:3]
	return render_to_response('index.html', {'form': SignupForm(), 'users': users}, context_instance = RequestContext(request))

def all_signers(request):
	users = User.objects.all().order_by('-date_joined')
	return render_to_response('signers.html', {'users': users}, context_instance = RequestContext(request))