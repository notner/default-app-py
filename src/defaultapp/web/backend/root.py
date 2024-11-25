import sqlalchemy as sa

from flask import Blueprint, jsonify
from defaultapp.web.backend.lib.util import get_ctx

bp = Blueprint('/', __name__)


@bp.route('/health-check', methods=['GET'])
def health():
    ctx = get_ctx()
    psql_up = ctx.psql.execute(sa.text('select 23;')).one()[0]
    return jsonify({'success': 1,
                    'env': ctx.environ,
                    'psql': psql_up})


def register_blueprint(app):
    app.register_blueprint(bp)
