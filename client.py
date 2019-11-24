import select
import socket
import sys
import uuid
import time
import random

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo

while 1:
    msgFromClient = input("Enter message: ")
    bytesToSend = str.encode(msgFromClient)  # wiadomosc od klienta

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(1024)
    print(msgFromServer[0].decode())
    if msgFromServer[0].decode() != "Received":
        print("kys")
        UDPClientSocket.close()
        break

# UDPClientSocket.close()

    # start = time.time()
    # message = time.ctime()
