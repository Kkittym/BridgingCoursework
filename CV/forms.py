from django import forms
from django.forms import Textarea
from .models import CV, Section, Element, Institute

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('name', 'phone', 'email',)
        widgets = {
            'name': Textarea(attrs={'cols':80, 'rows':1}),
            'email': Textarea(attrs={'cols':80, 'rows':1}),
        }
    
    def getType(self):
        return "cvform"

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('title',)
        widgets = {
            'title': Textarea(attrs={'cols':80, 'rows':1})
        }
    
    def getType(self):
        return "sectionform"

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'cols':80, 'rows':1}),
        }

    def getType(self):
        return "elementform"

class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ('start', 'end', 'location', 'area')
        widgets = {
            'start': Textarea(attrs={'cols':80, 'rows':1}),
            'end': Textarea(attrs={'cols':80, 'rows':1}),
            'location': Textarea(attrs={'cols':80, 'rows':1}),
            'area': Textarea(attrs={'cols':80, 'rows':1}),
        }
    
    def getType(self):
        return "instituteform"