import socket

sock = socket.socket()
sock.connect(('localhost', 9091))
while True:
    sock.send(bytes(input(), 'utf-8'))
    data = sock.recv(1024)
    print(data)
    if data == b'STOP':
        break
sock.close()
