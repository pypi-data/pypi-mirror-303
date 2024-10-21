import datetime
from enum import Enum
from typing import Type, Union, Optional, Set
from pydantic import BaseModel, Field as PField
from pydantic.fields import FieldInfo, PydanticUndefined


class LinkType(str, Enum):
    one = "one"
    many = "many"


class Link(BaseModel):
    model: str
    type: LinkType


class FieldType(BaseModel):
    python_type: str
    sql_type: str = PField(default="")
    nullable: bool = PField(default=False)
    link: Optional[Link] = PField(default=None)
    depends: Set[str] = PField(default_factory=set)
    default: Optional[str] = PField(default=None)


class FieldHelper:

    @staticmethod
    def is_builtin(t: Type):
        return t in [str, int, float, bool, bytes, datetime.datetime, datetime.date]

    def parse_builtin(self, t: Type):
        if not self.is_builtin(t):
            return
        t: [str, int, float, bool, bytes]
        sql_map = {
            str: "sqltypes.Text",
            int: "sqltypes.Integer",
            float: "sqltypes.Float",
            bool: "sqltypes.Boolean",
            bytes: "sqltypes.LargeBinary",
            datetime.datetime: "sqltypes.DateTime",
            datetime.date: "sqltypes.Date",
        }
        f = FieldType(python_type=str(t.__name__), sql_type=sql_map[t])
        if t.__module__ != "builtins":
            f.python_type = f"{t.__module__}.{f.python_type}"
            f.depends.add(t.__module__)
        return f

    def is_model(self, t: Type):
        if self.is_builtin(t):
            return False
        return isinstance(t, type) and BaseModel.__subclasscheck__(t)

    def parse_model(self, t: Type):
        if not self.is_model(t):
            return
        return FieldType(python_type=t.__name__, link=Link(model=t.__name__, type="one"))

    def is_optional(self, t: Type):
        if self.is_builtin(t):
            return False
        if not hasattr(t, "__origin__"):
            return False
        origin = getattr(t, "__origin__")
        if origin is not Union:
            return False
        if not hasattr(t, "__args__"):
            return False
        args = getattr(t, "__args__")
        if len(args) != 2:
            return False
        if args[1] is not type(None):
            return False
        return True

    def parse_optional(self, t: Type):
        if not self.is_optional(t):
            return
        if self.is_builtin(t.__args__[0]):
            f = self.parse_builtin(t.__args__[0])
        elif self.is_model(t.__args__[0]):
            f = self.parse_model(t.__args__[0])
        else:
            return None
        f.nullable = True
        f.python_type = f'Optional[{f.python_type}]'
        return f

    def is_batch(self, t: Type):
        if self.is_builtin(t):
            return False
        if not hasattr(t, "__origin__"):
            return False
        origin = getattr(t, "__origin__")
        if origin is not list:
            return False
        return True

    def parse_batch(self, t: Type):
        if not self.is_batch(t):
            return None
        if self.is_model(t.__args__[0]):
            f = self.parse_model(t.__args__[0])
            f.sql_type = ""
            f.python_type = f'List[{f.python_type}]'
            f.nullable = True
            f.link.type = "many"
            return f

    def parse(self, f: FieldInfo):
        t = f.annotation
        res = self.parse_type(t)
        if self.is_builtin(t):
            if f.default is not PydanticUndefined:
                res.default = f.default
        return res

    def parse_type(self, t: Type):
        f = self.parse_builtin(t)
        if f is not None:
            return f
        f = self.parse_model(t)
        if f is not None:
            return f
        f = self.parse_optional(t)
        if f is not None:
            return f
        f = self.parse_batch(t)
        if f is not None:
            return f
