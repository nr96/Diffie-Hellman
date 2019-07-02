import socket
import threading
import sys
import random
import Queue

p = 0x00cc81ea8157352a9e9a318aac4e33ffba80fc8da3373fb44895109e4c3ff6cedcc55c02228fccbd551a504feb4346d2aef47053311ceaba95f6c540b967b9409e9f0502e598cfc71327c5a455e2e807bede1e0b7d23fbea054b951ca964eaecae7ba842ba1fc6818c453bf19eb9c5c86e723e69a210d4b72561cab97b3fb3060b
g = 2


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    connections = []

    def __init__(self):
        self.sock.bind(('', 9999))
        self.sock.listen(1)  # begin running server

    def handler(self, c, d, a):  # function to handle data from clients and their connections
        while True:
            data = c.recv(1024)
            if not data:
                break
            K = pow(int(data), int(a), p)
            print(str(K))
            sys.exit()

            if not data:
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            try:
                try:
                    c, d = self.sock.accept()
                except KeyboardInterrupt:
                    self.sock.close()
                    sys.exit(0)

                a = random.randint(1, p)
                A = pow(g, int(a), p)
                c.send(str(A) + '\n')

                sThread = threading.Thread(target=self.handler, args=(c, d, a))  # thread to handle server duties
                sThread.daemon = True
                sThread.start()

                self.connections.append(c)
            except KeyboardInterrupt:
                self.sock.close()
                sys.exit(0)


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def sendMsg(self, b, queue):  # function to sendMsg to server
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            K = pow(int(data), int(b), p)
            #print(str(K))
            queue.put(K)

            sys.exit()

    def __init__(self, address):
        self.sock.connect((address, 9999))  # connect to server

        b = random.randint(1, p)
        B = pow(g, int(b), p)
        self.sock.send(str(B) + '\n')

        queue = Queue.Queue()
        cThread = threading.Thread(target=self.sendMsg, args=(b, queue, ))  # create thread to handle client input
        cThread.daemon = True
        cThread.start()  # start thread
        cThread.join()
        K = queue.get()

        print(str(K))

        while True:
            data = self.sock.recv(1024)
            if not data:
                break


if(len(sys.argv) == 3):
    try:
        client = Client(sys.argv[2])
    except KeyboardInterrupt:
        sys.exit(0)
else:
    try:
        server = Server()
        server.run()
    except KeyboardInterrupt:
        server.close()
        sys.exit(0)
