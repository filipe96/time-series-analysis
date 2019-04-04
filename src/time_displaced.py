from src.data_objects.Report import Report


def create_report(machine_one, machine_two):
    calculated_similarity = compare_time_series(machine_one.machine_data, machine_two.machine_data)
    return Report(machine_one, machine_two, calculated_similarity)

def cut_away_fields_outside_of_timezone(status_time_line, factor):

    if factor < 1:
        status_time_line.pop(len(status_time_line) - 1)
    else:
        status_time_line.pop(0)

    return status_time_line


def compare_time_series(first_status_time_line, second_status_time_line):
    report = []

    for i in range(len(first_status_time_line)):
        report.append(calculate_similarity(first_status_time_line, second_status_time_line, i))

    return report

def calculate_similarity(first_status_time_line, second_status_time_line, displace_in_seconds):
    number_of_similar_fields = 0
    range_of_compared_fields = len(first_status_time_line) - displace_in_seconds

    for i in range(range_of_compared_fields):
        if first_status_time_line[i + displace_in_seconds] == second_status_time_line[i]:
            number_of_similar_fields = number_of_similar_fields + 1

    return number_of_similar_fields / range_of_compared_fields * 100