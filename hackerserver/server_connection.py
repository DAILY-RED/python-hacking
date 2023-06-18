import socket


CHUNK_SIZE = 4 * 1024

class ServerConnection:
    def __init__(self):
        """create a TCP socket for server
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def CreateConnection(self, ip="", port=8000):
        self.server_ip   = ip
        self.server_port = port
        self.address     = (self.server_ip, self.server_port)
        self.socket.bind(self.address)
    
    def Listen(self, backlog = 5):
        self.socket.listen(backlog)

    def AcceptConnection(self):
        self.client_conn, self.client_address = self.socket.accept()
        return (self.client_conn, self.client_address)
    
    def send_data(self, user_input):
        user_input_bytes = bytes(user_input, "utf-8")

        self.client_conn.send(user_input_bytes)
    
    def recieve_data(self):

        received_data_bytes = self.client_conn.recv(CHUNK_SIZE)
        self.data = received_data_bytes.decode('utf-8')
        return self.data