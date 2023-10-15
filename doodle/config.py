import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.PORT = int(os.getenv("SERVER_PORT", 3001))
        self.HOST = os.getenv("SERVER_HOST", "localhost")

        self.DB_CLUSTER_NAME = os.getenv("COUCHBASE_CLUSTER_NAME", "")
        self.DB_HOST = os.getenv("COUCHBASE_HOST", "localhost")
        self.DB_USER = os.getenv("COUCHBASE_USER", "")
        self.DB_PASS = os.getenv("COUCHBASE_PASS", "")
        self.DB_BUCKET = os.getenv("COUCHBASE_BUCKET", "")


config = Config()
