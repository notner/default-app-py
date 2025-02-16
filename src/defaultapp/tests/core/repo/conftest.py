import pytest

from defaultapp.core.model import init_models
from defaultapp.lib import ctx
from defaultapp.tests.fixtures.psql import populate_psql


@pytest.fixture
def app_ctx():
    app_ctx = ctx.ctx_from_env('test')
    init_models(app_ctx)
    populate_psql(app_ctx)
    yield app_ctx
    app_ctx.close_db()
