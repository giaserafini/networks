import select
import socket
import sys
import uuid
import time
import random

s = 0
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo

while 1:
    msgFromClient = input("Enter message: ")
    c_message = msgFromClient.split("#")
    for x in c_message:
        if x != "":
            y = x.split("->")
            if y[0] == "s":
                s = s + 1
    if s == 0:
        msgFromClient = msgFromClient + "s->request#"

    print(msgFromClient)
    bytesToSend = str.encode(msgFromClient)  # wiadomosc od klienta

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(1024)
    print(msgFromServer[0].decode())
    if msgFromServer[0].decode() != "Received":
        UDPClientSocket.close()
        break

    # start = time.time()
    # message = time.ctime()
