import socket

HOST = "127.0.0.1"  
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    str = input("Send (type 'bye' to exit) :")
    s.send(str.encode())
    if(str == "Bye" or str == "bye"):
        break
    print ("Received :",s.recv(1024).decode())
s.close()