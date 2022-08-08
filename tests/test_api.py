from app import app


def test_application():
    api_url = '/test'
    response = app.test_client().get(api_url)
    assert response.status_code == 404
