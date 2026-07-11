import pytest

from semantic_rsvp.web import create_app


@pytest.fixture()
def app():
    return create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "rule_based"})


@pytest.fixture()
def client(app):
    return app.test_client()
