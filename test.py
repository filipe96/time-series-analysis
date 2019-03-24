import unittest

from timeDisplaced import *


class MyFirstTests(unittest.TestCase):

    def test_calculate_similarity_with_100_equal_data_set(self):
        machine_one = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two = [0, 0, 0, 1, 0, 0, 0, 1]

        self.assertEqual(calculate_similarity(machine_one, machine_two), 100)

    def test_calculate_similarity_with_100_not_equal_data_set(self):
        machine_one = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two = [0, 0, 1, 0, 0, 0, 1, 0]

        self.assertEqual(calculate_similarity(machine_one, machine_two), 50)

    def test_manipulate_range_of_array(self):  # TODO: write more generic with variable index
        machine_one = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]
        factor = -1

        expected = [0, 0, 0, 1, 0, 0, 0, 1, 0]
        self.assertEqual(cut_away_fields_outside_of_timezone(machine_one, factor), expected)

        machine_two = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]
        factor = 1

        expected2 = [0, 0, 1, 0, 0, 0, 1, 0, 1]
        self.assertEqual(cut_away_fields_outside_of_timezone(machine_two, factor), expected2)

    def test_compare_two_time_series(self):
        machine_one = [0, 0, 1]
        machine_two = [1, 0, 0]

        report = [33.33333333333333, 0, 100]
        self.assertEqual(compare_time_series(machine_one, machine_two), report)
