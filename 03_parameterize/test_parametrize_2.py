"""


"""
import math
import pytest

# Sample functions that raises a base to a power
def pow(base, exp):
    return base ** exp

# our parameterized test
@pytest.mark.parametrize("base", [1,2,3])
@pytest.mark.parametrize("exp", [4,5,6])
def test_square(base, exp):
    result = pow(base, exp)
    assert result == math.pow(base,exp)