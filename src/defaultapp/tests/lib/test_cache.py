
from defaultapp.lib.cache import _cache_key


def test_cache_key():
    assert _cache_key('get-log') == 'get-log'
    assert _cache_key('get-log', ('test', 'arg')) == 'get-log-test-arg'
