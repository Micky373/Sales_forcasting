import os
import sys
import unittest
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

sys.path.append('..')
from scripts.data_cleaning import DataCleaner


class TestDataCleaner(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.cleaner = DataCleaner()

    def test_remove_cols(self):
        df = pd.DataFrame({'col1': [1, 2, 1], 'col2': [3, 4, 3]})
        df = self.cleaner.remove_cols(df)
        self.assertEqual(df.shape, (2, 1))

    def test_convert_to_datetime(self):
        df = pd.DataFrame({'col1': ["2018-01-05", "2018-01-06"]})
        df = self.cleaner.convert_to_datetime(df, ['col1'])
        self.assertTrue(type(df['col1'].dtype == ptypes.DatetimeTZDtype))

    def test_convert_to_numbers(self):

        df = pd.DataFrame({'col1': ["1", "2"]})
        df = self.cleaner.convert_to_numbers(df, ['col1'])
        self.assertTrue(types.is_int64_dtype(df['col1']))

    def test_convert_to_boolean(self):
        df = pd.DataFrame({'col1': [1, 0, 0, 1]})
        df = self.cleaner.convert_to_boolean(df, ['col1'])
        self.assertTrue(types.is_bool_dtype(df['col1']))

    def test_convert_to_string(self):
        df = pd.DataFrame({'col1': ["love", "owesome"]})
        df = self.cleaner.convert_to_string(df, ['col1'])
        self.assertTrue(df['col1'].dtype == "string")


if __name__ == '__main__':
    unittest.main()