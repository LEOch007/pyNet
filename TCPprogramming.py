import socket
import threading
import time


def client():
    # initialization
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    s.connect(('www.sina.com.cn', 80))

    # request:
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    # receive:
    buffer = []
    while True:
        d = s.recv(1024)  #at most 1k bytes
        if d:
            buffer.append(d)
        else:
            break

    data = b''.join(buffer)

    # close
    s.close()

    # printing
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    print('---------------------')
    print(html.decode('utf-8'))


# each connection requires a new thread to handle. otherwise, single thread cannot serve for many clients
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


def server():
    # initialization
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binding
    s.bind(('127.0.0.1', 9999))

    # listening
    s.listen(5)
    print('Waiting for connection...')

    while True:
        # accept a new connection
        sock, addr = s.accept()
        # create a new thread to handle
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


# run the server
server()