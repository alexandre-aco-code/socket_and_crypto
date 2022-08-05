import socket
import time

HOST = "127.0.0.1" 
PORT = 65432 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print ('Server UDP started')

while True:

    data, addr = s.recvfrom(1024)   
    time1 = time.monotonic_ns()

    print("received message : %s" % data.decode())
    time2 = time.monotonic_ns()

    difference_time = float((time2-time1)/1000)
    print("Message received in milliseconds:", difference_time)