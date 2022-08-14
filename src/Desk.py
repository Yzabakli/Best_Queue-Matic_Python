class Desk:

    def __init__(self, desk_number):
        self._desk_number = desk_number
        self._desk_waiting_time = 0

    def get_desk_number(self):
        return self._desk_number

    def set_desk_waiting_time(self, value):
        self._desk_waiting_time = self._desk_waiting_time + value

    def get_desk_waiting_time(self):
        return self._desk_waiting_time

