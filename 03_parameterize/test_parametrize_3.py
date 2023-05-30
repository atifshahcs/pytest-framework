"""


"""
import pytest

# Sample functions square and cube
def square(num):
    return num * num

# our parameterized test
@pytest.mark.parametrize("num", [1,2, pytest.param(3, marks=pytest.mark.skip),4])
def test_square(num):
    result = square(num)
    assert result == num ** 2