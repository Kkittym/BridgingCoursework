from django.urls import path
from . import views

urlpatterns = [
    path('to-do', views.home_page, name='home'),
]