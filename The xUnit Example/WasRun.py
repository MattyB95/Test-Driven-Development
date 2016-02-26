from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = "setUp "

    def set_up(self):
        pass

    def test_method(self):
        self.log += "testMethod "

    @staticmethod
    def test_broken_method():
        raise Exception

    def tear_down(self):
        self.log += "tearDown "
