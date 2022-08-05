import hashlib
import sys

#try :
    #message = sys.argv[1]
#except Exception as e:
    #print("Manque string dans votre commande après le nom de fichier")
    #sys.exit()

message = "Hello Alexandre"

hashed_string = hashlib.sha256(message.encode('utf-8')).hexdigest()

print("hashed_string with sha256 is : ",hashed_string)


