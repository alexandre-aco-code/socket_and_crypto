import rsa
 
publicKey, privateKey = rsa.newkeys(3072)
 
message = input("Votre message à encrypter ?")


encMessage = rsa.encrypt(message.encode(),
                         publicKey)
 
print("original string: ", message)
print("encrypted string: ", encMessage)


decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
print("Le message décrypté est: ", decMessage)