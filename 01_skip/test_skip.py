# Sample functions square and cube
"""
using @pytest.mark.skip
you can skip test class or function by using this above the function or class
"""
import pytest
import sys

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


    @pytest.mark.skipif(
        sys.version_info > (3,7), reason="test required python version <= 3.6")
    def test_skip(self):
        result = cube(self.num)*self.num
        assert self.num ** 4