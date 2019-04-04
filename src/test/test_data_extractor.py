import unittest

from src.data_extractor import read_file


class TestDataExtractor(unittest.TestCase):

    def test_read_file(self):
       a = read_file("../../data/a_ereignis_02.csv", "|")
       self.assertFalse(a.empty)


