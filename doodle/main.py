from flask import Flask


def app_factory() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def docs():
        return "Pretend there are docs here..."

    return app
