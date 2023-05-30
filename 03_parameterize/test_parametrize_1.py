"""


"""
import pytest

# Sample functions square and cube
def square(num):
    return num * num

# our parameterized test
@pytest.mark.parametrize("num,ref", [(1,1),(2,4),(3,9),(4,16)])
def test_square(num, ref):
    result = square(num)
    assert result == ref