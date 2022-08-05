import os

os.system("ls -a")
os.sync()
os.system("echo je fais un test")
os.sync()
os.system("make")
os.sync()
os.system('./server')
os.sync()
os.system('./client')