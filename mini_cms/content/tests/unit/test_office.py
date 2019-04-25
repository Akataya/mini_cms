from unittest import TestCase
from ...models import Office
from ...templatetags.custom_tags import get_office_list_not_empty


class OfficeTest(TestCase):
    def setUp(self):
        self.office1 = Office(number=1, name='Test Office1', abbreviation='TO1', address='123 Main Street',
                              phone_number='+11234566789')

    def test_office_str(self):
        self.assertEqual(self.office1.__str__(), 'TO1')

    def test_get_office_list_not_empty(self):
        Office.objects.create(number=1, name='Test Office2', abbreviation='TO2', address='456 Main Street',
                              phone_number='+11234566788')

        self.assertEquals(get_office_list_not_empty(), True)