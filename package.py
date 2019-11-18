class package:
    def __init__(self):
        self.o = ""
        self.s = ""
        self.i = ""
        self.data = []
        self.end = ""

    def set_o(self, operation):
        self.o = operation

    def set_s(self, status):
        self.s = status

    def set_i(self, session_id):
        self.i = session_id

    def add_data(self, number):
        self.data.append(number)

    def set_end(self, end):
        self.end = end
