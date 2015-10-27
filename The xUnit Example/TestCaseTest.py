import unittest

from WasRun import WasRun

__author__ = 'Matthew'


class TestCaseTest(unittest.TestCase):
    def testTemplateMethod(self):
        test = WasRun("test_method")
        test.run()
        assert "setUp testMethod tearDown " == test.log


TestCaseTest("testTemplateMethod").run()
