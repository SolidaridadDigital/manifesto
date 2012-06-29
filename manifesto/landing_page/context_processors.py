from django.contrib.auth.models import User

def last_three_signers(request):
    users = User.objects.filter(is_active=True).order_by('-date_joined')[:15]
    return {'users': users}