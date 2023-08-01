from django.urls import path
from .import views as v
urlpatterns = [
    path("",v.home,name="home"),
    path("about",v.about,name="about"),
    path("contact",v.contact,name="contact"),
    path("reg",v.register,name="register"),
    path("login",v.loginn,name="login"),
    path("logout",v.logoutt,name="logout")
]