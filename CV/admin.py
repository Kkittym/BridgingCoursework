from django.contrib import admin
from .models import CV, Section, Institute, SectionElement, InstituteElement

# Register your models here.

admin.site.register(CV)
admin.site.register(Section)
admin.site.register(Institute)
admin.site.register(SectionElement)
admin.site.register(InstituteElement)