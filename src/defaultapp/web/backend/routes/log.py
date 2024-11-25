from defaultapp.core.repo import log
from defaultapp.lib.ctx import AppCtx
from defaultapp.web.backend.routes import api


@api.route('/logs', methods=['GET'])
def get_logs(ctx: AppCtx) -> list:
	return log.get(ctx)
