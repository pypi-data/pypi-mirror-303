import asyncio
import inspect
from typing import List

from e2xcore.handlers import E2xApiHandler
from nbgrader.server_extensions.formgrader.base import check_xsrf
from tornado import web

from ...dataclasses import ErrorMessage, SuccessMessage


def status_msg(method):
    """Decorates a method of a BaseApiManager
    Wraps the response in a status message (ErrorMessage or SuccessMessage)
    and catches exceptions.

    Args:
        method: The method to decorate
    """

    if asyncio.iscoroutinefunction(method):

        async def async_wrapper(*args, **kwargs):
            try:
                res = await method(*args, **kwargs)
                return SuccessMessage(data=res)
            except Exception as e:
                return ErrorMessage(error=getattr(e, "message", str(e)))

        return async_wrapper
    else:

        def wrapper(*args, **kwargs):
            try:
                res = method(*args, **kwargs)
                return SuccessMessage(data=res)
            except Exception as e:
                return ErrorMessage(error=getattr(e, "message", str(e)))

        return wrapper


class ApiManageHandler(E2xApiHandler):
    def initialize(self, manager_cls, actions) -> None:
        self.__manager = manager_cls(self.coursedir)
        self.__allowed_actions = {
            request_type: dict(default=None, actions=[])
            for request_type in ["delete", "get", "post", "put"]
        }
        self.set_allowed_actions(actions)

    def set_allowed_actions(self, allowed_actions):
        for request_type, action_dict in self.__allowed_actions.items():
            if request_type in allowed_actions:
                actions = allowed_actions[request_type].get("actions", [])
                for action in actions:
                    assert hasattr(
                        self.__manager, action
                    ), f"The manager class does not provide an action called {action}."
                action_dict["default"] = allowed_actions[request_type].get(
                    "default", None
                )
                action_dict["actions"].extend(actions)

    def extract_arguments(self, method: str):
        params = dict()
        json_body = self.get_json_body() or dict()
        for arg in inspect.signature(method).parameters.keys():
            argument = self.get_argument(name=arg, default=None)
            if argument is None:
                argument = json_body.get(arg, None)
            params[arg] = argument
        return params

    async def perform_action(self, action: str, allowed_actions: List[str]):
        assert (
            action is not None and action in allowed_actions
        ), f"Action {action} is not a valid action."
        method = getattr(self.__manager, action)
        arguments = self.extract_arguments(method)

        # If the method is async, await it, otherwise call it synchronously
        if inspect.iscoroutinefunction(method):
            return await method(**arguments)
        else:
            return method(**arguments)

    @status_msg
    async def handle_request(self, request_type: str):
        action = self.get_argument(
            "action", default=None  # self.__allowed_actions[request_type]["default"]
        )
        if action is None:
            action = (self.get_json_body() or dict()).get(
                "action", self.__allowed_actions[request_type]["default"]
            )

        return await self.perform_action(
            action, self.__allowed_actions[request_type]["actions"]
        )

    @web.authenticated
    @check_xsrf
    async def get(self):
        result = await self.handle_request("get")
        self.finish(result.to_json())

    @web.authenticated
    @check_xsrf
    async def delete(self):
        result = await self.handle_request("delete")
        self.finish(result.to_json())

    @web.authenticated
    @check_xsrf
    async def put(self):
        result = await self.handle_request("put")
        self.finish(result.to_json())

    @web.authenticated
    @check_xsrf
    async def post(self):
        result = await self.handle_request("post")
        self.finish(result.to_json())
