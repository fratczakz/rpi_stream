import socket


class NVServer(object):

    def __init__(self):
        self.s = socket.socket()
        host = socket.gethostname()
        port = 12345
        self.s.bind((host, port))

    def listen(self):
        self.s.listen(5)
        while True:
            c, addr = self.s.accept()
            print ('Got connection from', addr)
            c.send('Thank you for connecting')
            c.close()
