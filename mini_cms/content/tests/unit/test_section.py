from unittest import TestCase
from ...models import Section


class SectionTest(TestCase):
    def setUp(self):
        self.section1 = Section(
            title='Test Section1',
            description='Test Section1 Description',
            show=True
        )

    def test_section_str(self):
        self.assertEqual(self.section1.__str__(), 'Test Section1')