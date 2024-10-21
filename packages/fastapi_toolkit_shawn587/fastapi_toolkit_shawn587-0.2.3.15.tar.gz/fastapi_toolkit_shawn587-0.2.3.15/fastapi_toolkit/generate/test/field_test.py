import unittest
import datetime

from typing import Optional, List
from pydantic import BaseModel

from fastapi_toolkit.generate.field_helper import FieldHelper, FieldType, Link


class A(BaseModel):
    a: int


class B:
    a: int


class TesterFieldHelper(unittest.TestCase):
    def setUp(self):
        self.fh = FieldHelper()

    def test_builtin(self):
        self.assertEqual(True, self.fh.is_builtin(str))
        self.assertEqual(True, self.fh.is_builtin(int))
        self.assertEqual(True, self.fh.is_builtin(float))
        self.assertEqual(True, self.fh.is_builtin(bool))
        self.assertEqual(True, self.fh.is_builtin(bytes))
        self.assertEqual(False, self.fh.is_builtin(A))
        self.assertEqual(False, self.fh.is_builtin(B))

    def test_model(self):
        self.assertEqual(True, self.fh.is_model(A))
        self.assertEqual(False, self.fh.is_model(B))
        self.assertEqual(False, self.fh.is_model(int))

    def test_optional(self):
        self.assertEqual(True, self.fh.is_optional(Optional[A]))
        self.assertEqual(False, self.fh.is_optional(A))
        self.assertEqual(True, self.fh.is_optional(Optional[int]))
        self.assertEqual(False, self.fh.is_optional(int))

    def test_batch(self):
        self.assertEqual(True, self.fh.is_batch(List[A]))
        self.assertEqual(True, self.fh.is_batch(List[int]))
        self.assertEqual(True, self.fh.is_batch(List[B]))
        self.assertEqual(False, self.fh.is_batch(int))
        self.assertEqual(False, self.fh.is_batch(A))
        self.assertEqual(False, self.fh.is_batch(B))

    def test_explicit_parse(self):
        tests = [
            (FieldType(python_type='str', sql_type='sqltypes.Text'), self.fh.parse_builtin(str)),
            (FieldType(python_type='int', sql_type='sqltypes.Integer'), self.fh.parse_builtin(int)),
            (FieldType(python_type='float', sql_type='sqltypes.Float'), self.fh.parse_builtin(float)),
            (FieldType(python_type='bool', sql_type='sqltypes.Boolean'), self.fh.parse_builtin(bool)),
            (FieldType(python_type='bytes', sql_type='sqltypes.LargeBinary'), self.fh.parse_builtin(bytes)),

            (FieldType(python_type='A', link=Link(model="A", type="one")), self.fh.parse_model(A)),
            (None, self.fh.parse_model(int)),
            (None, self.fh.parse_model(B)),

            (FieldType(python_type='Optional[A]', link=Link(model="A", type="one"), nullable=True),
             self.fh.parse_optional(Optional[A])),
            (None, self.fh.parse_optional(Optional[B])),

            (FieldType(python_type='List[A]', link=Link(model="A"), type="many"), self.fh.parse_batch(List[A])),
            (None, self.fh.parse_batch(List[B])),
            (None, self.fh.parse_batch(List[int])),
        ]
        for want, got in tests:
            self.assertEqual(want, got)

    def test_parse(self):
        tests = [
            (FieldType(python_type='str', sql_type='sqltypes.Text'), str),
            (FieldType(python_type='int', sql_type='sqltypes.Integer'), int),
            (FieldType(python_type='float', sql_type='sqltypes.Float'), float),
            (FieldType(python_type='bool', sql_type='sqltypes.Boolean'), bool),
            (FieldType(python_type='bytes', sql_type='sqltypes.LargeBinary'), bytes),

            (FieldType(python_type='datetime.datetime', sql_type='sqltypes.DateTime', depends=['datetime']),
             datetime.datetime),
            (FieldType(python_type='datetime.date', sql_type='sqltypes.Date', depends=['datetime']),
             datetime.date),

            (FieldType(python_type='A', link=Link(model="A", type="one")), A),
            (None, B),

            (FieldType(python_type='Optional[A]', link=Link(model="A", type="one"), nullable=True), Optional[A]),
            (None, Optional[B]),

            (FieldType(python_type='List[A]', link=Link(model="A", type="many"), nullable=True), List[A]),
            (None, List[B]),
        ]

        for want, got in tests:
            self.assertEqual(want, self.fh.parse(got))


if __name__ == '__main__':
    unittest.main()
