from enum import Enum
from http import HTTPStatus
from json import dumps, JSONEncoder
from pathlib import Path
from typing import Any, Callable, Unpack, TypedDict

from edri.api import Headers
from edri.api.handlers import HTTPHandler
from edri.api.handlers.http_handler import ResponseErrorKW
from edri.config.constant import ApiType
from edri.dataclass.directive import HTTPResponseDirective
from edri.dataclass.event import Event
from edri.utility import NormalizedDefaultDict


class ResponseKW(TypedDict):
    headers: NormalizedDefaultDict[str, Headers]


class RESTHandler[T: HTTPResponseDirective](HTTPHandler):
    _directive_handlers: dict[T, Callable[[T], tuple[int, Headers]]] = {}

    class CustomJSONEncoder(JSONEncoder):
        """
        A custom JSON encoder for converting various data types to JSON-compatible
        formats, including support for Enums, datetime objects, Paths, bytes, and
        more.

        Inherits from JSONEncoder to override the default() method for custom serialization.
        """

        def default(self, data) -> Any:
            # noinspection SpellCheckingInspection
            if hasattr(data, "to_json"):
                return data.to_json()
            elif hasattr(data, "isoformat"):
                return data.isoformat()
            elif isinstance(data, Path):
                return data.as_posix()
            elif isinstance(data, bytes) or isinstance(data, bytearray):
                return data.hex()
            elif isinstance(data, Enum):
                return data.value
            else:
                return super().default(data)

    @classmethod
    def api_type(cls) -> ApiType:
        return ApiType.REST

    async def response(self, status: HTTPStatus, data: Event | bytes, *args, **kwargs: Unpack[ResponseKW]):
        headers = kwargs["headers"]
        if isinstance(data, Event):
            response = data.get_response()
            if "Content-Type" not in headers:
                headers["Content-Type"].append("application/json")
            try:
                body = dumps(response.as_dict(transform=True, keep_concealed=False), ensure_ascii=False, cls=self.CustomJSONEncoder).encode("utf-8")
            except TypeError as e:
                self.logger.error("Object is not JSON serializable", exc_info=e)
                await self.response_error(HTTPStatus.INTERNAL_SERVER_ERROR, {
                    "reasons": [{
                        "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                        "message": "Object is not JSON serializable",
                    }]
                })
                return
        else:
            body = data

        return await super().response(status, body, headers=headers)

    async def response_error(self, status: HTTPStatus, data: Event | dict | None = None, *args, **kwargs: Unpack[ResponseErrorKW]):
        data = self.response_error_prepare(status, data)
        data = dumps(data, ensure_ascii=False, cls=self.CustomJSONEncoder).encode("utf-8")
        return await super().response_error(status, data, *args, **kwargs)
