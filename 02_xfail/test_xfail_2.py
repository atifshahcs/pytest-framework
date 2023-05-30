"""
xfail
Now we change the squre function and removing * and added +, so that our test_square should fail. 
"""
import pytest
import sys

# Sample functions square and cube
def square(num):
    return num + num


class TestClass:
    # Test for the functions
    num = 5

    # Test marked as fail (we expect the test to fail)
    # We expect the assertion error, 
    @pytest.mark.xfail(raises=(AssertionError, ZeroDivisionError))
    def test_square(self):
        self.num /= 0
        result = square(self.num)
        assert result == self.num ** 2

