"""


"""
import pytest

# Sample functions square and cube
def square(num):
    return num * num

# our parameterized test
@pytest.mark.parametrize("num", [1,2,3,4])
def test_square(num):
    result = square(num)
    assert result == num ** 2