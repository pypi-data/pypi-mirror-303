from typing import Union, List

from fastapi import Security


class RouteConfig:
    guards: List[Security]

    def __init__(self, guards: List[Security] = None):
        self.guards = []
        if guards is not None:
            self.guards = guards


class ModelConfig:
    get_one: Union[RouteConfig, bool]
    batch_get: Union[RouteConfig, bool]
    get_link_one: Union[RouteConfig, bool]
    get_all: Union[RouteConfig, bool]
    get_link_all: Union[RouteConfig, bool]
    create_one: Union[RouteConfig, bool]
    update_one: Union[RouteConfig, bool]
    delete_one: Union[RouteConfig, bool]

    def __init__(self):
        self.get_one = RouteConfig()
        self.batch_get = RouteConfig()
        self.get_link_one = RouteConfig()
        self.get_all = RouteConfig()
        self.get_link_all = RouteConfig()
        self.create_one = RouteConfig()
        self.update_one = RouteConfig()
        self.delete_one = RouteConfig()

    def add_guard(self, guard):
        self.get_one.guards.append(guard)
        self.get_link_one.guards.append(guard)
        self.get_all.guards.append(guard)
        self.get_link_all.guards.append(guard)
        self.create_one.guards.append(guard)
        self.update_one.guards.append(guard)
        self.delete_one.guards.append(guard)
