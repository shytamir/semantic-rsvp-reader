from semantic_rsvp.web import create_app


class UnknownEncryptionStatus:
    warning = "encrypted storage could not be confirmed"


def test_app_can_be_created():
    app = create_app()

    assert app is not None


def test_health_endpoint_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert "chunking" in payload


def test_index_returns_mobile_shell(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b'name="viewport"' in response.data
    assert b"Semantic RSVP Reader" in response.data
    assert b"Week 3 prototype" in response.data


def test_storage_encryption_warning_does_not_block_requests(monkeypatch, caplog):
    monkeypatch.setattr(
        "semantic_rsvp.web.check_storage_encryption",
        lambda path: UnknownEncryptionStatus(),
    )
    app = create_app()
    app.config.update(TESTING=False)
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert "encrypted storage could not be confirmed" in caplog.text
