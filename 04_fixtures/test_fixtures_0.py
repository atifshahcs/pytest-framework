"""


"""
import pytest

# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    return 5

# Sample functions square
def square(num):
    return num * num
# test function for squre
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2