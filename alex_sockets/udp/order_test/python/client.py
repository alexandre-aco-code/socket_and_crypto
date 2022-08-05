import socket
import time

HOST = "127.0.0.1"  
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    str = "Message 1\n"
    s.sendto(str.encode(), (HOST, PORT))

    str2 = "Message 2\n"
    s.sendto(str2.encode(), (HOST, PORT))

    time.sleep(5)

    str3 = "Message 3 after 5 sec sleep\n"
    s.sendto(str3.encode(), (HOST, PORT))

    str4 = "Message 4\n"
    s.sendto(str4.encode(), (HOST, PORT))

    break
s.close()

