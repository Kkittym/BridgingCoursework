from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class CV(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.TextField()

    def __str__(self):
        return (self.name + "'s CV")
    
    def getType(self):
        return "cv"

class Section(models.Model):
    CV = models.ForeignKey('CV.CV', on_delete=models.CASCADE, related_name='sections')
    title = models.TextField()

    def __str__(self):
        return self.title

    def getType(self):
        return "section"

class Institute(models.Model):
    section = models.ForeignKey('CV.Section', on_delete=models.CASCADE, related_name='institutes')
    start = models.TextField()
    end = models.TextField()
    location = models.TextField()
    area = models.TextField()

    def __str__(self):
        return self.location

    def getType(self):
        return "institute"

class SectionElement(models.Model):
    section = models.ForeignKey('CV.Section', on_delete=models.CASCADE, related_name='elements')
    text = models.TextField()

    def __str__(self):
        return ("Element for section: " + self.section.__str__() + ", text: " + self.text)
    
    def getType(self):
        return "Section element"

class InstituteElement(models.Model):
    institute = models.ForeignKey('CV.Institute', on_delete=models.CASCADE, related_name='elements')
    text = models.TextField()

    def __str__(self):
        return ("Element for section: " + self.institute.__str__() + ", text: " + self.text)
    
    def getType(self):
        return "Institute element"