def test_health_check(client):
    resp = client.get('/health-check')
    assert resp.status_code == 200
    data = resp.json
    assert data['env'] == 'test'
    assert data['success'] == 1
    assert data['psql'] == 23
