class Client:

    def __init__(self, name, process):

        self._name = name
        self._process = process

    def get_name(self):
        return self._name

    def get_process(self):
        return self._process
