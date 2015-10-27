import unittest

from TestResult import TestResult
from TestSuite import TestSuite

from WasRun import WasRun

__author__ = 'Matthew'


class TestCaseTest(unittest.TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert "1 run, 1 failed", self.result.summary()

    def testFailedResultFormatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert "1 run, 1 failed" == self.result.summary()

    def testSuite(self):
        test_suite = TestSuite()
        test_suite.add(WasRun("test_method"))
        test_suite.add(WasRun("test_broken_method"))
        test_suite.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())
