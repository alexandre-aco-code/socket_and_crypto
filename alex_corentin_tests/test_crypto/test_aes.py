import subprocess

from cryptography.fernet import Fernet

class TestAes:

    path = r"/home/alexandre/Documents/babdevexplo-corentin_sockets/babdevexplo/cryptography/aes"

    fileName = './main'

    filePath = path+"/"+fileName

    from subprocess import Popen, PIPE

    output = subprocess.check_output([filePath], universal_newlines=True)

    output_in_list = output.split()

    #print(output_in_list)

    initial_msg = output_in_list[6:9]
    decrypted_msg = output_in_list[14:17]

    #print(initial_msg)
    #print(decrypted_msg)

    def test_aes(self):
        assert self.decrypted_msg == self.initial_msg
