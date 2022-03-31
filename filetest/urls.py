from django.urls import path
from . import views

app_name = "filetest"
urlpatterns = [
    path('', views.index, name="index"),
]
