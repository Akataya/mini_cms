from unittest import TestCase
from ...models import Announcement


class AnnouncementTest(TestCase):
    def setUp(self):
        self.announcement1 = Announcement(title='Test Announcement', show=True, color='Red')

    def test_announcement_str(self):
        self.assertEqual(self.announcement1.__str__(), 'Test Announcement')