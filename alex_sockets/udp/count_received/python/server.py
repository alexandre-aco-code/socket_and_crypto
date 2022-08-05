from re import S
import socket

HOST = "127.0.0.1" 
PORT = 65432 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print ('Server UDP started')

number_of_messages = 0

while True:
    data, addr = s.recvfrom(1024)


    number_of_messages = number_of_messages+1

    print("number of messages received: ", number_of_messages)

    print("bytes received: {}".format(len(data)))

    print("received message : %s" % data.decode())