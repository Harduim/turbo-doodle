from flask import Flask


def app_factory() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    async def docs():
        return "Pretend there are docs here..."

    @app.get("/health")
    def health():
        return "OK"

    return app
