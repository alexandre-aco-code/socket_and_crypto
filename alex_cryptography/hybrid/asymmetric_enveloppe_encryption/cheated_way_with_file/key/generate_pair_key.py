import rsa

(pubkey, privkey) = rsa.newkeys(1024) 

# PEM (default)
print(privkey.save_pkcs1().decode('utf-8'))
print(pubkey.save_pkcs1().decode('utf-8'))


f = open('publickey.pem','wb')
f.write(pubkey.save_pkcs1())
f.close()

f = open('privatekey.pem','wb')
f.write(privkey.save_pkcs1())
f.close()