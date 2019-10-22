import socket
import select
import sys

IP = "127.0.0.1"

Port = 20001

bufferSize = 1024

msgFromServer = "ELO"

bytesToSend = str.encode(msgFromServer)

UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPSocket.bind((IP, Port))

print("I'm listening to you ")

while 1:

    bytesAddressPair = UDPSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    msgFromServer = input(a%b)
    msgFromServer = input(a+b)  #nie jestem jeszcze pewna tych 3 linijek
    msgFromServer = input (a*b)
    serverSocket.sendto(messagetoclient, clientAddress)
    print(clientMsg)
    print(clientIP)
    print (a%b)
    print(a+b)
    print(a*b)
   # print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))
    UDPSocket.sendto(bytesToSend, address)


