from django.shortcuts import render_to_response
from django.template import RequestContext
from allauth.account.forms import SignupForm


def index(request):
    return render_to_response('index.html', {'form': SignupForm()}, context_instance = RequestContext(request))
