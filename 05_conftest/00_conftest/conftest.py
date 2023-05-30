import pytest

@pytest.fixture(autouse=True)
def log_start():
    print("Test Starting")