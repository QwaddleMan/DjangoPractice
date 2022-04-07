from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from .models import NiftiFile, NiftiFileForm, UserLoginForm, NewUserForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = NiftiFileForm(request.POST, request.FILES)
        if form.is_valid():
            nifti_file = form.save()
            return HttpResponseRedirect(reverse("filetest:index"))
    else:
        form = NiftiFileForm()
    return render(request, "filetest/index.html", {'form': form})

def login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
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
