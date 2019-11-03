import socket
import sys
import uuid

IP = "127.0.0.1"
Port = 20001
listeningAddress = (IP, Port)
my_id = uuid.uuid1()  # identyfikator sesji

UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo
print ('Socket created successfully')
UDPSocket.bind('', Port)
#print('Socket binded to ')

UDPSocket.listen(5)
print("I'm listening to you")

while True:
    #tutaj jeszcze powinno byc cos takiego tylko nwm jak to zaimplementowac, bo nwm czym jest to c czy to klient?
    # Establish connection with client.
   # c, addr = s.accept()
   # print
   # 'Got connection from', addr

    # send a thank you message to the client.
    #c.send('Thank you for connecting')

    # Close the connection with the client
   # c.close()
    bytesAddressPair = UDPSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1][0]
    print("Message from Client:", message)
    print("Client IP Address:", address)

#   clientMsg = "Message from Client:{}".format(message)
#   clientIP = "Client IP Address:{}".format(address)
#   print(clientMsg)
#   print(clientIP)


