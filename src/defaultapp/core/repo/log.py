# access layer into log
from defaultapp.core.model.log import Log
from defaultapp.lib.ctx import AppCtx


def get(ctx: AppCtx) -> list[Log]:
	return [r for r in ctx.psql.query(Log).all()]
