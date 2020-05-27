from django.test import TestCase

from django.urls import resolve
from django.http import HttpRequest
from django.contrib.auth.models import User

from CV.views import main

class HomePageTest(TestCase):

    def test_cv_url_resolves_to_main_view(self):
        found = resolve('/cv')  
        self.assertEqual(found.func, main)

    def test_uses_home_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'main.html')

    def test_education_on_page(self):
        response = self.client.get('/cv')
        self.assertIn('Education', response.content.decode())

    def test_work_experience_on_page(self):
        response = self.client.get('/cv')
        self.assertIn('Work Experience', response.content.decode())

    def test_other_skills_on_page(self):
        response = self.client.get('/cv')
        self.assertIn('Other Skills', response.content.decode())

class AdminTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser()

