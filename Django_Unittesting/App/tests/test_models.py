from django.test import TestCase
from .models import User

class UserTestCase(TestCase):

    def setUp(self):
        self.author     = User.objects.create(
          username      = 'author@test.com',
          email         = 'author@test.com',
          user_type     = User.AUTHOR
        )
        self.publisher = User.objects.create(
          username='publisher@test.com',
          email='publisher@test.com',
          user_type=User.AUTHOR
        )

    def test_get_authors(self):
      self.assertEqual(User.get_authors(), 1)

    def test_can_write_books(self):
      self.assertTrue(self.author.can_write_books())
      self.assertFalse(self.publisher.can_write_books())