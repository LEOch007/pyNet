import datetime
import socket

from ChatRoom.myget import myget

class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        self.addr = (myget.get_ip(), 9990)                             # IP address : port

    def start_client(self):
        pass



def client():
    # TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connection
    send_ip = input("请输入要发送的ip地址：")
    send_port = input("请输入要发送的端口号地址：")
    address = (send_ip, int(send_port))
    client_socket.connect(address)

    while True:
        send_msg = input("输入想发送的文字")
        if send_msg != 'exit':
            # send the data
            send_data = send_msg.encode("utf-8")
            client_socket.send(send_data)

            # receive the data
            recv_data = client_socket.recv(1024)
            recv_msg = recv_data.decode("utf-8")

            print(recv_msg)
        else:
            break
    client_socket.close()


if __name__ == "__main__":
    client()