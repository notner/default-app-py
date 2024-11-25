import flask

from defaultapp.lib.ctx import AppCtx
from defaultapp.lib.ctx import ctx_from_env

from defaultapp.web.backend import root
from defaultapp.web.backend.routes import api
from defaultapp.web.backend.lib.marshal import DefaultAppJSONProvider


def create_app(env: str) -> flask.app.Flask:
    app: flask.app.Flask = flask.Flask(__name__)
    app.ctx: AppCtx = ctx_from_env(env)
    app.json = DefaultAppJSONProvider(app)

    # Register routes
    root.register_blueprint(app)
    api.register_blueprint(app)

    return app
