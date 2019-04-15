from src.data_objects.Report import Report
from src.data_objects.Machine import Machine
from tqdm import tqdm


def create_report(machine_one, machine_two, beginning_time, sice_of_time_window):
    calculated_similarity = create_report_of_given_window(machine_one, machine_two,
                                                          beginning_time, sice_of_time_window)
    return Report(machine_one, machine_two, calculated_similarity)


def calculate_similarity(first_status_time_line, second_status_time_line, displace_in_seconds):
    number_of_similar_fields = 0
    range_of_compared_fields = len(first_status_time_line)  # - displace_in_seconds

    for i in range(range_of_compared_fields):
        if second_status_time_line[i + displace_in_seconds] == first_status_time_line[i]:
            number_of_similar_fields = number_of_similar_fields + 1

    return (number_of_similar_fields / range_of_compared_fields) * 100


def create_report_of_given_window(first_status_time_line, second_status_time_line, beginning_time, sice_of_time_window):
    range_of_comparison = len(second_status_time_line) - (beginning_time + sice_of_time_window)
    report = []
    for i in tqdm(range(range_of_comparison)):
        report.append(calculate_similarity_of_window(first_status_time_line, second_status_time_line, beginning_time,
                                                     sice_of_time_window, i))

    return report


def calculate_similarity_of_window(first_status_time_line, second_status_time_line, begin, window_slice, displace):
    trimmed_window = first_status_time_line[begin:(window_slice + begin)]

    return calculate_similarity(trimmed_window, second_status_time_line, displace)
