import socket

sock = socket.socket()
sock.bind(('', 9091))

sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if data == b'stop':
        conn.send(data.upper())
        break
    conn.send(data.upper())
conn.close()
