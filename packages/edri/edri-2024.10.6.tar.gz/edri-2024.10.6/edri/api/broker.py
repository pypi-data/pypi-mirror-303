from multiprocessing.queues import Queue
from multiprocessing.connection import wait, Connection
from typing import Optional, Set, cast
from logging import getLogger

from edri.abstract.manager.manager_base import ManagerBase
from edri.api.middleware import Middleware
from edri.api.dataclass import Client
from edri.api.dataclass.api_event import api_events
from edri.config.constant import ApiType
from edri.dataclass.directive.base import InternalServerErrorResponseDirective
from edri.dataclass.event import Event
from edri.dataclass.response import ResponseStatus
from edri.events.api import group, manage, client
from edri.utility import Storage



class Broker(ManagerBase):
    """
    The ApiBroker class acts as an intermediary between the central router and all API handlers,
    managing client registrations, event dispatching, and communication in a multiprocessing
    environment. It extends ManagerBase to leverage common management functionalities and
    adds capabilities specific to API interactions.

    Attributes:
        api_broker_queue (Queue): A multiprocessing queue used to receive events specifically for the API broker.
        clients (Optional[Storage[Client]]): A storage mechanism for registered clients, allowing for quick access and management.
        db: Placeholder attribute for potential database connections or operations, not implemented by default.
        events (dict): A mapping of event resources to event classes, derived from the global api_events definition.
        middlewares_request (list[Middleware]): List of middlewares applied to incoming requests.
        middlewares_response (list[Middleware]): List of middlewares applied to outgoing responses.

    Methods:
        __init__(router_queue: "Queue[Event]", api_broker_queue: "Queue[Event]", middlewares: list[Middleware]):
            Constructor for the ApiBroker class.
        name (property): Returns the name of the ApiBroker instance.
        send_specific(event: Event): Sends an event to a specific client based on the event's key.
        send_all(event: Event): Broadcasts an event to all clients of a specific API type.
        client_register(event: client.Register): Registers a new client and sends a confirmation event.
        client_unregister(event: Event): Unregisters a client based on the event's key.
        event_register(event: manage.Register): Registers a client for specific events and parameters.
        solve(event: Event): Determines the appropriate method to handle an incoming event.
        _prepare(): Prepares the ApiBroker for operation by initializing storage for clients.
        additional_pipes (property): Returns a set of additional pipes to monitor for incoming events.
        run_resolver(): Main loop for processing incoming events and dispatching them to the appropriate handlers.
        resolve_callback(event: Event, pipe: Connection): Callback method for handling events received from clients.
        _prepare_resolvers(): Prepares resolvers for handling specific types of events.
        resolve(event: Event): Processes an event through the appropriate middlewares and forwards it to its destination.

    Usage:
        This class is instantiated with specific queues and is used within a multiprocessing
        application to manage communications between the router and API handlers. It handles
        client registrations, event dispatching, and utilizes middlewares for request and
        response processing.
    """

    def __init__(self, router_queue: Queue[Event], api_broker_queue: Queue[Event], middlewares: list[Middleware]) -> None:
        """
        Initializes an ApiBroker instance with specific queues for routing and
        API broker events.

        Parameters:
            router_queue (Queue): The queue for receiving routed events from other
            components of the system.
            api_broker_queue (Queue): The queue specifically for the API broker to
            receive events.
        """
        super().__init__(router_queue)
        self.api_broker_queue = api_broker_queue
        self.logger = getLogger(__name__)
        self.clients: Storage[Client]
        self.db = None
        self.events = {event.resource: event.event for event in api_events}
        self.middlewares_request = [middleware for middleware in middlewares if middleware.is_request]
        self.middlewares_response = [middleware for middleware in middlewares if middleware.is_response]

    @property
    def name(self) -> str:
        """
        Property returning the name of the ApiBroker instance. Primarily used for
        logging and identification purposes.

        Returns:
            str: The name "ApiBroker".
        """
        return "ApiBroker"

    def _send(self, client: Client, event: Event) -> None:
        """
        Attempts to send an event to a specific client. If the connection is broken
        or reset during sending, it logs a warning and unregisters the client.

        Parameters:
            client (Client): The client object representing the target for the event.
            event (Event): The event to be sent to the client.

        Returns:
            None
        """
        try:
            client.socket.send(event)
        except (BrokenPipeError, ConnectionResetError) as e:
            self.logger.warning("Cannot be send %s", client.socket, exc_info=e)
            self.client_unregister(event)

    def send_specific(self, event: Event) -> None:
        """
        Sends an event to the specific client identified by the event's key. Logs
        a warning if the client is not found.

        Parameters:
            event (Event): The event containing the key of the target client.

        Returns:
            None
        """
        self.logger.debug("-> %s", event)
        if not event._key:
            self.logger.error("Key not found in the event %s", event)
            return
        try:
            client = self.clients[event._key]
        except KeyError:
            self.logger.warning("Client was not found: %s", event)
            return
        self._send(client, event)

    def send_all(self, event: Event) -> None:
        """
         Broadcasts an event to all clients that are of a specific API type (e.g., WebSocket).
         It iterates through all clients and sends the event to those matching the type.

         Parameters:
             event (Event): The event to be broadcasted.

         Returns:
             None
         """
        self.logger.debug("->* %s", event)
        for client in self.clients.values():
            if client.type == ApiType.WS:
                self._send(client, event)

    ##### API #####
    def client_register(self, event: client.Register) -> None:
        """
        Handles the registration of a new client based on the received register event.
        It assigns a unique key to the client, stores it, and acknowledges the registration.

        Parameters:
            event (client.Register): The event containing the client's registration information.

        Returns:
            None
        """
        event._key = self.clients.append(Client(event.socket, ApiType.WS))
        event.socket = None
        event.response.set_status(ResponseStatus.OK)
        self.send_specific(event)

    def client_unregister(self, event: Event) -> None:
        """
        Handles the unregistration of a client, removing them from the stored clients
        based on the event's key. It performs cleanup if necessary.

        Parameters:
            event (Event): The event containing the key of the client to be unregistered.

        Returns:
            None
        """
        try:
            if event._key:
                client = self.clients[event._key]
                client.socket.close()
                del self.clients[event._key]
            else:
                self.logger.warning("Client cant be unregistered because key is missing!")
        except KeyError as e:
            self.logger.debug("Client was not found!", exc_info=e)

    def event_register(self, event: manage.Register) -> None:
        """
          Registers a client for specific events and their parameters, allowing for
          customized event handling. This method updates the client's event subscriptions
          and their associated parameters based on the provided event registration details.

          Parameters:
              event (manage.Register): An object representing the event registration request.
              This object must include a non-empty `_key` attribute identifying the client,
              a list of `events` the client wishes to subscribe to, and corresponding
              `parameters` and `values` for those events.

          Returns:
              None

          Raises:
              KeyError: If the event `_key` attribute is missing or if the `_key` does not
              correspond to any existing client in the `clients` dictionary.

              ValueError: If the `events` list in the `event` object is empty, indicating
              that no events have been specified for registration.

              LookupError: If any of the events specified in the `event.events` list do not
              exist in the `self.events` mapping, indicating an attempt to register for
              undefined events.

          This method first verifies that the event `_key` is present and corresponds to an
          existing client. It then proceeds to update the client's event subscriptions and
          parameters. If successful, the client's response status is set to `OK`, and the
          updated event registration details are sent back to the client via their socket.
          """
        if not event._key:
            raise AttributeError("Event key is missing!")
        try:
            client = self.clients[event._key]
        except KeyError as e:
            self.logger.error("Client was not found: %s", event, exc_info=e)
            return

        client.events = {self.events[event] for event in event.events}
        client.parameters = dict(zip(event.parameters, event.values))
        event.response.set_status(ResponseStatus.OK)
        client.socket.send(event)

    def solve(self, event: Event) -> None:
        """
        Determines how to handle an incoming event, directing it to specific clients
        or broadcasting it based on the event's properties.

        Parameters:
            event (Event): The event to be handled.

        Returns:
            None
        """
        if event._key:
            self.send_specific(event)
        else:
            found = False
            for client in self.clients.values():
                if event.__class__ in client.events:
                    found = True
                    client.socket.send(event)
            if not found:
                self.send_all(event)

    def _prepare(self) -> None:
        """
         Prepares the ApiBroker for operation by initializing necessary components,
         such as client storage.

         Returns:
             None
         """
        super()._prepare()
        self.clients = Storage[Client]()

    @property
    def additional_pipes(self) -> Set[Connection]:
        """
        Provides a set of additional pipes that should be monitored for incoming
        events, specifically the API broker queue.

        Returns:
            Set[Pipe]: A set containing the reader end of the API broker queue.
        """
        return {self.api_broker_queue._reader}

    def run_resolver(self) -> None:
        """
        The main event loop of the ApiBroker, continuously checking for and processing
        incoming events from various sources.

        Returns:
            None
        """
        while True:
            pipes: set[Connection] = set()
            if self.router_pipe:
                pipes.add(self.router_pipe)
            if self._workers:
                pipes.update(worker.pipe for worker in self._workers.values())
            pipes.update(self.additional_pipes)
            try:
                active_pipes = cast(list[Connection], wait(pipes, timeout=10))
                for active_pipe in active_pipes:
                    if active_pipe == self.router_pipe:
                        event: Event = self.router_pipe.recv()
                        self.logger.debug("Received event: %s", event)
                        self.resolve(event)
                    else:
                        try:
                            event = active_pipe.recv()
                        except EOFError as e:
                            self.logger.error("Communication problems", exc_info=e)
                            continue
                        except OSError as e:
                            self.logger.error("OS problems", exc_info=e)
                            continue
                        self.resolve_callback(event, active_pipe)

            except KeyboardInterrupt:
                return

    def resolve_callback(self, event: Event, pipe: Connection) -> None:
        """
        Handles incoming events received from clients or other components, dispatching
        them to the appropriate handling method based on their type.

        Parameters:
            event (Event): The incoming event to be handled.
            pipe (Connection): The communication pipe from which the event was received.

        Returns:
            None
        """
        self.logger.debug("<- Client %s", event)
        if isinstance(event, group.Client):
            if isinstance(event, client.Register):
                self.client_register(event)
            elif isinstance(event, client.Unregister):
                self.client_unregister(event)
        elif isinstance(event, group.Manage):
            if isinstance(event, manage.Register):
                self.event_register(event)
        else:
            for middleware in self.middlewares_request:
                try:
                    middleware.process_request(event)
                except Exception as e:
                    self.logger.error("Unknown error while processing request in middleware", exc_info=e)
                    event.response.set_status(ResponseStatus.FAILED)
                    event.response.add_directive(InternalServerErrorResponseDirective(f"Unknown error while processing request in middleware: {middleware.__class__.__name__}"))
                    self.resolve(event)
                    return
                if not isinstance(event, Event):
                    self.logger.error("Wrong type returned by %s", middleware.__class__.__name__)
                    event.response.set_status(ResponseStatus.FAILED)
                    event.response.add_directive(InternalServerErrorResponseDirective(f"Wrong type returned by {middleware.__class__.__name__}"))
                    self.resolve(event)
                    return
                if event.response.get_status() != ResponseStatus.NONE:
                    self.logger.debug("Event %s returned by %s", event, middleware.__class__.__name__)
                    self.resolve(event)
                    return
            self.logger.debug("Router <- API Broker %s", event)
            self.router_queue.put(event)

    def _prepare_resolvers(self) -> None:
        """
        Prepares the resolvers for handling specific types of events, enhancing
        the base implementation with API-specific event handling.

        Returns:
            None
        """
        super()._prepare_resolvers()
        for event in api_events:
            if "response" not in event.event.__annotations__:
                self._requests[event.event] = self.solve
            else:
                self._responses[event.event] = self.solve

    def resolve(self, event: Event) -> None:
        for middleware in self.middlewares_response:
            event = middleware.process_response(event)
            if event.response.get_status() != ResponseStatus.OK:
                self.logger.debug("Event %s returned by %s", event, middleware.__class__.__name__)
                super().resolve(event)
                return
        super().resolve(event)
