from doodle.main import app_factory


if __name__ == "__main__":
    app = app_factory()
    app.run(port=3001, debug=True)
