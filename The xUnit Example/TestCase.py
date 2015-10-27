from TestResult import TestResult

__author__ = 'Matthew'


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tear_down()
        return result

    def set_up(self):
        pass

    def tear_down(self):
        pass
