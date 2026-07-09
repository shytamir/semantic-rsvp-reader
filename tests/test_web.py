from semantic_rsvp.web import create_app


def test_app_can_be_created():
    app = create_app()

    assert app is not None


def test_health_endpoint_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index_returns_mobile_shell(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b'name="viewport"' in response.data
    assert b"Semantic RSVP Reader" in response.data
    assert b"Week 3 prototype" in response.data
