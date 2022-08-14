class Process:

    def __init__(self, __id, process_duration):
        self._id = id
        self._process_duration = process_duration

    def get_id(self):
        return self._id

    def get_process_duration(self):
        return self._process_duration
