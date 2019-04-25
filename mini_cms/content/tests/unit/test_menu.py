from django.test import TestCase
from ...models import Section
from ...templatetags.custom_tags import get_menu


class MenuTest(TestCase):
    def test_menu(self):
        section1 = Section.objects.create(title='Test')

        self.assertIn(section1, get_menu())

