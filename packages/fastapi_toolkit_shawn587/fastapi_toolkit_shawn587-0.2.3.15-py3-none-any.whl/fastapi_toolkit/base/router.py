from typing import Type
from abc import ABC, abstractmethod
from fastapi import APIRouter
from fastapi_pagination import Page


class BaseRouter(APIRouter, ABC):
    snake_name: str
    snake_plural_name: str
    camel_name: str
    base_schema: Type
    schema: Type

    def __init__(self, config, base_schema: Type, schema: Type):
        super().__init__()
        self.prefix = f"/{self.snake_name}"
        self.tags = [self.camel_name]
        self.base_schema = base_schema
        self.schema = schema

        if config.get_one:
            self.add_api_route(
                path="/get_one",
                endpoint=self._get_one(),
                response_model=self.base_schema,
                methods=["POST"],
                dependencies=config.get_one.guards,
                summary=f"Get one {self.snake_name}",
                description=f"Get one {self.snake_name}",
                response_description=f"A {self.snake_name}",
            )

        if config.batch_get:
            self.add_api_route(
                path="/batch_get",
                endpoint=self._batch_get(),
                response_model=Page[self.base_schema],
                methods=["POST"],
                dependencies=config.get_one.guards,
                summary=f"Batch get {self.snake_name}",
                description=f"Batch get {self.snake_name}",
                response_description=f"Batch {self.snake_name}",
            )

        if config.get_all:
            self.add_api_route(
                path="/get_all",
                endpoint=self._get_all(),
                response_model=Page[self.base_schema],
                methods=["POST"],
                dependencies=config.get_all.guards,
                summary=f"Get all {self.snake_name}",
                description=f"Get all {self.snake_name}",
                response_description=f"All {self.snake_name}",
            )

        if config.get_link_all:
            self.add_api_route(
                path="/get_link_all",
                endpoint=self._get_link_all(),
                response_model=Page[self.schema],
                methods=["POST"],
                dependencies=config.get_link_all.guards,
                summary=f"Get all {self.snake_plural_name} with link",
                description=f"Get all {self.snake_plural_name} with link",
                response_description=f"All {self.snake_plural_name} with link",
            )

            if config.create_one:
                self.add_api_route(
                    path="/create_one",
                    endpoint=self._create_one(),
                    response_model=self.base_schema,
                    methods=["POST"],
                    dependencies=config.create_one.guards,
                    summary=f"Create one {self.snake_name}",
                    description=f"Create one {self.snake_name}",
                    response_description=f"Created {self.snake_name}",
                )

            if config.update_one:
                self.add_api_route(
                    path="/update_one",
                    endpoint=self._update_one(),
                    response_model=self.base_schema,
                    methods=["POST"],
                    dependencies=config.update_one.guards,
                    summary=f"Update one {self.snake_name}",
                    description=f"Update one {self.snake_name}",
                    response_description=f"Updated {self.snake_name}",
                )

            if config.delete_one:
                self.add_api_route(
                    path="/delete_one",
                    endpoint=self._delete_one(),
                    methods=["POST"],
                    dependencies=config.delete_one.guards,
                    summary=f"Delete one {self.snake_name}",
                    description=f"Delete one {self.snake_name}",
                    response_description=f"Deleted {self.snake_name}",
                )

    @abstractmethod
    def _get_one(self):
        raise NotImplementedError

    @abstractmethod
    def _batch_get(self):
        raise NotImplementedError

    @abstractmethod
    def _get_all(self):
        raise NotImplementedError

    @abstractmethod
    def _get_link_all(self):
        raise NotImplementedError

    @abstractmethod
    def _create_one(self):
        raise NotImplementedError

    @abstractmethod
    def _update_one(self):
        raise NotImplementedError

    @abstractmethod
    def _delete_one(self):
        raise NotImplementedError
