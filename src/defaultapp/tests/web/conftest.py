import pytest

from defaultapp.core.model import init_models
from defaultapp.tests.fixtures.psql import populate_psql
from defaultapp.web.app import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app('test')
    init_models(app.ctx)
    populate_psql(app.ctx)

    assert app.ctx.psql
    yield app

    # clean up / reset resources here
    app.ctx.close_db()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
