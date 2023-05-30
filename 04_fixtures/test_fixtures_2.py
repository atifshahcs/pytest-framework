
import pytest


# A simple fixture that generates some inputs

@pytest.fixture(scope="function") #scope="module"
def initial_value():
    print("Generating an initial value!")
    return 5


# Sample functions square and cube
def square(num):
    return num * num


def cube(num):
    return square(num) * num


def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2

def test_cube(initial_value):
    result = cube(initial_value)
    assert result == initial_value ** 3
