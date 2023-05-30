
import pytest

# A simple fixture that generates some inputs
# this take one parameter that is forwarded from the test
# request is the builten fixture
@pytest.fixture
def element_list(request):
    return list(range(request.param))