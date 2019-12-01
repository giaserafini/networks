import socket
import time
from package import package

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024


def odebranie_wyniku():
    msgFromServer = UDPClientSocket.recvfrom(1024)
    msgFromServer_ = msgFromServer[0].decode()
    c_message = msgFromServer_.split("#")
    for x in c_message:
        if x != "":
            y = x.split("->")
            if y[0] == "o":
                packet_response.set_o(y[1])
            elif y[0] == "s":
                packet_response.set_s(y[1])
            elif y[0] == "i":
                packet_response.set_i(y[1])
            elif y[0] == "t":
                packet_response.set_time(y[1])
            elif y[0] == "d3":
                packet_response.set_data3(y[1])

    request = packet_response.return_packet_response
    # print(request)  # wiadomosc od serwera
    print(packet_response.data3)
def odebranie_wyniku_sort():
    msgFromServer = UDPClientSocket.recvfrom(1024)
    msgFromServer_ = msgFromServer[0].decode()
    c_message = msgFromServer_.split("#")
    for x in c_message:
        if x != "":
            y = x.split("->")
            if y[0] == "o":
                packet_response.set_o(y[1])
            elif y[0] == "s":
                packet_response.set_s(y[1])
            elif y[0] == "i":
                packet_response.set_i(y[1])
            elif y[0] == "t":
                packet_response.set_time(y[1])
            elif y[0] == "d":
                packet_response.data_tab = y[1]
            elif y[0] == "e":
                packet_response.set_end(y[1])

    request = packet_response.return_packet_response_sort
    #print(request)  # wiadomosc od serwera
    print(packet_response.data_tab)


UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo


while True:
    packet = package()
    packet_response = package()
    print("Wybierz operacje:\n"
          "modulo\n"
          "dodawanie\n"
          "odejmowanie\n"
          "losowanie\n"
          "sortowanie rosnace\n"
          "sortowanie malejace\n\n"
          "Aby zakończyć wpisz exit")
    msgFromClient = input("\n")

    if msgFromClient == "modulo":
        print("Modulo")
        liczba1 = input("Podaj pierwsza liczbe: ")
        liczba2 = input("Podaj druga liczbe: ")

        #wyslanie wiadomosci
        packet.set_o("A")
        packet.set_s("null")
        packet.set_i()
        packet.set_t()
        packet.set_data1(liczba1)
        packet.set_data2(liczba2)
        request = packet.return_packet
        # print(request)  # wiadomosc od klienta
        UDPClientSocket.sendto(str(request).encode(), serverAddressPort)

        #odebranie wiadomosci
        odebranie_wyniku()

    elif msgFromClient == "losowanie":
        print("Losowanie")
        liczba1 = input("Wpisz najmniejszą możliwą liczbe: ")
        liczba2 = input("Wpisz najwieksza możliwą liczbe: ")

        # wyslanie wiadomosci
        packet.set_o("a")
        packet.set_s("null")
        packet.set_i()
        packet.set_t()
        packet.set_data1(liczba1)
        packet.set_data2(liczba2)
        request = packet.return_packet

        # print(request)  # wiadomosc od klienta
        UDPClientSocket.sendto(str(request).encode(), serverAddressPort)

        # odebranie wiadomosci
        odebranie_wyniku()

    elif msgFromClient == "dodawanie":
        print("dodawanie")
        liczba1 = input("Wpisz pierwsza liczbe: ")
        liczba2 = input("Wpisz druga liczbe: ")

        # wyslanie wiadomosci
        packet.set_o("D")
        packet.set_s("null")
        packet.set_i()
        packet.set_t()
        packet.set_data1(liczba1)
        packet.set_data2(liczba2)
        request = packet.return_packet

        # print(request)  # wiadomosc od klienta
        UDPClientSocket.sendto(str(request).encode(), serverAddressPort)

        # odebranie wiadomosci
        odebranie_wyniku()

    elif msgFromClient == "odejmowanie":
        print("odejmowanie")
        liczba1 = input("Wpisz pierwsza liczbe: ")
        liczba2 = input("Wpisz druga liczbe: ")

        # wyslanie wiadomosci
        packet.set_o("O")
        packet.set_s("null")
        packet.set_i()
        packet.set_t()
        packet.set_s("null")
        packet.set_data1(liczba1)
        packet.set_data2(liczba2)
        request = packet.return_packet

        # print(request)  # wiadomosc od klienta
        UDPClientSocket.sendto(str(request).encode(), serverAddressPort)

        # odebranie wiadomosci
        odebranie_wyniku()

    elif msgFromClient == "sortowanie malejace":
        print("sortowanie malejące")
        end = 0
        while end == 0:
            liczba = int(input("Podaj liczbe: "))

            # wyslanie wiadomości
            packet.set_o("SM")
            if packet.i == "":
                packet.set_i()
            else:
                packet.set_i()
            packet.set_t()
            packet.set_s("null")
            packet.set_data1(liczba)
            koniec = input("Czy jest to ostatnia liczba? tak/nie\n")
            if koniec == "tak":
                end = 1
            elif koniec == "nie":
                end = 0
            else:
                koniec = input("Czy jest to ostatnia liczba? tak/nie\n")
            packet.set_end(end)

            request = packet.return_packet_sort

            # print(request)  # wiadomosc od klienta
            UDPClientSocket.sendto(str(request).encode(), serverAddressPort)

            # odebranie wiadomosci
            odebranie_wyniku_sort()

    elif msgFromClient == "sortowanie rosnace":
        print("sortowanie rosnace")
        end = 0
        while end == 0:
            liczba = int(input("Podaj liczbe: "))

            # wyslanie wiadomości
            packet.set_o("SR")
            if packet.i == "":
                packet.set_i()
            else:
                packet.set_i()
            packet.set_t()
            packet.set_s("null")
            packet.set_data1(liczba)
            koniec = input("Czy jest to ostatnia liczba? tak/nie\n")
            if koniec == "tak":
                end = 1
            elif koniec == "nie":
                end = 0
            else:
                koniec = input("Czy jest to ostatnia liczba? tak/nie\n")
            packet.set_end(end)

            request = packet.return_packet_sort

            # print(request)  # wiadomosc od klienta
            UDPClientSocket.sendto(str(request).encode(), serverAddressPort)

            # odebranie wiadomosci
            odebranie_wyniku_sort()
    elif msgFromClient == "exit":
        UDPClientSocket.close()
        break
    else:
        print("Nie ma takiej operacji\n")


