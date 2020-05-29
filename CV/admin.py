from django.contrib import admin
from .models import CV, Section, Institute, Element

# Register your models here.

admin.site.register(CV)
admin.site.register(Section)
admin.site.register(Institute)
admin.site.register(Element)