import pandas as pd

file_path = "data/a_ereignis_02.csv"
delimiter = "|"
machine_name = "BFD1ERF1"


def get_machine_time_series_data():
    data = read_file(file_path, delimiter)
    filtered_data_frame = filter_data_frame(data, machine_name)
    return build_time_series_list(filtered_data_frame)


def read_file(file, delim):
    dataframe = pd.read_csv(filepath_or_buffer=file, delimiter=delim)
    return dataframe


def filter_data_frame(df, machine_name):
    table = df[['$COLUMNS$MASCH_NR', 'BEGIN_ZEIT', 'ENDE_ZEIT', 'BEGIN_DAT', 'STOERTXT_NR']]
    table.columns = ['MashineID', 'StartTime', 'FinishTime', 'Date', 'MashineState']
    table = table[['MashineID', 'StartTime', 'FinishTime', 'Date', 'MashineState']]
    table = table[table['MashineID'] == machine_name]
    table = table[table['Date'] == '08/09/2013']
    table = table[table['MashineState'] == 2]
    return table.sort_values(by=['StartTime'])


def build_time_series_list(filtered_data_frame):
    machine_status_time_line = initialize_empty_dictionary()
    machine_status_time_line = fill_up_dictionary(filtered_data_frame, machine_status_time_line)
    return machine_status_time_line


def initialize_empty_dictionary():
    keys = range(86400)
    machine_status_time_line = {}
    for i in keys:
        machine_status_time_line[i] = 0
    return machine_status_time_line


def fill_up_dictionary(filtered_data_frame, dictionary):
    for index, row in filtered_data_frame().iterrows():
        for x in range(row['StartTime'], row['FinishTime'] + 1, 1):
            dictionary[x] = 1
    return dictionary


def transform_to_list(dictionary):
    pure_data = []
    for i in dictionary:
        pure_data.append(dictionary[i])

    return pure_data
