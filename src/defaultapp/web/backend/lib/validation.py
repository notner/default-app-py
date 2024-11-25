import functools
import flask


def validate_decorator(jsSchema=None, qsSchema=None):

	def decorator(func):

		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			d: dict = {}
			req = flask.request
			if jsSchema:
				if not req.is_json:
					raise Exception('Invalid content type. JSON required.')

				# attempt decode to json
				try:
					data = req.get_json()
				except Exception as e:
					raise Exception(f'Invalid JSON format. {str(e)}')

				# validate this with the schema
				d = jsSchema.to_python(data)

			return func(*args, **d, **kwargs)

		return wrapper

	return decorator
