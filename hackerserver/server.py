import socket

SERVER_IP   = "172.16.1.23"  # address of the server
SERVER_PORT = 8080

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    address = (SERVER_IP, SERVER_PORT)
    sock.bind(address)       # Bind the IP with the server port

    sock.listen(1)           # listening to 1 conncetion 

    print("[+] Waiting for incoming connections: ", SERVER_PORT)
    client_sock, client_add = socket.accept()  # wait until the client connect
    print ("[+] Connection established: ", client_add)

    msg = "This is the server speaking"

    client_sock.send(msg.encode()) # Sends message to client 

    client_sock.close() # close connection with client
    sock.close()