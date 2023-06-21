from mal_create.server_connection import ServerConnection

if __name__ == "__main__":

    my_socket = ServerConnection()
    my_socket.CreateConnection("", 8080)

    my_socket.Listen()

    my_conn, _ = my_socket.AcceptConnection()

    my_socket.send_data("Hi this is server")

    print(my_socket.receive_data())

    my_conn.close()