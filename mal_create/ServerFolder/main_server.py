from server_connection import *
from handleConnectionS import handleConnection

if __name__ == "__main__":

    my_socket = ServerConnection()
    print("[+] Waiting for incoming connection on port 8080")
    my_socket.CreateConnection("", 8080)

    my_socket.Listen()

    my_conn, _ = my_socket.AcceptConnection()

    handleConnection(my_socket)

    #my_socket.send_data("Hi this is server")
    #print(my_socket.receive_data())

    my_conn.close()