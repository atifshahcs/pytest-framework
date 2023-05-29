# Sample functions square and cube
def square(num):
    return num * num


def cube(num):
    return square(num) * num

# Test for the functions
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2


def test_cube():
    num = 5
    result = cube(num)
    assert result == num ** 3


