class Jtk:

    guts = None

    def __init(self):
        self.guts = 'Set'

    @staticmethod
    def test_static():
        return 'Yep, this works'

    def test_method(self):
        return f"guts is {self.guts}"
