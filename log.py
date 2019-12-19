import datetime
import socket	#for sockets
import sys	#for exit
import subprocess


now = datetime.datetime.now().isoformat(' ', 'seconds')
s = socket.socket()
host = '0.0.0.0'
port = 22
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print (addr[0])
    eko = 'echo ' + addr[0] + ' ' + now + ' >> /home/log.txt'
    subprocess.run(eko, shell=True)
    c.close()
