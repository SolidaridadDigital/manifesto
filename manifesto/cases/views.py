from models import Case, CaseForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

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
