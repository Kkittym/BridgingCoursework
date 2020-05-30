from django.urls import path
from . import views

urlpatterns = [
    path('cv', views.main, name='cv'),
    path('cv/new', views.CV_new, name='cv_new'),
    path('cv/<int:pk>/new_section', views.add_section, name="add_section"),
    path('cv/edit_section/<int:pk>', views.edit_section, name="edit_section"),
    path('cv/edit_section/<int:secpk>/institute', views.add_institute, name="add_institute"),
    path('cv/edit_section/<int:secpk>/edit_institute/<int:instpk>', views.edit_institute, name="edit_institute"),
    path('cv/edit_section/<int:secpk>/remove_institute/<int:instpk>', views.remove_institute, name="remove_institute"),
    path('cv/edit_section/<int:secpk>/remove_element/<int:elepk>', views.remove_element_from_section, name="remove_element_from_section"),
    path('cv/edit_section/<int:secpk>/edit_institute/<int:instpk>/remove_element/<int:elepk>', views.remove_element_from_institute, name="remove_element_from_institute"),
]