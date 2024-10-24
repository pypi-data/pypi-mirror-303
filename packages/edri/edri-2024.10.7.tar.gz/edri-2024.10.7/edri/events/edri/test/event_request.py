from http import HTTPMethod
from typing import Optional

from edri.api.dataclass.api_event import api
from edri.dataclass.event import event
from edri.dataclass.response import Response, response
from edri.events.edri.group import Test as GroupTest


@response
class EventResponse(Response):
    random: Optional[int]


@event
class EventRequest(GroupTest):
    response: EventResponse


@api(template="/src/test")
class EventWithInvalidTemplate(GroupTest):
    method: HTTPMethod = HTTPMethod.GET
    response: EventResponse
