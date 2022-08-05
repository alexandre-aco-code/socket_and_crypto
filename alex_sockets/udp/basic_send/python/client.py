import socket

HOST = "127.0.0.1"  
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    str = input("Send (type 'bye' to exit) :")
    s.sendto(str.encode(), (HOST, PORT))
    if(str == "Bye" or str == "bye"):
        break
s.close()