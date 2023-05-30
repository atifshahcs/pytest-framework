

# Sample functions square and cube
def square(num):
    return num * num

# Test using fixture
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2