import socket
import sys
import uuid
import time
import random
import datetime
from package import package


def operation(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '%':
        return number1 % number2


def insertion_sort(sorted_list): #rosnaco
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1
        while j >= 0 and key > sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key
        return sorted_list
    sorted_list = insertion_sort()


IP = "127.0.0.1"
Port = 20001
listeningAddress = (IP, Port)
session_id = uuid.uuid1()  # identyfikator sesji

UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo
UDPSocket.bind(listeningAddress)

p1 = package()

print("I'm listening to you")
print(time.ctime())
while True:

    # odebranie komunikatu
    bytesAddressPair = UDPSocket.recvfrom(1024)
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1][0]
    p1.set_i(session_id)


    print(time.ctime())
    print("Message from Client:", message)
    print("Client IP Address:", address)
    print(bytesAddressPair)

    # odczytanie komunikatu
    c_message = message.split("#")
    for x in c_message:
        if x != "":
            y = x.split("->")
            if y[0] == "o":
                p1.set_o(y[1])
            elif y[0] == "s":
                p1.set_s(y[1])
            elif y[0] == "i":
                p1.set_i(y[1])
            elif y[0] == "d":
                p1.add_data(y[1])
            elif y[0] == "e":
                p1.set_end(y[1])

    if p1.end == "1":
        p1.set_s("OK")

        if p1.o == "A":
            number1 = int(p1.data[0])
            number2 = int(p1.data[1])
            print(number1 % number2)
        elif p1.o == "B":
            number1 = int(p1.data[0])
            number2 = int(p1.data[1])
            print(number1 + number2)
        elif p1.o == "C":
            number1 = int(p1.data[0])
            number2 = int(p1.data[1])
            print(number1 - number2)

        elif p1.o == "a":
            a = int(p1.data[0])
            b = int(p1.data[1])
            print(random.randint(a, b))

        elif p1.o == "SR":
            print(session_id)
            print('\nThe sorted list: \t', sorted_list)
            print('\n')
            lista = []
            size = int(input("\nEnter size of the list: \t"))
            for i in range(size):
                elements = int(input("Enter the element: \t"))
                lista.append(elements)

            insertion_sort(lista)

        elif p1.o == "SM":
            print(session_id)
            sorted_list = p1.data
            print('\nThe sorted list is: \t', sorted_list)
            sorted_list.reverse()

            listad = []
            size = int(input("\nEnter size of the list: \t"))
            for i in range(size):
                elements = int(input("Enter the element: \t"))
                listad.append(elements)
        reply ="yas"

    else:
        reply = "Received"
    UDPSocket.sendto(reply.encode(), bytesAddressPair[1])

