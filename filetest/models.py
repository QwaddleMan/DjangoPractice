from django.db import models
from django.forms import ModelForm

class NiftiFile(models.Model):
    upload = models.FileField(upload_to="uploads/")

class NiftiFileForm(ModelForm):
    class Meta:
        model = NiftiFile
        fields = ['upload']
