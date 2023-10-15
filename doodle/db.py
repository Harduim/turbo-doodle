from acouchbase.cluster import Cluster
from config import config
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions


async def get_couchbase():
    cluster = Cluster(
        f"couchbase://{config.HOST}",
        ClusterOptions(PasswordAuthenticator(config.DB_USER, config.DB_PASS)),
    )
    bucket = cluster.bucket(config.DB_BUCKET)
    await bucket.on_connect()

    return cluster, bucket
