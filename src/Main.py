import DataGenerator
import StaticConstants

DataGenerator.DataGenerator.create_process()
DataGenerator.DataGenerator.create_client()
DataGenerator.DataGenerator.create_desk()


def _flow():
    desk_list = StaticConstants.StaticConstants.desk_list

    while len(StaticConstants.StaticConstants.client_queue) > 0:

        least_waiting_time = 0

        for i in range(len(desk_list)):

            if desk_list[i].get_desk_waiting_time() < desk_list[least_waiting_time].get_desk_waiting_time():
                least_waiting_time = i

        if len(StaticConstants.StaticConstants.client_queue) > 1:

            desk_list[least_waiting_time].set_desk_waiting_time(
                StaticConstants.StaticConstants.client_queue.pop(0).get_process().get_process_duration())

        else:

            StaticConstants.StaticConstants.client_queue.pop(0)
            print("Desk " + str(least_waiting_time + 1) + ", " + str(
                desk_list[least_waiting_time].get_desk_waiting_time()) +
                  " minutes")


_flow()
