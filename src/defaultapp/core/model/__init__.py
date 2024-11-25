def init_models(ctx):
	from defaultapp.core.model.base import PsqlBase
	from defaultapp.core.model.log import Log
	assert Log
	PsqlBase.registry.configure()  # adds all to Base
