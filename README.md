# Diffie-Hellman
Program that performs a Diffie-Hellman (DH) Key Exchange over a network. The program operates in either client or server mode. The former initiates a connection to the latter; otherwise, their functionality is identical.

The program should work as follows:
1. The client instance of dh.py opens a TCP connection to the server instance of dh.py. The latter listens on TCP port 9999 for the client’s connection.
2. Once connected, the client chooses a number a uniformly at random from the range [1, p) and computes A = ga mod p. It then sends A to the server.
3. The server similarly and independently chooses a number b uniformly at random from the range [1, p) and computes B = gb mod p. It then sends B to the client.
4. The client then computes K = Ba mod p and prints K to standard output.
5. The server then computes K = Ab mod p and prints K to standard output.

Program has the following command-line options: dh.py --s|--c hostname
where the --s argument indicates that the program should wait for an incoming TCP/IP connection on port 9999; the --c argument (with its required hostname parameter) in- dicates that the program should connect to the machine hostname (over TCP/IP on port 9999).
