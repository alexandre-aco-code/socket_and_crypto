import socket
import time

HOST = "127.0.0.1"  
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    str = input("Send (type 'bye' to exit) :")

    time1 = time.monotonic_ns()
    s.sendto(str.encode(), (HOST, PORT))

    time2 = time.monotonic_ns()
    difference_time = float((time2-time1)/1000)

    print("Message sent in milliseconds:", difference_time)

    if(str == "Bye" or str == "bye"):
        break

s.close()