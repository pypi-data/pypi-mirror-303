from http import HTTPMethod

from edri.api.dataclass.api_event import api
from edri.config.constant import ApiType
from edri.dataclass.response import Response, response
from edri.events.api.group import Manage


@response
class RegisterResponse(Response):
    pass


@api(resource="register", exclude=[ApiType.REST, ApiType.HTML])
class Register(Manage):
    events: list[str]
    parameters: list[str]
    values: list[str]
    # method: HTTPMethod = HTTPMethod.PUT
    response: RegisterResponse
