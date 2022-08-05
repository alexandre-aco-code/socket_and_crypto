import socket
import time
from warnings import catch_warnings

HOST = "127.0.0.1"  
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
  s.connect((HOST, PORT))
  while True:
      str = "Message 1\n"
      s.send(str.encode())
      print ("Received :",s.recv(1024).decode())

      str2 = "Message 2\n"
      s.send(str2.encode())
      print ("Received :",s.recv(1024).decode())

      time.sleep(5)

      str3 = "Message 3 after 5 sec sleep\n"
      s.send(str3.encode())
      print ("Received :",s.recv(1024).decode())

      str4 = "Message 4\n"
      s.send(str4.encode())
      print ("Received :",s.recv(1024).decode())
      
      break
      s.close()
  
except Exception as ex:
  print(ex)