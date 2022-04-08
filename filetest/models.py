from django.db import models
from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import magic

class MultiContrastFiles(models.Model):
    T1 = models.FileField(upload_to="uploads/")
    T1C = models.FileField(upload_to="uploads/")
    T2 = models.FileField(upload_to="uploads/")
    FLAIR = models.FileField(upload_to="uploads/")


class NiftiFileForm(ModelForm):
    T1 = forms.FileField(required=True, label="T1")
    T1C = forms.FileField(required=True, label="T1C")
    T2 = forms.FileField(required=True, label="T2")
    FLAIR = forms.FileField(required=True, label="FLAIR")

#    def clean_upload(self):
#        file = self.cleaned_data.get("upload")
#        filetype = magic.from_buffer(file.read())
#        print(filetype)
#        return file

    class Meta:
        model = MultiContrastFiles
        fields = ['T1', 'T1C', 'T2', 'FLAIR']

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Mets:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email'] # note: user.email != email.
        if commit:
            user.save()
        return user

class UserLoginForm(Form):
    username = forms.CharField(max_length=200, label="username")
    password = forms.CharField(max_length=200, widget=forms.PasswordInput,
                                label="password")
