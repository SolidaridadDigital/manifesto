from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from signers.models import SignerProfile

admin.site.unregister(User)

class SignerProfileInline(admin.StackedInline):
    model = SignerProfile

class CamposExtras(UserAdmin):
    inlines = [SignerProfileInline]
 

#admin modificado para que se puedan ver los campos de signer profile en el admin
admin.site.register(User, CamposExtras)