import factory
from django.test import TestCase
from .models import Post


class PostFactory(factory.Factory):
    class Meta:
        model = Post

    message = ""


class PostTestCase(TestCase):

    def setUp(self):
        self.blank_message = PostFactory.create()
        self.silly_message = PostFactory.create(message="silly")

    def test_post_title_was_set(self):
        self.assertEqual(self.blank_message.message, "")
        self.assertEqual(self.silly_message.message, "silly")
