import socket
import os
import rsa
import time

from cryptography.fernet import Fernet

HOST = "127.0.0.1" 
PORT = 65402

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print ('Server TCP started and listening')

try:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
except:
    print("connection lost")


with open('key/privatekey.pem') as privatefile:
    keydata = privatefile.read()  
with open('key/publickey.pem') as publicfile:
    pkeydata = publicfile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata,'PEM')
pubkey = rsa.PublicKey.load_pkcs1(pkeydata)


# VERIFICATION QUE LES CLEFS GENERES SONT VALIDES
random_text = os.urandom(8)
signature = rsa.sign(random_text, privkey, 'MD5')
try:
    rsa.verify(random_text, signature, pubkey)
    print("La paire de clef générée est valide")
except:
    print ("La paire de clef générée n'est pas valide")


while True:
    data = conn.recv(1024)
    print("received: ",data)

    if not data:
        break

    #try:
    # STEP 1 : we decrypt data with rsa priv key to get symetric_key
    symetric_key = rsa.decrypt(data, privkey)

    print("symetric_key is : ",symetric_key)

    #time.sleep(1)

    os.system("sync")

    # STEP 2 : We decrypt cipher.txt with symetric_key
    f = open('cipher.txt', 'r')
    encMessage = f.read()

    print('encMessage with symetric key is : ', encMessage)

    fernet = Fernet(symetric_key)

    #decMessage = fernet.decrypt(encMessage).decode()
    decMessage = fernet.decrypt(encMessage.encode()).decode()

    print("Le message décrypté est: ", decMessage)

    #except Exception as e:
        #print("erreur dechiffrement : ", e)

conn.close()
