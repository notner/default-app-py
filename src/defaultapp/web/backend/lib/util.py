import functools
import flask
from flask import jsonify


def get_ctx():
	return flask.current_app.ctx


def handle_exception(e: Exception):
	# e.type
	# e.status_code
	# internal-errors-> external-errors
	return jsonify({'error': 'error', 'details': str(e)}), 400


def handle_request():
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			try:
				r = func(get_ctx(), *args, **kwargs)
			except Exception as e:
				return handle_exception(e)
			return jsonify({'code': 200, 'data': r}), 200

		return wrapper
	return decorator
