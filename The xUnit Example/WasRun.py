from TestCase import TestCase

__author__ = 'Matthew'


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.wasRun = 1

    def set_up(self):
        self.wasRun = None
        self.wasSetup = 1
