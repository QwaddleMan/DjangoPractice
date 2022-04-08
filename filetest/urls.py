from django.urls import path
from . import views

app_name = "filetest"
urlpatterns = [
    path('', views.index, name="index"),
#    path('login/', views.ftlogin, name="login"),
#    path('register/', views.register, name="register"),
#    path('logout/', views.ftlogout, name="logout"),
]
