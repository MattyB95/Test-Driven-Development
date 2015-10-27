import unittest

from WasRun import WasRun

__author__ = 'Matthew'


class TestCaseTest(unittest.TestCase):
    def testTemplateMethod(self):
        test = WasRun("test_method")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed", result.summary


TestCaseTest("testTemplateMethod").run()
