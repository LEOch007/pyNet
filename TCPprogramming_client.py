import socket


def client():
    # initialization: IPV4 TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect
    s.connect(('127.0.0.1', 9999))

    # print the msg from server
    print(s.recv(1024).decode('utf-8'))

    # send msg to server
    for data in [b'Michael', b'Tracy', b'Sarah']:
        s.send(data)                            # send the data
        print(s.recv(1024).decode('utf-8'))     # receive the response

    for i in range(10):
        data = str(i).encode('utf-8')
        s.send(data)  # send the data
        print(s.recv(1024).decode('utf-8'))  # receive the response

    # ask for closure
    s.send(b'exit')
    s.close()


# run the client
client()