from models import Case, CaseForm
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext
import json
from math import ceil

def case_submit(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CaseForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            if not request.user.is_anonymous():
                user = request.user.get_profile()
            else:
                return HttpResponseRedirect('/accounts/login')
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            case_date = form.cleaned_data['case_date']
            publish_date = timezone.now()
            Case.objects.create(user=user, title=title, description=description, case_date=case_date, publish_date=publish_date)
            return HttpResponseRedirect('/') # Redirect after POST
        
    else:
        if request.user.is_anonymous():
            return HttpResponseRedirect('/accounts/login')
        form = CaseForm() # An unbound form

    return render(request, 'case_submit.html', {
        'form': form,
    })
# $.post('http://localhost:8000/cases/list', {n_page: 1 , 'csrfmiddlewaretoken': 'zpy3KJ9vXuVoBDP8Xgtm52cARj8r9IzN'}, function(){alert("exito")});
def all_cases(request):
    cases = Case.objects.all().order_by('-publish_date')
    L = []
    for case in cases:
      L.append({'title': case.title, 'content': case.description, 'date': str(case.case_date)})
    if request.method == 'POST':
      n_page = int(request.POST['n_page'])
      sublist = L[int(((n_page+1) % ceil(len(L)/6.0)) * 6) : int(((n_page+1) % ceil(len(L)/6.0)) * 6) + 6]
    else:
      sublist = L
    s = json.dumps(sublist)
    return render_to_response('cases_list.html', {'cases': s}, context_instance = RequestContext(request))
