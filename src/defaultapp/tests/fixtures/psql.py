from defaultapp.lib.ctx import AppCtx
from defaultapp.core.model.log import Log


def populate_psql(ctx: AppCtx):
	#  psql is up, now populate it with test data
	for idx in range(0, 6):
		ctx.psql.add(Log(id=idx, data=f'log {idx}'))
	try:
		ctx.psql.commit()
	except Exception:
		ctx.psql.rollback()
