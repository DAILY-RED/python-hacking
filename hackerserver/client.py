import socket

SERVER_IP   = "172.16.1.23"  # address of the server
SERVER_PORT = 8080

CHUNK_SIZE = 1024   # this determines how much data is received at a time (1024 bytes)

if __name__ == "__main__":

    # AF_INET indicates the address family (IPv4) 
    # SOCK_STREAM  indicates the socket type(TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (SERVER_IP, SERVER_PORT)
    sock.connect(address)

    # Print received message from server
    msg_received = sock.recv(CHUNK_SIZE) 
    print(msg_received.decode())
    sock.close()