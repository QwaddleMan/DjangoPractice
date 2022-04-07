from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import NiftiFile, NiftiFileForm

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
