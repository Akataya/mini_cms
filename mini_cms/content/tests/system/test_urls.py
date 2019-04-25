from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ...views import index, section, OfficeListView


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_section_url_is_resolved(self):
        url = reverse('section', args=[1])
        self.assertEqual(resolve(url).func, section)

    def test_office_list_url_is_resolved(self):
        url = reverse('offices')
        self.assertEqual(resolve(url).func.view_class, OfficeListView)
