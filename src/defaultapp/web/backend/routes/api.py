import formencode
import functools

import flask
from flask import Blueprint

from defaultapp.web.backend.lib.auth import authn_decorator
from defaultapp.web.backend.lib.util import handle_request
from defaultapp.web.backend.lib.validation import validate_decorator

bp = Blueprint('api', __name__)


def route(
    url: str,
    methods: list[str] | None = None,
    perms=None,
    jsSchema: formencode.Schema | None = None,
):
    def decorator(func):
        validate = validate_decorator(jsSchema=jsSchema)(func)
        authn = authn_decorator(perms=perms)(validate)
        wrapped_func = handle_request()(authn)

        @functools.wraps(wrapped_func)
        def wrapper(*args, **kwargs):
            return wrapped_func(*args, **kwargs)

        bp.route('/api' + url, methods=methods)(wrapper)
        return wrapper

    return decorator


def register_blueprint(app: flask.app.Flask):
    # prefix doesnt do shit without uwsgi apparently
    app.register_blueprint(bp, prefix='/api')
