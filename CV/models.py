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

class Section(models.Model):
    CV = models.ForeignKey('CV.CV', on_delete=models.CASCADE, related_name='sections')
    title = models.TextField()

    def __str__(self):
        return self.title

class Institute(models.Model):
    start = models.TextField()
    end = models.TextField()
    location = models.TextField()
    area = models.TextField()

class Element(models.Model):
    section = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='elements')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('section', 'object_id')
    text = models.TextField()

    def __str__(self):
        return ("Element for section: " + self.section.__str__() + ", text: " + self.text)