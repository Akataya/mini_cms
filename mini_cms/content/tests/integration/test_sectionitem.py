from unittest import TestCase
from ...models import Section, SectionItem


class SectionItemModelAdminTest(TestCase):
    def test_create_section_item(self):
        s1 = Section(title='Section A')
        s2 = Section(title='Section B')
        s_item = SectionItem(title='Test Section Item', section=s1)

        self.assertEqual(s_item.section, s1)

