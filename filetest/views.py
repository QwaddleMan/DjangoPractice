from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MultiContrastFiles, NiftiFileForm, UserLoginForm, NewUserForm
from .test import load_data

# changed origin to use ssh. this is a test.
# Create your views here.
#@login_required(login_url='/filetest/login')
def index(request):
    if request.method == "POST":
        form = NiftiFileForm(request.POST, request.FILES)
        if form.is_valid():
#            niftis = form.save(commit=False)
            load_data(form.cleaned_data['T2'].temporary_file_path())
            return HttpResponseRedirect(reverse("filetest:index"))
    else:
        form = NiftiFileForm()
    return render(request, "filetest/index.html", {'form': form})

def ftlogin(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("filetest:index"))
    return render(request, "filetest/login.html", context = {"form":form})

def register(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful.")
        return HttpResponseRedirect(reverse("filetest:index"))
    return render(request, "filetest/register.html", context = {"form":form})

def ftlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("filetest:login"))
