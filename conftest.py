# content of conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--slide_number", action="store", default=0,
        help="enter valid slide number")

@pytest.fixture
def slide_number(request):
    """
        Returns a slide_number provide as an input parameter.
    """
    return request.config.getoption("--slide_number")
