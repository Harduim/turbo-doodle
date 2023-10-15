from flask import Blueprint

from ..models.techs import Tech
from uuid import UUID

router = Blueprint("tech", __name__, url_prefix="/tech")


@router.get("<tech_id>")
async def get_tech(tech_id: str) -> str:
    tech = Tech(id=UUID(tech_id), name="tech_name", email="tech@email.com")
    return tech.model_dump_json()
