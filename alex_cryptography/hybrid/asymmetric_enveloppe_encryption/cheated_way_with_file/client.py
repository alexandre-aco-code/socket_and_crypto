import os
import socket
import rsa
import time

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from cryptography.fernet import Fernet

with open('key/publickey.pem', 'rb') as publicfile:
    pkeydata = publicfile.read()

pubkey = rsa.PublicKey.load_pkcs1(pkeydata)

symetric_key = Fernet.generate_key()
fernet = Fernet(symetric_key)

HOST = "127.0.0.1"  
PORT = 65402

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:

    # STEP 1 : message is Symetricly encrypted
    str = input("Type Message to send (type 'bye' to exit) :")

    
    print("symetric_key is : ",symetric_key)
    
    encryptedMessage = fernet.encrypt(str.encode())

    print('encryptedMessage.decode()', encryptedMessage.decode())

    f = open('cipher.txt', 'w')
    f.write(encryptedMessage.decode())
    f.close()

    print("File with encryptedMessage sucessfully created")

    #time.sleep(1)

    os.system("sync")

    # STEP 2 : symetric_key IS ENCRYPTED WITH RSA
    encryptedKey = rsa.encrypt(symetric_key,
                         pubkey)

    s.send(encryptedKey)
    print("encryptedKey sucessfully sent")

    if(str == "Bye" or str == "bye"):
        break

s.close()