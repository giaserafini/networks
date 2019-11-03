import socket
import sys
import uuid

IP = "127.0.0.1"

my_id = uuid.uuid1()  # identyfikator sesji

UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # gniazdo
print ('Socket created successfully')
Port = 20001
listeningAddress = (IP, Port)
UDPSocket.bind('', Port)
#print('Socket binded to ')

UDPSocket.listen(5)
print("I'm listening to you")

while True:
    c, addr = s.accept()
    print ('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()


    bytesAddressPair = UDPSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1][0]
    print("Message from Client:", message)
    print("Client IP Address:", address)
    UDPSocket.settimeout(0.5)


BUFFER_LENGHT = 100

def readUDP(UDPSocket): #odczytywanie, obsluga wyjatkow
    try:
        data, addr = UDPSocket.recvfrom(BUFFER_LENGHT)
    except UDPSocket.timeout as e:
        return b'Timeout error'
    except Exception as e:
        return b'Too much data'
    else:
        return data
#   clientMsg = "Message from Client:{}".format(message)
#   clientIP = "Client IP Address:{}".format(address)
#   print(clientMsg)
#   print(clientIP)


