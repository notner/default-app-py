# need to import to run the decorators
from defaultapp.web.backend.routes import foo  # noqa: F401
from defaultapp.web.backend.routes import log  # noqa: F401
assert foo
assert log
