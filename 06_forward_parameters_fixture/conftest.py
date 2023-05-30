
import pytest

# A simple fixture that generates some inputs
# this take one parameter that is forwarded from the test
@pytest.fixture
def element_list(num_elements):
    return list(range(num_elements))