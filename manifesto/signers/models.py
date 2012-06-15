from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class SignerProfile(models.Model):
  user = models.OneToOneField(User)
  comment = models.TextField(blank=True)
  country = models.CharField(max_length=30)
  suscribed = models.BooleanField(default=False)
  
  def __unicode__(self):
    return self.user.first_name

def create_user_profile(sender, instance, created, **kwargs):
  if created:
    SignerProfile.objects.create(user=instance)
    
post_save.connect(create_user_profile, sender=User)
