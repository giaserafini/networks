import socket
import sys

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo
UDPClientSocket.connect(('127.0.0.1', 20001))
print (UDPClientSocket.recv(1024))
# msgFromClient: str ='ELO'
msgFromClient = input("Enter message: ")
bytesToSend = str.encode(msgFromClient)     # wiadomosc od klienta

UDPClientSocket.sendto(bytesToSend, serverAddressPort)  # wyslanie wiadomosci
UDPClientSocket.close()