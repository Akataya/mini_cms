from django.test import TestCase, Client
from django.urls import reverse
from ...models import Announcement, Section, SectionItem, Office
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='temporary', password='temporary')

        self.index_url = reverse('index')
        self.office_list_url = reverse('offices')
        self.section_url = reverse('section', args=[1])

        self.office = Office(number=1, name='Test Office1', abbreviation='TO1', address='123 Main Street',
                             phone_number='+11234566789')
        self.section = Section.objects.create(title='Section1')
        self.section_item = SectionItem.objects.create(title='Section Item1', section=self.section)

    def test_index_GET(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'content/index.html')

    def test_office_list_GET(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(self.office_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'content/office_list.html')

    def test_section_GET(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(self.section_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'content/section.html')