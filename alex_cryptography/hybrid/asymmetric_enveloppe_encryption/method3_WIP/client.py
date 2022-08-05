import os
import socket
import rsa

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from cryptography.fernet import Fernet

HOST = "127.0.0.1"  
PORT = 65402



with open('key/publickey.pem', 'rb') as publicfile:
    pkeydata = publicfile.read()

pubkey = rsa.PublicKey.load_pkcs1(pkeydata)

symetric_key = Fernet.generate_key()
fernet = Fernet(symetric_key)

def TCPSocket_Send(data,len):
    networkLen = len
    return 



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:

    # STEP 1 : message is Symetricly encrypted
    str = input("Type Message to send (type 'bye' to exit) :")
    encMessage = fernet.encrypt(str.encode())

    # STEP 2 : symetric_key IS ENCRYPTED WITH RSA
    encKey = rsa.encrypt(symetric_key,pubkey)

    print(encMessage)
    print(encKey)

    len_encMessage = len(encMessage)
    len_encKey = len(encKey)

    print(len_encKey)
    print(len_encMessage)

    whole = len_encKey + encKey + len_encMessage + encMessage 


    s.send(whole)
    print("message sucessfully sent")

    if(str == "Bye" or str == "bye"):
        break

s.close()