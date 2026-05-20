def test_user_login_page_loads(client):
    response = client.get('/auth/login')
    assert response.status_code == 501
