# Here are the urls.
from django.urls import path
from . import views # The period stands for right here.

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]
