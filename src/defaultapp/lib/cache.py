import functools
import logging
import pickle

from defaultapp.lib.ctx import AppCtx


log = logging.getLogger(__name__)


def _cache_key(func_name: str, *args, ignore_args=None) -> str:
    if not args:
        return f'{func_name}'
    return f'{func_name}-{"-".join([arg for arg in iter(*args) if arg])}'


def cached(name=None, expire=None, ignore_args=None):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ctx = None
            for arg in args:
                if isinstance(arg, AppCtx):
                    ctx = arg
            if not ctx:
                log.error(
                    'failed to get ctx to be able to cache'
                )
            # remove ctx from cache attempt
            cache_key = _cache_key(name or func.__name__, args[1:], ignore_args=ignore_args)

            # look up in redis
            cached_value = ctx.redis.get(cache_key)
            if cached_value:
                return pickle.loads(cached_value)

            # not in cache, get and add to cache
            r = func(*args, **kwargs)
            ctx.redis.set(cache_key, pickle.dumps(r), expire=expire)
            return r

        return wrapper

    return decorator
