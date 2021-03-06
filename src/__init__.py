from src.data_extractor import get_machine_time_series_data
import matplotlib.pyplot as plt
import numpy as nu
from time_displaced import *


# ['BFD1ERF1' 'BFD1FUE1' 'BFD1AR01' 'BFL3KW01' 'BFO4FUE1' 'BFL6AP01'
# 'BFL6KW01' 'BFO4EL41' 'BFO4BL41' 'WFL1KW01' 'BFL6EP01' 'BFL2INS1'
# 'WFL1RM01' 'BFL3ETI1' 'BFO4EL01' 'BFO4EP01' 'BFL6EK01' 'BFL2FUE1'
# 'BFL6ETI3' 'BFL6RM01' 'BFO4ETI1' 'BFO4KT02' 'BFL3EK02' 'BFL3FUE1'
# 'BFL3EK01' 'BFO4EP41' 'BFL6BL01' 'BFL2BL01' 'BFO4RM01' 'BFO4BL01'
# 'BFL2AP01' 'BFO4AP41' 'BFL3EL01' 'BFL3EP01' 'WFL1AR01' 'BFL2EL01'
# 'BFO4PT01' 'BFO4ETI2' 'BFL3BL01' 'WFL1BL01' 'WFL1FUE1' 'BFL5SR01'
# 'BFL3PA01' 'BFL6FT01' 'BFL6FBE1' 'BK01EL01' 'BFL5FT01' 'BFL2INS2'
# 'BK01KAZ1' 'WFL1LGK1' 'BFL6EL01' 'BFL6KT01' 'BFO4FBE1' 'BFL3ETI2'
# 'BFO4AP02' 'BFL6ETI1' 'BFL2RM01' 'BFL2ETI2' 'BFL3RM01' 'BFL3AP01'
# 'BFL2EP01' 'BFL5ETI1' 'BFL5FUE1' 'WFL1ETI1' 'BFL6ETI2' 'BFL3AR01'
# 'BK01LW01' 'BFL5PT01' 'BFL6MV01' 'WFL1KZE1' 'BFL5AR01' 'BFL5INS1'
# 'BFL2ETI1' 'BFL6LGK1' 'BK01VW01' 'BK01KK01' 'BK01KAS1' 'BFL5MV01'
# 'BFL3VKK1' 'WFL1KT01' 'BFL3INS2' 'BFO4INS2' 'BFL3LGK4' 'WFL1EL01'
# 'BK01AW01' 'BFL6LKK1' 'BFL2KT01' 'BFL2KT02' 'BFL2PM01' 'BFL2PT01'
# 'BFL3FT01' 'BFL3FT02' 'BFL6INS1' 'BFL3FBE1' 'BK01FUE1' 'BK02FUE1'
# 'BUP1FUE1' 'BFL5KT01' 'BFL3MV01' 'BK01VR01' 'BK01KT01' 'WFL1FT01'
# 'WFL1EP01' 'WFL1CIP1' 'WFL1AP01' 'BFL6FUE1' 'BFO4EP02' 'BFL2KM01'
# 'BFL6AR01' 'BFL3VKK2' 'BFL3LGK1' 'BFL3LGK2' 'BK01HR01' 'BFL5EP01'
# 'BFO4INS1' 'BFL3LKK1' 'BFL6KE01' 'BFL6SR01' 'BFL3KT01' 'BFL3KT02'
# 'BFO4KM01' 'BFO4KT01' 'BFL6VKK1' 'BFO4LGK1' 'BFO4EK01' 'BFL3PT01'
# 'BFO4MV01' 'BFL3SOR1' 'BFL3SOR2' 'WFL1LKK1' 'BFO4PM01' 'BFL6PA01'
# 'BFL3LGK3' 'BFL5EP02' 'BFL5BL01' 'BFL5HS01' 'BK01KD01' 'BK01FS01'
# 'BK01FS02' 'BK01LK01' 'BK01FB01' 'BK01FB02' 'BK01MV01' 'BFL5HS02'
# 'BFL3LKK2' 'BFL2FBE1' 'BFL2MV01' 'BFO4AP01' 'BK01BL01' 'BFL3INS1'
# 'BFO4SOR1' 'BFO4LGK2' 'BFL5FB01' 'BFL3SOR3']

def main():
    # time_series_second_machine = get_machine_time_series_data("../data/a_ereignis_02.csv", "|", "BFO4AP01")
    # time_series_first_machine = get_machine_time_series_data("../data/a_ereignis_02.csv", "|", "BFO4AP02")
    machine_name_two = 'BFO4ETI1'
    machine_name_one = 'BFO4ETI2'
    starting_point: int = 2000
    window_size = 600
    range_of_search = 84000  # 2000

    time_series_first_machine = get_machine_time_series_data("../data/a_ereignis_02.csv", "|", machine_name_one)
    time_series_second_machine = get_machine_time_series_data("../data/a_ereignis_02.csv", "|", machine_name_two)
    machine_one = Machine(machine_name_one, time_series_first_machine)
    machine_two = Machine(machine_name_two, time_series_second_machine)

    report = create_report(machine_one.machine_data, machine_two.machine_data, starting_point, window_size,
                           range_of_search)
    print(report.calculated_similarity)
    print(max(report.calculated_similarity))
    t = nu.arange(0.0, len(report.calculated_similarity), 1)
    plt.plot(t, report.calculated_similarity, )
    plt.style.use("fast")
    # plt.plot('Item (s)')
    plt.ylabel('Similarity in percent')
    plt.xlabel('Displace in Seconds')
    plt.title(
        'Main machine: ' + machine_name_one + '\n' +
        'compared machine: ' + machine_name_two + '\n' +
        'starting Point: ' + str(starting_point) +
        '  Window Size: ' + str(window_size)
    )

    plt.grid(True)
    plt.ylim(0, 100)
    plt.tight_layout()
    image_name = machine_name_one + machine_name_two + str(starting_point) + str(window_size) + str(range_of_search)
    plt.savefig(fname=image_name)
    plt.show()

    # plt.figure(41)
    # plt.hist(report.calculated_similarity, 20)
    # plt.show()


if __name__ == '__main__':
    main()
