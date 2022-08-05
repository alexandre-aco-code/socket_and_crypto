from cryptography.fernet import Fernet
 
import sys

#message = input("Votre message à encrypter ?\n")

#message = "Hello Alexandre"

try :
    message = sys.argv[1]
except Exception as e:
    print("Manque string dans votre commande après le nom de fichier")
    sys.exit()


print("\noriginal string: ", message, "\n")

 
key = Fernet.generate_key()
 
fernet = Fernet(key)
 
encMessage = fernet.encrypt(message.encode())
 
print("encrypted string: ", encMessage, "\n")


decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage, "\n")

#import sys
#for path in sys.path:
#    print(path)