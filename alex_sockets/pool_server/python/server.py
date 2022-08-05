import socket
import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
   def run(self):

        print ("Starting " + self.name)

        print(self.name, self.counter, 3)

        while True:

            conn, addr = s.accept()

            while True:

                try :

                    msg = conn.recv(1024)

                    print(addr, ' >> ', msg.decode())

                    msg = input('SERVER ANSWER >> ')

                    conn.send(msg.encode())
                
                except Exception as e :

                    break

        conn.close()


HOST = "127.0.0.1" 
PORT = 61430

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print ('Server TCP started and listening')

threads = []

try:
    for i in range(3):
        threads.append(myThread(i, "Thread-{}".format(i), 1))

except Exception as e:
    print ("Error: unable to start thread", e)

# Start new Threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
