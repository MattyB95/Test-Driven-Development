import unittest

from WasRun import WasRun

__author__ = 'Matthew'


class TestCaseTest(unittest.TestCase):
    def setUp(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        assert self.test.wasSetup


TestCaseTest("test_running").run()
TestCaseTest("testSetUp").run()
