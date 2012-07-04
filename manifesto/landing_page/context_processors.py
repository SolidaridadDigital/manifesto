from django.contrib.auth.models import User

# envia los ultimos 15 firmantes en el request.context para que esten disponibles en todas las paginas
def last_three_signers(request):
    users = User.objects.filter(is_active=True).order_by('-date_joined')[:15]
    return {'users': users}