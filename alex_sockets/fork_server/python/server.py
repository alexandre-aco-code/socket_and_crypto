import socket
import _thread

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)

        print(addr, ' >> ', msg)
        msg = input('SERVER >> ')

        clientsocket.send(msg.encode())
    clientsocket.close()

HOST = "127.0.0.1" 
PORT = 65432 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print ('Server TCP started and listening')



while True:
    conn, addr = s.accept()

    print(f"Connected by {addr}")

    _thread.start_new_thread(on_new_client,(conn,addr))

conn.close()
