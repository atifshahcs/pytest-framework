# Sample functions square and cube
def square(num):
    return num * num


def cube(num):
    return square(num) * num


class TestClass:
    # Test for the functions
    num = 5
    def test_square(self):
        result = square(self.num)
        assert result == self.num ** 2
    
    def test_cube(self):
        result = cube(self.num)
        assert result == self.num ** 3

    def test_skip(self):
        result = cube(self.num)*self.num
        assert self.num ** 4