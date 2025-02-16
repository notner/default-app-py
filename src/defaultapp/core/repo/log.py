# access layer into log
# The Repository Pattern focuses on data access and provides a clean abstraction layer for interacting with the data source,
import logging
from defaultapp.core.model.log import Log
from defaultapp.lib.cache import cached
from defaultapp.lib.ctx import AppCtx


log = logging.getLogger(__name__)


@cached(name='get-log', expire=10)
def get(ctx: AppCtx) -> list[Log]:
	return [r for r in ctx.psql.query(Log).all()]
