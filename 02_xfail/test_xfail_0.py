"""
xfail
Now we change the squre function and removing * and added +, so that our test_square should fail. 
"""
import pytest

# Sample functions square and cube
def square(num):
    return num + num


class TestClass:
    # Test for the functions

    num = 5
    # Test marked as fail (we expect the test to fail)

    @pytest.mark.xfail(reason="There is bug in the main square function")
    def test_square(self):
        result = square(self.num)
        assert result == self.num ** 2

