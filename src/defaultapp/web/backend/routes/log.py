from defaultapp.lib.ctx import AppCtx
from defaultapp.web.backend.routes import api

from defaultapp.core.model.log import Log


@api.route('/logs', methods=['GET'])
def get_logs_new(ctx: AppCtx):
	return [r for r in ctx.psql.query(Log).all()]
