import os
import socket
import threading

from ChatRoom.myget import myget


class ChatServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        self.addr = (myget.get_ip(), 9999)                            # IP address : port
        self.users = {}                                               # user dictionary

    def start_server(self):
        try:
            self.sock.bind(self.addr)   # binding
        except Exception as e:
            print(e)
        self.sock.listen(6)             # listening
        print('Server has started, waiting for connection...')
        t = threading.Thread(target=self.accept_connect, args=())
        t.setDaemon(True)
        t.start()

    # accept connection from client
    def accept_connect(self):
        while True:
            client_socket, client_address = self.sock.accept()
            self.users[client_address] = client_socket
            number = len(self.users)
            print("User {} successfully connected. Now we have {} users in total.".format(client_address, number))

            # support multi-clients to connect
            t = threading.Thread(target=self.recv_print, args=(client_socket, client_address))
            t.setDaemon(True)
            t.start()

    def recv_print(self, c_sock, c_addr):
        while True:
            data = c_sock.recv(1024)
            if not data or data.decode('utf-8') == 'exit':
                break
            if data.decode('utf-8') == 'list':
                print('Response to user {} at {}.'.format(c_addr, myget.get_time()))
                send_msg = 'User List:' + str(self.users.keys())
                send_data = send_msg.encode('utf-8')
                c_sock.send(send_data)
            else:
                msg = "User {} is sending invalid msg to server at {}".format(c_addr, myget.get_time())
                print(msg)

        c_sock.close()
        print("At {}, user {} is offline.".format(myget.get_time(), c_addr))
        self.users.pop(c_addr)

    def close_server(self):
        for client_socket in self.users.values():
            client_socket.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    # create a new thread to accept the connection from clients
    server = ChatServer()
    server.start_server()

    # main thread: waiting and handling command for server
    while True:
        cmd = input()
        if cmd == "stop":
            server.close_server()
        else:
            print("Invalid command. Please type in \'stop\' to shut down the server.")
