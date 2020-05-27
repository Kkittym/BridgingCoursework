from django.test import TestCase

# Create your tests here.

from django.urls import resolve
from django.http import HttpRequest

from CV.views import main

class HomePageTest(TestCase):

    def test_cv_url_resolves_to_main_view(self):
        found = resolve('/cv')  
        self.assertEqual(found.func, main)

    def test_uses_home_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'main.html')

