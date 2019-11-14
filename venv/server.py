import socket
import sys
import uuid
from package import package

IP = "127.0.0.1"
Port = 20001
listeningAddress = (IP, Port)
my_id = uuid.uuid1()  # identyfikator sesji

UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo
UDPSocket.bind(listeningAddress)

p1 = package()

print("I'm listening to you")

while True:

    # odebranie komunikatu
    bytesAddressPair = UDPSocket.recvfrom(1024)
    message = bytesAddressPair[0].decode()
    address = bytesAddressPair[1][0]

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
