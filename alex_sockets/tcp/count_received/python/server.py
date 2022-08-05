import socket

HOST = "127.0.0.1" 
PORT = 65432 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print ('Server TCP started and listening')

conn, addr = s.accept()

print(f"Connected by {addr}")

number_of_messages = 0

while True:
    data = conn.recv(1024)
    print("received: ",data.decode())

    number_of_messages = number_of_messages+1

    print("number of messages received: ", number_of_messages)

    print("bytes received: {}".format(len(data)))

    if not data:
        break
    conn.sendall(data)

conn.close()
