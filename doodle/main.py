from flask import Flask
from .routers import client, tech


def app_factory() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(client.router)
    app.register_blueprint(tech.router)

    @app.get("/")
    async def docs():
        return "Pretend there are docs here..."

    @app.get("/health")
    def health():
        return "OK"

    return app
