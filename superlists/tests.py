from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from superlists.views import home_page
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_use_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')