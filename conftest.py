import pytest


def pytest_addoption(parser):
    parser.addoption("--URL", action="store", help="input URL")
    # parser.addoption("--password", action="store", help="input password")


@pytest.fixture
def params(request):
    params = {}
    params['URL'] = request.config.getoption('--URL')
    # params['password'] = request.config.getoption('--password') or params['password'] is None
    if params['URL'] is None:
        pytest.skip()
    return params
