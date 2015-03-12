from django.test import TestCase
from django.template import Template, Context


class DjTemplatesVsPythonInterp(TestCase):

    def test_equivalence(self):
        py = "<h1>{title}</h1>".format(title="SuperBook")
        dj = Template("<h1>{{ title }}</h1>").render(
            Context({"title": "SuperBook"}))
        expected = '<h1>SuperBook</h1>'

        self.assertEqual(py, dj)
        self.assertEqual(dj, expected)


import doctest
from . import mydoctests


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mydoctests))
    return tests
