from django.test import TestCase
from django.template import Template, Context


import doctest
from . import mydoctests


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mydoctests))
    return tests
