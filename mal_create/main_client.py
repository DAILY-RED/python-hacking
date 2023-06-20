from  malware_create.client_connection import ClientConnection

if __name__ == "__main__":
    my_socket = ClientConnection()

    # Server IP
    my_socket.Connect("172.16.1.23", 8080)

    print(my_socket.receive_data())

    my_socket.send_data("Hi this is client")