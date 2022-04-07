from django.db import models
from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import magic

class NiftiFile(models.Model):
    upload = models.FileField(upload_to="uploads/")

class NiftiFileForm(ModelForm):

    def clean_upload(self):
        file = self.cleaned_data.get("upload")
        filetype = magic.from_buffer(file.read())
        print(filetype)
        return file

    class Meta:
        model = NiftiFile
        fields = ['upload']

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
