import socket
import time

HOST = "127.0.0.1"  
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    str = input("Send (type 'bye' to exit) :")

    time1 = time.monotonic_ns();

    s.send(str.encode());

    if(str == "Bye" or str == "bye"):
        break

    print ("Received :",s.recv(1024).decode())

    time2 = time.monotonic_ns();

    difference_time = float((time2-time1)/1000);

    print("Difference in milliseconds:", difference_time)

s.close()