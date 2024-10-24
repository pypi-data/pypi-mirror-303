from dataclasses import asdict
from json import loads, JSONDecodeError, dumps
from typing import Callable, Type, Unpack, TypedDict

from edri.api import Headers
from edri.api.dataclass.api_event import api_events
from edri.api.handlers import BaseHandler
from edri.config.constant import ApiType
from edri.dataclass.directive import ResponseDirective
from edri.dataclass.event import Event
from edri.utility import NormalizedDefaultDict
from edri.utility.function import camel2snake, snake2camel


class ResponseKW(TypedDict):
    headers: NormalizedDefaultDict[str,Headers]


class WebsocketHandler(BaseHandler):

    def handle_directives(self, directives: list[ResponseDirective]) -> ...:
        pass

    def __init__(self, scope: dict, receive: Callable, send: Callable, headers: NormalizedDefaultDict[str,Headers]):
        super().__init__(scope, receive, send)
        self.events = {event.resource: event.event for event in api_events if ApiType.WS not in event.exclude}
        self.commands = {event.event: event.resource for event in api_events if ApiType.WS not in event.exclude}
        self.command: str | None = None
        self.headers = headers

    @classmethod
    def type(cls) -> ApiType:
        return ApiType.WS

    async def accept_client(self) -> bool:
        data = await self.receive()
        if "type" in data and data["type"] == "websocket.connect":
            await self.send({"type": "websocket.accept"})
            return True
        else:
            return False

    async def parse_body(self) -> bool:
        data = await self.receive()
        if data["type"] == "websocket.receive":
            if data["text"] is not None:
                received_data = data["text"]
            else:
                received_data = data["bytes"].decode("utf-8", errors="replace")
        else:
            self.logger.error("Parse body failed")
            await self.response_error(1003, "Parse body failed")
            return False
        try:
            self.parameters.update({camel2snake(key): value for key, value in loads(received_data).items()})
        except JSONDecodeError as e:
            self.logger.warning("Cannot process json data", exc_info=e)
            await self.response_error(1003, "Cannot process json data")
            return False
        except Exception as e:
            self.logger.error("Unknown error", exc_info=e)
            await self.response_error(1002, "Unknown error")
            return False
        return True

    async def get_event_constructor(self) -> Type[Event] | None:
        self.command = self.parameters.pop("command", None)
        if self.command is None:
            raise ResourceWarning("Missing command")
        return self.events.get(self.command, None)

    async def response(self, status, data, *args, **kwargs: Unpack[ResponseKW]) -> None:
        respond_data = {
            "command": self.commands[data.__class__],
        }
        respond_data.update(asdict(data))
        respond_data.pop("_key")
        respond_data.pop("_switch")
        respond_data.pop("_stream")
        respond_data.pop("method", None)
        respond_data.pop("_worker", None)
        if respond_data["response"]:
            respond_data["response"]["response_status"] = status
            # respond_data["response"].pop("_status")
            # respond_data["response"].pop("_changed")
            respond_data["response"] = {snake2camel(key): value for key, value in respond_data["response"].items() if
                                        not key.startswith("_")}
        else:
            respond_data.pop("response")
        await self.send({"type": "websocket.send", "text": dumps(respond_data)})

    async def response_error(self, status, data: str | None = None, *args, **kwargs) -> None:
        if status:
            await self.send({"type": "websocket.close", "code": status, "reason": data})
        else:
            await self.send({"type": "websocket.send", "text": dumps({"status": "error", "data": data})})
