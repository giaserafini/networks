import select
import socket
import sys

msgFromClient = "ELO2"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
#while 1:
    #message = input("> ")
    #message = message.encode()

    #try:
     #   UDPClientSocket.sendto(bytesToSend, ("127.0.0.1", 20001))
      #  msgFromServer = UDPClientSocket.recvfrom(1024)
       # #print("{}: {}".format(msgFromServer, data.decode()))

    #except socket.error:
     #   print("Error! {}".format(socket.error))
      #  exit()



#message = '-o'
#if message:
  #  print (message)
#message1 = ''
#if message1:
 #   print (message1)
#message2 = 'x'
#if message2:
 #   print(message2)
#message3 = " "
#if message3:
 #   print (message3)
#message4 = ' '
#if message4:
 #   print (message4)