from typing import Type, List, Optional, Callable

from fastapi import FastAPI, APIRouter
from fastapi_pagination import Page

from fastapi_toolkit.define import Schema


class Endpoint:
    def __init__(self, repo_map):
        self.repo_map = repo_map

    def _get_repo(self, s: Type[Schema]):
        def dfs(a: Type[Schema], p: List[Type[Schema]]):
            for i in a.__subclasses__():
                yield from dfs(i, p.copy() + [a])
                if i is not s:
                    continue
                yield p + [a, i]

        try:
            path = next(dfs(Schema, []))
        except StopIteration:
            raise ValueError(f"can't find repo for {s.__name__}")

        for c in path:
            if c in self.repo_map:
                return self.repo_map[c]

    def get_one(self, router: FastAPI | APIRouter, url: str, func: Optional[Callable[..., Schema]] = None):
        def decorator(view: Type[Schema]):
            nonlocal func
            if func is None:
                func = self._get_repo(view).get_one
            router.add_api_route(
                path=url,
                endpoint=func,
                methods=['POST'],
                tags=[view.__name__],
                response_model=view,
            )

            return view

        return decorator

    def get_many(self, router: FastAPI | APIRouter, url: str, func: Optional[Callable[..., Page[Schema]]] = None):
        def decorator(view: Type[Schema]):
            nonlocal func
            if func is None:
                func = self._get_repo(view).get_all
            router.add_api_route(
                path=url,
                endpoint=self._get_repo(view).get_all,
                methods=['POST'],
                tags=[view.__name__],
                response_model=Page[view],
            )

            return view

        return decorator
