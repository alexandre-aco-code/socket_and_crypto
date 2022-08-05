import subprocess
import re
import hashlib

class TestHash:

    path = r"/home/alexandre/Documents/babdevexplo-corentin_sockets/babdevexplo/alex_cryptography/hash/hashlib"

    fileName = '/hash.py'

    filePath = path+fileName

    input_message = "Hello Alexandre"

    output = subprocess.check_output(["python3", filePath, input_message], universal_newlines=True)

    hash_message = re.findall(r"hashed_string with sha256 is : (.*)", output)[0][1:]

    expected_hash_message = hashlib.sha256(input_message.encode('utf-8')).hexdigest()

    def test_hash(self):
        assert self.hash_message == self.expected_hash_message


    
