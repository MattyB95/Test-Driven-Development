from TestCase import TestCase

__author__ = 'Matthew'


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def set_up(self):
        self.log = "setUp "

    def test_method(self):
        self.log = self.log + "testMethod "

    def tear_down(self):
        self.log = self.log + "tearDown "
