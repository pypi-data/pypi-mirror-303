import unittest
from fastapi_toolkit.configer import Configer


class ConfigerTest(unittest.TestCase):
    def test_init(self):
        configer = Configer('test_configer.yaml')
        self.assertIsInstance(configer, Configer)

    def test_get_value(self):
        configer = Configer('test_configer.yaml')
        self.assertEqual(configer['key'], 'value')

    def test_get_inner_value(self):
        configer = Configer('test_configer.yaml')
        self.assertEqual(configer['keyA.keyB.keyC'], 'inner_value')

    def test_get_none(self):
        configer = Configer('test_configer.yaml')
        self.assertEqual(configer['key.none'], None)

    def test_get_inner_dict(self):
        configer = Configer('test_configer.yaml')
        self.assertEqual(configer['arr.2'], {'k': 'v'})

    def test_get_list_value(self):
        configer = Configer('test_configer.yaml')
        self.assertEqual(configer['arr.0'], 1)

    def test_get_list_overflow(self):
        configer = Configer('test_configer.yaml')
        self.assertEqual(configer['arr.3'], None)

    def test_get_inner_list_value(self):
        configer = Configer('test_configer.yaml')
        self.assertEqual(configer['keyA.keyB.arr'], [1, 2, 3])
