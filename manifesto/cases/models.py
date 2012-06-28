from django.db import models
from signers.models import SignerProfile
from django.forms import ModelForm

class Case(models.Model):
  user = models.ForeignKey(SignerProfile)
  title = models.CharField(max_length=80)
  description = models.TextField(blank = True)
  case_date = models.DateTimeField()
  publish_date = models.DateTimeField()
  
  def __unicode__(self):
    return self.title
    
class CaseForm(ModelForm):
  class Meta:
    model = Case
    exclude = ('user', 'publish_date')

