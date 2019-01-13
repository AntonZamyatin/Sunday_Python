import socket
import threading
import sys


class Server:
    connections = []
    peers = []

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 tcp
        sock.bind(('0.0.0.0', 10000))
        sock.listen(1)
        while True:
            conn, addr = sock.accept()
            self.connections.append(conn)
            self.peers.append(addr[0])
            self.sendPeers()
            conn.send(b'Kisuha - lisuha\n')
            cThread = threading.Thread(target=self.handler,
                                       args=(conn, addr))
            cThread.daemon = True
            cThread.start()
            print("{0}:{1} connected".format(str(addr[0]),
                                             str(addr[1])))

    def handler(self, conn, addr):
        while True:
            data = conn.recv(1024)
            for connection in self.connections:
                connection.send(bytes(data))
            if not data:
                self.connections.remove(conn)
                self.peers.remove(addr[0])
                conn.close()
                self.sendPeers()
                print("{0}:{1} disconnected".format(str(addr[0]),
                                                    str(addr[1])))
                break

    def sendPeers(self):
        p = ''
        for peer in self.peers:
            p = p + peer + ","
        p = str(len(p) + 2) + p[1:]

        for connection in self.connections:
            connection.send(b'\x11' + bytes(p, "utf-8"))


class Client:

    def __init__(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 tcp
        sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg, args=(sock,))
        iThread.daemon = True
        iThread.start()

        while True:
            data = sock.recv(1024)
            if not data:
                break
            if data[0:1] == b'\x11':
                n = int(data[1:3])
                print("got peers")
                print(str(data[n:], 'utf-8'))
            else:
                print("recieved:")
                print(str(data, 'utf-8'))

    def sendMsg(self, sock):
        while True:
            sock.send(bytes(input(), 'utf-8'))


if(len(sys.argv) > 1):
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()
