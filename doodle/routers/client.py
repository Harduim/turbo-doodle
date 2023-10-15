from flask import Blueprint

from ..models.clients import Client
from uuid import UUID

router = Blueprint("client", __name__, url_prefix="/client")


@router.get("<client_id>")
async def get_client(client_id: str) -> str:
    client = Client(id=UUID(client_id), name="client_name", email="client@email.com")
    return client.model_dump_json()
