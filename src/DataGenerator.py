import Client
import Desk
import Process
from StaticConstants import StaticConstants


class DataGenerator:

    @classmethod
    def create_process(cls):
        StaticConstants.process_list.append(Process.Process("A", 5))
        StaticConstants.process_list.append(Process.Process("B", 3))
        StaticConstants.process_list.append(Process.Process("C", 7))
        StaticConstants.process_list.append(Process.Process("D", 10))

    @classmethod
    def create_client(cls):
        StaticConstants.client_queue.append(Client.Client("Drogba", StaticConstants.process_list[0]))
        StaticConstants.client_queue.append(Client.Client("Cantona", StaticConstants.process_list[0]))
        StaticConstants.client_queue.append(Client.Client("Ronaldinho", StaticConstants.process_list[1]))
        StaticConstants.client_queue.append(Client.Client("Zidane", StaticConstants.process_list[2]))
        StaticConstants.client_queue.append(Client.Client("Cruyff", StaticConstants.process_list[3]))
        StaticConstants.client_queue.append(Client.Client("Ronaldo", StaticConstants.process_list[1]))
        StaticConstants.client_queue.append(Client.Client("Baggio", StaticConstants.process_list[2]))

    @classmethod
    def create_desk(cls):
        StaticConstants.desk_list.append(Desk.Desk(1))
        StaticConstants.desk_list.append(Desk.Desk(2))
        StaticConstants.desk_list.append(Desk.Desk(3))
