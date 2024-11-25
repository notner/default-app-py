def test_get_log(client):
	resp = client.get('/api/logs')
	assert resp.status_code == 200
	data = resp.json
	assert len(data['data']) > 3
