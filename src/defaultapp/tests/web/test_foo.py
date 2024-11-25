import json


def test_get_foo(client):
	resp = client.get('/api/foo')
	assert resp.status_code == 200


def test_get_foo_by_id(client):
	resp = client.get('/api/foo/58')
	assert resp.status_code == 200


def test_create_foo(client):
	resp = client.post(
		'/api/foo',
		data=json.dumps({'bar': 'fred'}),
		headers={'content-type': 'application/json'},
	)
	assert resp.status_code == 200
	data = resp.json
	assert data['code'] == 200
	assert data['data'] == 1
