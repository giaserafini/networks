import time
import sys


class package:
    def __init__(self):
        self.o = ""
        self.s = ""
        self.i = ""
        self.t = ""
        self.x = ""
        self.data1 = 0
        self.data2 = 0
        self.data3 = 0
        self.data_tab = []
        self.end = 0

    def set_o(self, operation):
        self.o = operation

    def set_s(self, status):
        self.s = status

    def set_i(self, session_id):
        self.i = session_id

    def set_x(self, ack):
        self.x = ack

    def set_t(self):
        self.t = time.ctime()

    def set_time(self, tim):
        self.t = tim

    def set_data1(self, number):
        self.data1 = number

    def set_data2(self, number):
        self.data2 = number

    def set_data3(self, number):
        self.data3 = number

    def add_data(self, number):
        self.data_tab.append(number)

    def set_end(self, end):
        self.end = end

    @property
    def return_packet(self):
        packet = "o->{0}#d1->{1}#d2->{2}#s->{3}#i->{4}#t->{5}#".format(str(self.o), str(self.data1), str(self.data2), str(self.s), str(self.i), str(self.t))
        return packet

    @property
    def return_packet_sort(self):
        packet = "o->{0}#d1->{1}#s->{2}#i->{3}#t->{4}#e->{5}#".format(str(self.o), str(self.data1), str(self.s), str(self.i), str(self.t), str(self.end))
        return packet

    @property
    def return_packet_response(self):
        packet = "o->{0}#d3->{1}#s->{2}#i->{3}#t->{4}#".format(str(self.o), str(self.data3), str(self.s), str(self.i), str(self.t))
        return packet

    def return_packet_response_sort(self, number):
        packet = "o->{0}#d->{1}#s->{2}#i->{3}#t->{4}#".format(str(self.o), str(self.data_tab[number]), str(self.s),
                                                              str(self.i),
                                                              str(self.t))
        return packet

    @property
    def return_packet_response_sort_exc(self):

        packet = "o->{1}#d3->{2}#s->{3}#i->{4}#t->{5}#".format(str(self.o), str(self.data3),
                                                                      str(self.s), str(self.i), str(self.t))
        return packet
