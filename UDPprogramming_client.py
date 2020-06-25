import socket


def client():
    # initialization: IPV4 UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # print the welcome msg from server
    print(s.recv(1024).decode('utf-8'))

    # send msg to server
    for data in [b'Michael', b'Tom', b'Sam']:
        s.sendto(data, ('127.0.0.1', 9999))     # send the data
        print(s.recv(1024).decode('utf-8'))     # receive the response

    # ask for closure
    s.send(b'exit')
    s.close()


# run UDP client
client()