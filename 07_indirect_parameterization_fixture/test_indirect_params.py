
import pytest


def sum_elements(elements):
    total = 0
    for e in elements:
        total += e
    return total

# A test function for sum elements
# The 'element_list' parameter is automatically forwarded to our fixture
# The 'element_list' is same name as passing to test method
@pytest.mark.parametrize("element_list",[1,2,3], indirect=True)
def test_sum(element_list):
    result = sum_elements(element_list)
    assert result == sum(element_list)