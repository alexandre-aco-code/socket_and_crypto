from Crypto.PublicKey import RSA

from hashlib import sha512

keyPair = RSA.generate(bits=1024)
#print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
#print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

#print(keyPair.publickey())



# RSA sign the message
msg = b'A message for signing'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')

signature = pow(hash, keyPair.d, keyPair.n)
print("Signature created: ", hex(signature))

# RSA verify signature
msg2 = b'A message for signing'
hash = int.from_bytes(sha512(msg2).digest(), byteorder='big')

hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature same msg2 valid ? ", hash == hashFromSignature)

# RSA verify signature (tampered msg)
msg3 = b'A message for signing (tampered)'
hash = int.from_bytes(sha512(msg3).digest(), byteorder='big')

hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature different msg3 valid ? ", hash == hashFromSignature)

