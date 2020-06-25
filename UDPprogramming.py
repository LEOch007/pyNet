import socket
import threading


def server():
    # initialization
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # binding
    s.bind(('127.0.0.1', 9999))

    # no need to listen
    print('Binding UDP on port 9999...')

    while True:
        data, addr = s.recvfrom(1024)

