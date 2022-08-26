import pytest


def pytest_addoption(parser):
    parser.addoption("--URL", action="store", help="input URL")


@pytest.fixture
def params(request):
    params = {}
    params['URL'] = request.config.getoption('--URL')
    return params
