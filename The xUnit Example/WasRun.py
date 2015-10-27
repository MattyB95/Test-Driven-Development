from TestCase import TestCase

__author__ = 'Matthew'


def test_broken_method():
    raise Exception


class WasRun(TestCase):
    def __init__(self, name):
        self.log = "setUp "
        self.wasRun = None
        TestCase.__init__(self, name)

    def set_up(self):
        pass

    def test_method(self):
        self.log += "testMethod "

    def tear_down(self):
        self.log += "tearDown "
