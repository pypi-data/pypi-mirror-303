from dataclasses import _process_class, dataclass, field
from enum import Enum
from http import HTTPMethod
from random import choices
from string import ascii_letters, digits
from typing import Optional
from uuid import UUID
from zlib import adler32

from edri.config.setting import SWITCH_KEY_LENGTH
from edri.dataclass.response import Response, ResponseStatus


@dataclass
class BaseIdentification:
    router_id: Optional[UUID] = None
    key: str = field(default_factory=lambda: "".join(choices(ascii_letters + digits, k=SWITCH_KEY_LENGTH)))
    received: bool = False


@dataclass
class Event:
    _key: Optional[str] = field(init=False, default=None)
    _stream: Optional[str] = field(init=False, default=None)
    _switch: Optional[BaseIdentification] = field(init=False, default=None)
    _worker: str | None = field(init=False, default=None)
    response: Optional[Response] = field(init=False, default=None)
    method: Optional[HTTPMethod] = field(init=False, default=None)

    def get_response(self) -> Optional[Response]:
        if self.response and self.response.get_status() != ResponseStatus.NONE:
            return self.response
        return None

    def has_response(self) -> bool:
        return self.response is not None and self.response.get_status() != ResponseStatus.NONE

    def set_response(self, response: Response) -> None:
        self._switch = None
        self.response = response

    def remove_response(self) -> None:
        self._switch = None
        self.response = None

    @classmethod
    def hash_name(cls) -> int:
        return adler32(f"{cls.__module__}.{cls.__qualname__}".encode())


class EventHandlingType(Enum):
    """
    Enum representing the different modes of event handling in the system.

    The `EventHandlingType` Enum is used to categorize the ways in which events
    are handled and dispatched to clients in the API broker system. Each mode
    defines a distinct strategy for event delivery, ensuring that events reach
    their intended recipients based on the specified criteria.

    Attributes:
        SPECIFIC (str): Handles an event in a 1:1 fashion, responding directly to
        the client that requested it. This mode ensures that the event is sent
        only to the client whose request triggered the event.

        Example APIs: Typically used for REST or HTML requests where a client
        makes a direct request, and the server provides a direct response.

        SPECIFIC_SUBSCRIBED (str): A flexible mode of event handling where the event
        can either be a direct 1:1 response to a client's request or be broadcasted
        to all clients subscribed to that event type. The handling behavior is determined
        by the context in which the event is created. If the event originates from a
        REST request or similar, it might behave like a SPECIFIC event. If generated
        internally as part of core logic, it might be broadcast to subscribers.

        Example APIs: Can be used for REST or HTML requests, but also applies to
        asynchronous protocols like WebSocket or MQTT where clients can subscribe
        to specific events.

        SPECIFIC_ALL (str): Similar to `SPECIFIC_SUBSCRIBED`, but with a broader scope.
        The event can either be sent as a direct response to the specific client that
        requested it or broadcasted to all clients capable of receiving events,
        regardless of their subscription status. The handling behavior is determined
        by the event's context — it is either specific or for all, but it cannot be both
        at the same time.

        Example APIs: Applies to REST, HTML, WebSocket, or MQTT. The event could either
        act like a direct response to a client request or be broadcast to every client,
        but not both simultaneously.

        SUBSCRIBED (str): Sends the event exclusively to clients who have registered
        their interest by subscribing to this event type. This mode is used for
        events that are meant to notify or update only a specific subset of clients.

        Example APIs: Suitable for APIs with the ability to accept asynchronous
        events, such as WebSocket or MQTT, where clients subscribe to events
        and receive notifications asynchronously.

        ALL (str): Broadcasts the event to all clients connected to the system that
        are capable of receiving asynchronous events, regardless of their specific
        subscription status. The event is sent to every client that has the ability
        to receive events, not limiting to those who subscribed to a specific type.

        Example APIs: Similar to `SUBSCRIBED`, this mode is used for protocols
        like WebSocket or MQTT, but the event is sent to all clients regardless of
        their specific subscriptions.
    """

    SPECIFIC = "SPECIFIC"
    SPECIFIC_SUBSCRIBED = "SPECIFIC_SUBSCRIBED"
    SPECIFIC_ALL = "SPECIFIC_ALL"
    SUBSCRIBED = "SUBSCRIBED"
    ALL = "ALL"

events: list[Event] = list()
shareable_events: list[Event] = list()


def _event(cls, init, repr, eq, order, unsafe_hash, frozen, match_args, kw_only, slots, weakref_slot, shareable):
    event_response = cls.__annotations__.get("response", False)
    if event_response:
        attribute = getattr(cls, "response", False)
        if attribute:
            attribute.init = False
            attribute.default_factory = event_response
        else:
            setattr(cls, "response", field(init=False, default_factory=event_response))
    dataclass = _process_class(cls, init=init, repr=repr, eq=eq, order=order, unsafe_hash=unsafe_hash, frozen=frozen,
                               match_args=match_args, kw_only=kw_only, slots=slots, weakref_slot=weakref_slot)
    if shareable:
        shareable_events.append(dataclass)
    return dataclass


def event(cls=None, /, *, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
          match_args=True, kw_only=False, slots=False, weakref_slot=False, shareable=False):
    def wrapper(cls):
        return _event(cls, init=init, repr=repr, eq=eq, order=order, unsafe_hash=unsafe_hash, frozen=frozen, match_args=match_args,
                      kw_only=kw_only, slots=slots, weakref_slot=weakref_slot, shareable=shareable)

    if cls is None:
        return wrapper  # pragma: no cover

    return wrapper(cls)


__all__= [Event, event, EventHandlingType, events, shareable_events, BaseIdentification]