import datetime
import os
import socket
import threading

from ChatRoom.myget import myget


class ChatServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        self.addr = (myget.get_ip(), 10000)                            # IP address : port
        self.users = {}                                               # user dictionary

    def start_server(self):
        try:
            self.sock.bind(self.addr)   # binding
        except Exception as e:
            print(e)
        self.sock.listen(6)             # listening
        print('server has started, waiting for connection...')
        self.accept_connect()           # accept connection from client

    def accept_connect(self):
        while True:
            client_socket, client_address = self.sock.accept()
            self.users[client_address] = client_socket
            number = len(self.users)
            print("User {} successfully connected.\n Now we have {} users in total.".format(client_address, number))

            # support multi-clients to connect
            threading.Thread(target=self.recv_send, args=(client_socket, client_address)).start()

    def recv_send(self, c_sock, c_addr):
        while True:
            try:
                response = c_sock.recv(1024).decode("utf-8")
                msg = "At {}, user {} is sending msg.".format(myget.get_time(), c_addr)
                print(msg)

            except ConnectionResetError:
                print("At {}, user {} is offline.".format(myget.get_time(), c_addr))
                self.users.pop(c_addr)
                break

    def close_server(self):
        for client_socket in self.users.values():
            client_socket.close()
        self.sock.close()
        os._exit(0)


def print_haha():
    for i in range(10000):
        print('haha')

if __name__ == "__main__":
    # create a new thread to accept the connection from clients
    server = ChatServer()
    threading.Thread(target=server.start_server(), args=()).start()

    # main thread: waiting and handling command for server
    while True:
        cmd = input('Input the Command: ')
        if cmd == "stop":
            server.close_server()
        else:
            print("command is invalid, please type in \'stop\' to shut down the server.")
