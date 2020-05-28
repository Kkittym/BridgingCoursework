from django.urls import path
from . import views

urlpatterns = [
    path('cv', views.main, name='cv'),
    path('cv/new', views.CV_new, name='cv_new'),
    path('cv/section', views.section_new, name='section_new'),
]