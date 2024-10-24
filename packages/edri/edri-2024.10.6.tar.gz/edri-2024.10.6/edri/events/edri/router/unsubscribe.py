from multiprocessing.connection import Connection
from typing import Type

from edri.dataclass.event import Event, event
from edri.events.edri.group import Router


@event
class Unsubscribe(Router):
    event_type: Type[Event]
    pipe: Connection
    request: bool
