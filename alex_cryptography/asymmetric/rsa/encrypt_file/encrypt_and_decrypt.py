#https://cryptobook.nakov.com/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples

from cgitb import text
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()

with open('files/1_encryptme.txt') as f:
    lines = f.readlines()

print(lines)

msgtotal = ''

for line in lines:
    msgtotal += line

msg = bytes(msgtotal, 'utf-8')

print("Message is: ", msg)

encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)

#text = encrypted.decode('latin-1')
#print(text)

hextest = binascii.hexlify(encrypted)
print("Encrypted:", hextest)

f = open("files/2_encrypted.txt", "w")
f.write(hextest.decode())
f.close()

print("ENCRYPTED => File 2_encrypted.txt successfully created!")

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)


f = open("files/3_decrypted.txt", "w")
f.write(decrypted.decode("utf-8") )
f.close()

print("DECRYPTED => File 3_decrypted.txt successfully created!")