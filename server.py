import socket
import time
import random
import sys
from package import package


listeningAddress = ("", 20001)
UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo
UDPSocket.bind(listeningAddress)

p1 = package()
print(time.ctime())
session_id = random.randint(1000, 10000)
while True:

    # odebranie komunikatu
    bytesAddressPair = UDPSocket.recvfrom(1024)
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1][0]

    # identyfikator sesji

    p1.set_i(session_id)
    p1.set_s("ACK")
    # wyswietlenie komunikatu
    print(time.ctime())
    print("Message from client:", message)
    p1.set_t()
    response = p1.return_packet
    UDPSocket.sendto(response.encode(), bytesAddressPair[1])


    # odczytanie operacji komunikatu
    c_message = message.split("#")
    for x in c_message:
        if x != "":
            y = x.split("->")
            if y[0] == "o":
                p1.set_o(y[1])


    if p1.o == "A":

        for x in c_message:
            if x != "":
                y = x.split("->")
                if y[0] == "d1":
                    p1.set_data1(y[1])
                elif y[0] == "d2":
                    p1.set_data2(y[1])

        if p1.data2 == "0":
            p1.set_s("error")
            p1.set_t()
            response = p1.return_packet

        else:
            d3 = int(p1.data1) % int(p1.data2)
            p1.set_data3(d3)
            p1.set_s("OK")
            p1.set_t()
            response = p1.return_packet_response

        print("Message to client:", response)
        UDPSocket.sendto(response.encode(), bytesAddressPair[1])
        p1 = package()

    elif p1.o == "a":

        for x in c_message:
            if x != "":
                y = x.split("->")
                if y[0] == "d1":
                    p1.set_data1(y[1])
                elif y[0] == "d2":
                    p1.set_data2(y[1])
        if p1.data2 < p1.data1 :
            p1.set_s("error")
            p1.set_t()
            response = p1.return_packet
        else:
            d3 = random.randint(int(p1.data1), int(p1.data2))
            p1.set_data3(d3)

        p1.set_s("OK")
        p1.set_t()
        response = p1.return_packet_response
        print("Message to client:", response)
        UDPSocket.sendto(response.encode(), bytesAddressPair[1])
        p1 = package()

    elif p1.o == "D":

        for x in c_message:
            if x != "":
                y = x.split("->")
                if y[0] == "d1":
                    p1.set_data1(y[1])
                elif y[0] == "d2":
                    p1.set_data2(y[1])
        d3 = int(p1.data1) + int(p1.data2)
        p1.set_data3(d3)

        p1.set_s("OK")
        p1.set_t()
        response = p1.return_packet_response
        print("Message to client:", response)
        UDPSocket.sendto(response.encode(), bytesAddressPair[1])
        p1 = package()

    elif p1.o == "O":

        for x in c_message:
            if x != "":
                y = x.split("->")
                if y[0] == "d1":
                    p1.set_data1(y[1])
                elif y[0] == "d2":
                    p1.set_data2(y[1])
        d3 = int(p1.data1) - int(p1.data2) #oczekiwanie 20ms
        p1.set_data3(d3)

        p1.set_s("OK")
        p1.set_t()
        response = p1.return_packet_response
        print("Message to client:", response)
        UDPSocket.sendto(response.encode(), bytesAddressPair[1])
        p1 = package()

    elif p1.o == "SM":
        end = 0
        for x in c_message:
            if x != "":
                y = x.split("->")
                if y[0] == "d1":
                    p1.add_data(y[1])
                    if y[1] == "blad":
                        p1.set_s("inv_arg")
                if y[0] == "e":
                    end = y[1]
        if p1.s != "inv_arg":
            p1.set_s("OK")
        p1.set_s("ACK")
        p1.set_t()
        response = p1.return_packet_response_sort(number)
        print("Message to client:", response)
        UDPSocket.sendto(response.encode(), bytesAddressPair[1])

        while end == "0":
            number = number +1
            bytesAddressPair = UDPSocket.recvfrom(1024)
            message = bytesAddressPair[0].decode()
            print("Message from Client:", message)
            p1.set_s("ACK")
            c_message = message.split("#")
            for x in c_message:
                if x != "":
                    y = x.split("->")
                    if y[0] == "d1":
                        p1.add_data(y[1])
                    if y[0] == "e":
                        end = y[1]
            p1.set_s("ACK")
            p1.set_t()
            response = p1.return_packet_response_sort(number)
            print("Message to client:", response)
            UDPSocket.sendto(response.encode(), bytesAddressPair[1])
        if end == "1":
            p1.data_tab = sorted(p1.data_tab, key=int, reverse=True)
            number = -1
            for x in p1.data_tab:
                number = number+1
                p1.set_s("OK")
                p1.set_t()
                response = p1.return_packet_response_sort(number)
                print("Message to client:", response)
                UDPSocket.sendto(response.encode(), bytesAddressPair[1])
                time.sleep(0.2)
                UDPSocket.recvfrom(1024)
                #we are waiting for aACKKKKK
        p1 = package()



    elif p1.o == "SR":
        end = 0
        number = 0

        for x in c_message:
            if x != "":
                y = x.split("->")
                if y[0] == "d1":
                    p1.add_data(y[1])

                    if y[1] == "blad":
                        p1.set_s("inv_arg")

                if y[0] == "e":
                    end = y[1]
        if p1.s != "inv_arg":
            p1.set_s("OK")
        p1.set_t()
        response = p1.return_packet_response_sort(number)
        print("Message to client:", response)
        UDPSocket.sendto(response.encode(), bytesAddressPair[1])

        while end == "0":
            number = number +1
            bytesAddressPair = UDPSocket.recvfrom(1024)
            message = bytesAddressPair[0].decode()
            print("Message from Client:", message)

            c_message = message.split("#")
            p1.set_s("ACK")
            response = p1.return_packet
            UDPSocket.sendto(response.encode(), bytesAddressPair[1])
            for x in c_message:
                if x != "":
                    y = x.split("->")
                    if y[0] == "d1":
                        p1.add_data(y[1])
                    if y[0] == "e":
                        end = y[1]
            p1.set_s("OK")
            p1.set_t()
            p1.data_tab = sorted(p1.data_tab, key=int)
            response = p1.return_packet_response_sort(number)
            print("Message to client:", response)
            UDPSocket.sendto(response.encode(), bytesAddressPair[1])
            time.sleep(0.2)
            UDPSocket.recvfrom(1024)

        p1 = package()
