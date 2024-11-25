from flask.json.provider import DefaultJSONProvider


def encode_log(o):
    return {
        '__type': 'Log',
        'data': o.data,
        'id': o.id
    }


ENCODE_MAP: dict[str, callable] = {
    'Log': encode_log
}


class DefaultAppJSONProvider(DefaultJSONProvider):
    def __init__(self, app):
        super().__init__(app)

    def default(self, o):
        fn = ENCODE_MAP.get(o.__class__.__name__)
        if fn is not None:
            return fn(o)
        return super().default(self, o)
