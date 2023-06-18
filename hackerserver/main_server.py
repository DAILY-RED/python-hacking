from core.connection import Serv

if __name__ == "__main__":

    my_socket = ServerConnection()
    my_socket.CreateConnection("", 8080)

    my_socket.Listen()

    my_conn, _ = my_socket.Accept