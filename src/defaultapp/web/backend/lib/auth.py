import functools


def authn_decorator(perms=None):

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			print('3: check authn...')
			print('     ---> in authn')
			print(f'    run-func: {func.__name__}')
			r = func(*args, **kwargs)
			print('      <---out auth')
			return r

		return wrapper

	return decorator


def authz_decorator(fn):
	def wrapper(*args, **kwargs):
		print('check authz...')
		print('in authz')
		return fn(*args, **kwargs)
		print('out authz')
	return wrapper
