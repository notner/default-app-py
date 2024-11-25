import pytest

from defaultapp.lib.cfg import AppCfg
from defaultapp.lib import exc


def test_cfg():
	cfg = AppCfg.from_env('test')
	assert cfg is not None
	assert cfg['app']['environ'] == 'test'
	assert cfg['server']['mysql']['host'] == 'localhost'
	assert cfg['server']['psql']['host'] == 'localhost'


def test_bad_cfg():
	with pytest.raises(exc.ConfigException):
		AppCfg.from_env('never-actual-name')

	# fails because we dont have prod.toml
	with pytest.raises(exc.ConfigException):
		AppCfg.from_env('prod')
