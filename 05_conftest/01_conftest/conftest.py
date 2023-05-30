import pytest

@pytest.fixture
def initial_value():
    print("Providing the value 10")
    return 10