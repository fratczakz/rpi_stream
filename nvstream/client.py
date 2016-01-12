import socket


class NVClient(object):
    """docstring for NVClient"""
    def __init__(self):
        self.s = socket.socket()

    def get(self):
        host = socket.gethostname()
        print (host)
        port = 12345
        self.s.connect((host, port))
        print (self.s.recv(1024))
        self.s.close()
