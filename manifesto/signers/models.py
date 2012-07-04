from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class SignerProfile(models.Model):
    # usuario con el que se relaciona 1 a 1
    user = models.OneToOneField(User)
    # comentario agregado al firmar el manifiesto
    comment = models.TextField(blank=True)
    # pais del firmante
    country = models.CharField(max_length=30)
    # boolean para saber si el firmante quiere recibir mails del sitio
    suscribed = models.BooleanField(default=False)

    # metodo que dice como se vera el signer en el admin
    def __unicode__(self):
        return self.user.first_name

# metodo que crea y asocia un signer profile cada vez que se crea un usuario
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SignerProfile.objects.create(user=instance)
    
# se llama al metodo anterior despues que el usuario fue guardado en la base de datos
post_save.connect(create_user_profile, sender=User)