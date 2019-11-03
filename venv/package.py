class package:
    def __init__(self, o, s, i, data, end):
        self.o = ""
        self.s = 0
        self.i = 0
        self.data = 0
        self.end = 0

    def set_o(self, operation):
        self.o = operation

    def set_s(self, status):
        self.s = status

    def set_i(self, session_id):
        self.i = session_id
