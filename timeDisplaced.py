def calculate_similarity(first_array, second_array):
    number_of_similar_fields = 0

    for i in range(len(first_array)):
        if first_array[i] == second_array[i]:
            number_of_similar_fields = number_of_similar_fields + 1

    return number_of_similar_fields / len(first_array) * 100


def cut_away_fields_outside_of_timezone(status_time_line, factor):
    if factor < 1:
        status_time_line.pop(len(status_time_line) - 1)
    else:
        status_time_line.pop(0)

    return status_time_line


def compare_time_series(first_status_time_line, second_status_time_line):
    report = []
    for i in range(len(first_status_time_line)):
        report.append(calculate_similarity(first_status_time_line, second_status_time_line))
        cut_away_fields_outside_of_timezone(first_status_time_line, 1)
        cut_away_fields_outside_of_timezone(second_status_time_line, -1)

    return report
