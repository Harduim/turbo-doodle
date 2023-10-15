from pytest import fixture

from doodle.main import app_factory


@fixture(scope="function")
def test_app():
    app = app_factory()

    yield app


@fixture(scope="function")
def test_client(test_app):
    return test_app.test_client()


@fixture(scope="function")
def cli_runner(test_app):
    return test_app.test_cli_runner()
