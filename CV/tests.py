from django.test import TestCase

from django.urls import resolve
from django.http import HttpRequest
from django.contrib.auth.models import User

from CV.views import main, CV_new
from CV.models import CV, Section, Institute, SectionElement, InstituteElement

class HomePageTest(TestCase):

    def test_cv_url_resolves_to_main_view(self):
        found = resolve('/cv')  
        self.assertEqual(found.func, main)

    def test_uses_main_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'main.html')

    def test_cv_appears_on_page(self):
        CV.objects.create(name='Test Test', phone='12345678910', email='test.test@test.com')
        self.assertEqual(CV.objects.count(), 1)

        response = self.client.get('/cv')

        self.assertIn('Test Test', response.content.decode())
        self.assertIn('12345678910', response.content.decode())
        self.assertIn('test.test@test.com', response.content.decode())

    def test_section_appears_on_page(self):
        CV.objects.create(name='Test Test', phone='12345678910', email='test.test@test.com')
        Section.objects.create(CV=CV.objects.first(), title="SectionTest")

        response = self.client.get('/cv')

        self.assertIn('SectionTest', response.content.decode())

    def test_institute_appears_on_page(self):
        CV.objects.create(name='Test Test', phone='12345678910', email='test.test@test.com')
        Section.objects.create(CV=CV.objects.first(), title="Test")
        Institute.objects.create(section=Section.objects.first(), start='NowStart', end='NowEnd', location='Institute', area='Institute Test')

        response = self.client.get('/cv')

        self.assertIn('NowStart', response.content.decode())
        self.assertIn('NowEnd', response.content.decode())
        self.assertIn('Institute', response.content.decode())
        self.assertIn('Institute Test', response.content.decode())

    def test_section_element_appears_on_page(self):
        CV.objects.create(name='Test Test', phone='12345678910', email='test.test@test.com')
        Section.objects.create(CV=CV.objects.first(), title="Test")
        SectionElement.objects.create(section=Section.objects.first(), text="This is a section element test")

        response = self.client.get('/cv')

        self.assertIn('This is a section element test', response.content.decode())

    def test_institute_element_appears_on_page(self):
        CV.objects.create(name='Test Test', phone='12345678910', email='test.test@test.com')
        Section.objects.create(CV=CV.objects.first(), title="Test")
        Institute.objects.create(section=Section.objects.first(), start='Test', end='Test', location='Test', area='Test')
        InstituteElement.objects.create(institute=Institute.objects.first(), text="This is a institute element test")

        response = self.client.get('/cv')

        self.assertIn('This is a institute element test', response.content.decode())

    def test_add_section_button_not_on_page(self):
        response = self.client.get('/cv')
        self.assertNotIn('Add section', response.content.decode())

class UnauthedUserTest(TestCase):

    def test_new_cv_url_redirects_login(self):
        response = self.client.get('/cv/new')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/accounts/login/?next=/cv/new')

    def test_new_section_url_redirects_login(self):
        response = self.client.get('/cv/1/new_section')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/accounts/login/?next=/cv/1/new_section')

class NewCvTest(TestCase):

    def login(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_create_cv_resolves_to_new_cv_view(self):
        found = resolve('/cv/new')  
        self.assertEqual(found.func, CV_new)

    def test_redirects_after_POST(self):
        self.login()

        response = self.client.post('/cv/new', data={'name':'Post Test', 'phone':'12345678910', 'email':'post.test@test.com'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_post_new_cv_saved(self):
        self.login()

        self.client.post('/cv/new', data={'name':'Post Test', 'phone':'12345678910', 'email':'post.test@test.com'})

        self.assertEqual(CV.objects.count(), 1)
        new = CV.objects.first()
        self.assertEqual(new.name, 'Post Test')
        self.assertEqual(new.phone, '12345678910')
        self.assertEqual(new.email, 'post.test@test.com')

    def test_post_new_cv_displayed(self):
        self.login()

        self.client.post('/cv/new', data={'name':'Post Test', 'phone':'12345678910', 'email':'post.test@test.com'})

        response = self.client.get('/cv')

        self.assertIn('Post Test', response.content.decode())
        self.assertIn('12345678910', response.content.decode())
        self.assertIn('post.test@test.com', response.content.decode())

    def test_user_gone(self):
        self.assertEqual(User.objects.count(), 0)

class SectionTest(TestCase):

    def loginSetUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        CV.objects.create(name='Test Test', phone='12345678910', email='test.test@test.com')

    def test_redirects_after_POST(self):
        self.loginSetUp()
        response = self.client.post('/cv/1/new_section', data={'title':'Section Post Test'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/1/edit_section/1')

    def test_post_new_section_saved(self):
        self.loginSetUp()
        self.client.post('/cv/1/new_section', data={'title':'Section Post Test'})

        self.assertEqual(Section.objects.count(), 1)
        new = Section.objects.first()
        self.assertEqual(new.title, 'Section Post Test')

    def test_post_new_section_appears_on_page(self):
        self.loginSetUp()
        self.client.post('/cv/1/new_section', data={'title':'Section Post Test'})
        
        response = self.client.get('/cv')
        self.assertIn('Section Post Test', response.content.decode())

