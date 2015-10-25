import unittest

from WasRun import WasRun

__author__ = 'Matthew'


class TestCaseTest(unittest.TestCase):
    @staticmethod
    def test_running():
        test = WasRun("test_method")
        assert (not test.wasRun)
        test.run()
        assert test.wasRun


TestCaseTest("test_running").run()
