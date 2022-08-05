import socket

HOST = "127.0.0.1" 
PORT = 65432 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print ('Server UDP started')

while True:
    data, addr = s.recvfrom(1024)
    print("received message : %s" % data.decode())