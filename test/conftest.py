import os

import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--molo-bootstrap-image', action='store',
        default=os.environ.get(
            'MOLO_BOOTSTRAP_IMAGE', 'praekeltfoundation/molo-bootstrap:test'),
        help='molo-bootstrap Docker image to test')


def pytest_report_header(config):
    return 'molo-bootstrap docker image: {}'.format(
        config.getoption('--molo-bootstrap-image'))


@pytest.fixture(scope='session')
def molo_bootstrap_image(request):
    return request.config.getoption('--molo-bootstrap-image')
