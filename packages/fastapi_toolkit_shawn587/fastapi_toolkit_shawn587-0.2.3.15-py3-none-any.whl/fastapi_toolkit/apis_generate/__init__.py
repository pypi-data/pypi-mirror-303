import inspect

from fastapi_toolkit.generate import CodeGenerator
from fastapi_toolkit.define import Controller


class ApiGenerator:
    g: CodeGenerator

    def __init__(self, g: CodeGenerator):
        self.g = g
        for c in self._get_controller():
            for name, f in inspect.getmembers(c, predicate=inspect.isfunction):
                print(name, f.__annotations__['return'])
                r = f.__annotations__['return']

    def _get_controller(self, root=Controller):
        for model_ in root.__subclasses__():
            yield model_
            yield from self._get_controller(model_)
