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
        while j >= 0 and key < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key

IP = "127.0.0.1"
Port = 20001
listeningAddress = (IP, Port)
my_id = uuid.uuid1()  # identyfikator sesji

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
            print(my_id)
            print(number1 % number2)
        elif p1.o == "B":
            number1 = int(p1.data[0])
            number2 = int(p1.data[1])
            print(my_id)
            print(number1 + number2)
        elif p1.o == "C":
            number1 = int(p1.data[0])
            number2 = int(p1.data[1])
            print(my_id)
            print(number1 - number2)
        elif p1.o == "a":
            a = int(input(p1.data[0]))
            b = int(input(p1.data[1]))
            print(my_id)
            print(random.randint(a, b))

        elif p1.o == "SortowanieRosnace":
            print(my_id)
            print('\nThe sorted list: \t', sorted_list)
            print('\n')
            lista = []
            size = int(input("\nEnter size of the list: \t"))
            for i in range(size):
                elements = int(input("Enter the element: \t"))
                lista.append(elements)

            insertion_sort(lista)

        elif p1.o == "SortowanieMalejace":
            print(my_id)
            print('\nThe sorted list is: \t', sorted_list)
            sorted_list.reverse()

            listad = []
            size = int(input("\nEnter size of the list: \t"))
            for i in range(size):
                elements = int(input("Enter the element: \t"))
                listad.append(elements)
insertion_sort_d(listad)
socket.sendto(reply, address)
            #print ('Message[' + address[0] + ':' + str(address[1]) + '] - ' + data.strip())


        # tutaj wykonanie operacji


        # print("koniec")
        # print(p1.o)
        # print(p1.s)
        # print(p1.i)
        # print(p1.data)
        # print(p1.end)

        # na sam koniec + dopisanie w komunikacie o zamknieciu i zakoczeniu poalczania
        # UDPSocket.close()








#   clientMsg = "Message from Client:{}".format(message)
#   clientIP = "Client IP Address:{}".format(address)
#   print(clientMsg)
#   print(clientIP)

# sys.getsizeof(message)-17 rozmiar
UDPSocket.close()