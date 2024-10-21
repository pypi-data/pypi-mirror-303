import datetime
import enum
import uuid
from typing import Type, Tuple, Optional

import pydantic
from sqlalchemy.sql import sqltypes


def mapping(t) -> Tuple[bool, Optional[str]]:
    type_map = {
        int: sqltypes.Integer,
        float: sqltypes.Float,
        str: sqltypes.Text,
        bool: sqltypes.Boolean,
        bytes: sqltypes.LargeBinary,
        bytearray: sqltypes.LargeBinary,

        datetime.datetime: sqltypes.DateTime,
        datetime.date: sqltypes.Date,
        datetime.timedelta: sqltypes.Interval,
    }
    if t in type_map:
        return False, 'sqltypes.' + type_map[t].__name__
    if issubclass(t, enum.Enum):
        # TODO: check database is postgresql
        return True, f'dialects.postgresql.ENUM({t.__name__})'
    return True, None
