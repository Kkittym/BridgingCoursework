from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page  

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/to-do')  
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/to-do')
        self.assertTemplateUsed(response, 'home.html')