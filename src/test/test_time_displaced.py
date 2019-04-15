import unittest
from src.time_displaced import *


class Test_time_displaced(unittest.TestCase):

    def test_calculate_similarity_with_100_equal_data_set(self):
        machine_one_data = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_one_name = "DB02"
        machine_two_data = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two_name = "DB03"

        machine_one = Machine(machine_one_name, machine_one_data)

        machine_two = Machine(machine_two_name, machine_two_data)

        self.assertEqual(calculate_similarity(machine_one.get_machine_data(), machine_two.get_machine_data(), 0), 100)

    def test_calculate_similarity_with_100_not_equal_data_set(self):
        machine_one = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two = [0, 0, 1, 0, 0, 0, 1, 0]

        self.assertEqual(calculate_similarity(machine_one, machine_two, 0), 50)

    def test_create_report(self):
        machine_one_data = [1, 0, 0, 0]
        machine_one_name = "DB02"
        machine_two_data = [0, 0, 0, 1, 0, 0, 0, 1]
        machine_two_name = "DB03"

        machine_one = Machine(machine_one_name, machine_one_data)

        machine_two = Machine(machine_two_name, machine_two_data)

        expected_report = Report(machine_one, machine_two, [66.66666666666666,
                                                            33.33333333333333,
                                                            33.33333333333333,
                                                            100.0,
                                                            66.66666666666666])

        created_report = create_report(machine_one.machine_data, machine_two.machine_data, 0, 3)
        self.assertEqual(created_report.calculated_similarity, expected_report.calculated_similarity)

    def test_compare_to_machines_with_given_offset(self):
        machine_one_data = [0, 1]
        machine_one_name = "DB02"
        machine_two_data = [0, 0, 1]
        machine_two_name = "DB03"

        machine_one = Machine(machine_one_name, machine_one_data)
        machine_two = Machine(machine_two_name, machine_two_data)

        self.assertEqual(calculate_similarity(machine_one.machine_data, machine_two.machine_data, 0), 50)
        self.assertEqual(calculate_similarity(machine_one.machine_data, machine_two.machine_data, 1), 100)

    def test_compare_data_in_given_window(self):
        machine_one_data = [1, 1, 0, 0, 0, 0, 0, 0]
        machine_one_name = "DB02"
        machine_two_data = [0, 0, 0, 1, 1, 0, 0, 0]
        machine_two_name = "DB03"

        machine_one = Machine(machine_one_name, machine_one_data)
        machine_two = Machine(machine_two_name, machine_two_data)

        self.assertEqual(create_report_of_given_window(machine_one.machine_data, machine_two.machine_data, 0, 4),
                         [25.0, 0.0, 50.0, 100.0])

    def test_calculate_similarity_of_window(self):
        machine_one_data = [1, 1, 0, 0, 0, 0, 0, 0]
        machine_one_name = "DB02"
        machine_two_data = [0, 0, 0, 1, 1, 0, 0, 0]
        machine_two_name = "DB03"

        machine_one = Machine(machine_one_name, machine_one_data)
        machine_two = Machine(machine_two_name, machine_two_data)

        self.assertEqual(calculate_similarity_of_window(machine_one.machine_data, machine_two.machine_data, 0, 4, 3),
                         100)


if __name__ == '__main__':
    unittest.main()
