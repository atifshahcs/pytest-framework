

import pytest


def sum_elements(elements):
    total = 0
    for e in elements:
        total += e
    return total

# A test function for sum elements
# The 'num_elements' parameter is automatically forwarded to our fixture
@pytest.mark.parametrize("num_elements",[1,2,3])
def test_sum(element_list):
    result = sum_elements(element_list)
    assert result == sum(element_list)