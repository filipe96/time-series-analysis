import unittest
from src.data_objects.Machine import Machine
from src.timeDisplaced import *

class MyFirstTests(unittest.TestCase):

    def test_calculate_similarity_with_100_equal_data_set(self):
        machine_one_data = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_one_name = "DB02"
        machine_two_data = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two_name = "DB03"

        machine_one = Machine(machine_one_name, machine_one_data)

        machine_two = Machine(machine_two_name, machine_two_data)

        self.assertEqual(calculate_similarity(machine_one.get_machine_data(), machine_two.get_machine_data()), 100)

    def test_calculate_similarity_with_100_not_equal_data_set(self):
        machine_one = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two = [0, 0, 1, 0, 0, 0, 1, 0]

        self.assertEqual(calculate_similarity(machine_one, machine_two), 50)

    def test_manipulate_range_of_array(self):
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

    def test_create_report(self):
        machine_one_data = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_one_name = "DB02"
        machine_two_data = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two_name = "DB03"

        machine_one = Machine(machine_one_name, machine_one_data)

        machine_two = Machine(machine_two_name, machine_two_data)

        expected_report = Report(machine_one, machine_two, [100.0, 57.14285714285714, 50.0, 40.0, 100.0, 66.66666666666666, 50.0, 0.0])

        created_report = create_report(machine_one, machine_two)

        self.assertEqual(created_report.first_machine.machine_name, expected_report.first_machine.machine_name)
        self.assertEqual(created_report.calculated_similarity, expected_report.calculated_similarity)
