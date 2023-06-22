import socket

def run_command(conn):
    print("[+] Running commands")
    while True:
        command = input(">> ")
        conn.send(command.encode())
        if command.lower() == "stop":
            break
        result = conn.recv(4096).decode()
        print(result)


def handle_connection(client_socket):
    print("[+] Handling connection")
    run_command(client_socket)
    client_socket.close()


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("[+] Server started, waiting for incoming connections on port", port)
    
    while True:
        client_socket, addr = server_socket.accept()
        print("[+] Connection established with", addr[0], "on port", addr[1])
        handle_connection(client_socket)


if __name__ == "__main__":
    host = ""
    port = 8080
    start_server(host, port)
