import socket
import sys
import uuid

IP = "127.0.0.1"
Port = 20001
listeningAddress = (IP, Port)
my_id = uuid.uuid1()  # identyfikator sesji

UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo
UDPSocket.bind(listeningAddress)

print("I'm listening to you")

while True:

    bytesAddressPair = UDPSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1][0]
    print("Message from Client:", message)
    print("Client IP Address:", address)

#   clientMsg = "Message from Client:{}".format(message)
#   clientIP = "Client IP Address:{}".format(address)
#   print(clientMsg)
#   print(clientIP)


