import formencode

from defaultapp.lib.ctx import AppCtx
from defaultapp.web.backend.routes import api


@api.route('/foo', methods=['GET'])
def get_all_foo(ctx: AppCtx):
    return ['the', 'options']


@api.route('/foo/<int:id>', methods=['GET'])
def get_foo_by_id(ctx: AppCtx, id: int):
    return [id]


class CreateFooSchema(formencode.Schema):
    bar = formencode.validators.ByteString(not_empty=True)
    fred = formencode.validators.ByteString(if_missing=None)


@api.route('/foo', methods=['POST'], jsSchema=CreateFooSchema)
def create_foo(ctx: AppCtx, bar: str, fred: str | None = None):
    return 1
