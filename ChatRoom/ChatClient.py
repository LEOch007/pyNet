import socket
import threading
import random

from ChatRoom.myget import myget

class ChatClient:
    def __init__(self):
        self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # For Listening
        self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # For Connecting
        self.port = random.randint(10000,10100)                          # port
        self.addr1 = (myget.get_ip(), self.port)                        # IP address : port for sock1

    def start_client(self):
        # Sock1: listen
        try:
            self.sock1.bind(self.addr1)   # binding
        except Exception as e:
            print(e)
        self.sock1.listen(6)             # listening
        print('Client has started.')
        # waiting for connection from other clients
        t = threading.Thread(target=self.accept_connect, args=())
        t.setDaemon(True)
        t.start()

        # Sock2: connect
        self.sock2.connect(('127.0.0.1', 9999))         # connect to server
        self.sock2.send(b'list')                        # request
        print(self.sock2.recv(1024).decode('utf-8'))    # receive

    def accept_connect(self):
        while True:
            client_socket, client_address = self.sock1.accept()
            print('Accept new connection from %s:%s...' % client_address)


if __name__ == "__main__":
    client = ChatClient()
    client.start_client()