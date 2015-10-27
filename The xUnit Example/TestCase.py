__author__ = 'Matthew'


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self, result):
        result.test_started()
        self.set_up()
        # noinspection PyBroadException
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass
