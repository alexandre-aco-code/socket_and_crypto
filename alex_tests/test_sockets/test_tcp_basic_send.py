import os

class TestTCP:

    path = '../../socket/tcp/basic_send'

    def test_basic_send(self):
        
        os.system('./server')
        os.sync()
        os.system('./client')

        
    #input_message = input("Type >>>")





    def test_two(self):
        x = "hello"
        assert "o" in x

