__author__ = 'Matthew'


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()

    def set_up(self):
        pass
