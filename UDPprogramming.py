import socket
import threading
import time


def server():
    # initialization
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # binding
    s.bind(('127.0.0.1', 9999))

    # no need to listen
    print('Binding UDP on port 9999...')

    while True:
        data, addr = s.recvfrom(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        s.sendto(b'Hello, %s!' % data, addr)


# run UDP server
server()