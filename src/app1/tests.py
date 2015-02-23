from django.test import TestCase
from django.core.urlresolvers import resolve
from profiles.views import SignInAndSignUp as HomeView


class HomePageOpenTestCase(TestCase):
    def test_home_page_resolves(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__,
                         HomeView.as_view().__name__)


class AssertMethodsTestCase(TestCase):

    def setUp(self):
        self.l1 = [1, 2]
        self.l2 = [1, 0]

    def test_errors1(self):
        assert self.l1 == self.l2

    def test_errors2(self):
        self.assertEqual(self.l1, self.l2)

    def test_errors3(self):
        self.assertListEqual(self.l1, self.l2)

    def test_errors4(self):
        self.assertListEqual(self.l1, None)
