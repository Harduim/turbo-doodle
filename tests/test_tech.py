from json import loads
from uuid import uuid4

from werkzeug.test import TestResponse

from doodle.models.techs import Tech

from .conftest import test_client


def test_get_tech(test_client):
    response: TestResponse = test_client.get(f"/tech/{uuid4()}")
    print(response)
    assert response.status_code == 200

    tech = Tech.model_validate(loads(response.data))

    assert tech
