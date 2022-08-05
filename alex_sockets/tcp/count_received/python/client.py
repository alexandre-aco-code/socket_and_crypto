import socket

HOST = "127.0.0.1"  
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    str = input("Send (type 'bye' to exit) :")

    bytes_prepared = bytes(str, "utf-8") + b'\0'

    number_bytes_prepared = len(bytes_prepared)

    print("number of bytes prepared is: ",number_bytes_prepared)

    number_bytes_sent = s.send(bytes_prepared)

    print("number of bytes sent is: ",number_bytes_sent)

    if(str == "Bye" or str == "bye"):
        break
    print ("Received :",s.recv(1024).decode())
s.close()