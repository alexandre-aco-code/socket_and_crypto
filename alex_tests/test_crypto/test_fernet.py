from cmath import exp
from email import message
import re
import subprocess

from cryptography.fernet import Fernet

class TestFernet:

    #def setup(self):
    path = r"/home/alexandre/Documents/babdevexplo-corentin_sockets/babdevexplo/alex_cryptography/symetric/fernet"

    fileName = '/symetric.py'

    filePath = path+fileName

    input_message = "Hello Alexandre"
    #input_message = input("Type >>>")

    output = subprocess.check_output(["python3", filePath, input_message], universal_newlines=True)


    enc_message = re.findall(r"encrypted string: (.*)", output)[0]

    #print("input_message", input_message)
    #print("enc_message", enc_message)


    dec_message = re.findall(r"decrypted string: (.*)", output)[0][1:-1] #on enlève les espaces avant et après le string

    #print("dec_message", dec_message)
    #print("type of type(i)", type(dec_message))

    key = Fernet.generate_key()
    fernet = Fernet(key)

    expected_encrypted_message = fernet.encrypt(input_message.encode())

    expected_decrypted_message = fernet.decrypt(expected_encrypted_message).decode()


    #print(expected_decrypted_message)

    def test_decryption(self):
        #print("we test decryption")
        #print("self.dec_message", self.dec_message)

        assert self.dec_message == self.expected_decrypted_message


    
