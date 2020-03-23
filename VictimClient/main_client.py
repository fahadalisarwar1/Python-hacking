from core.connection import ClientConnection
from core.handleConnection import handleConnection

if __name__ == "__main__":
    my_socket = ClientConnection()

    my_socket.Connect("192.168.0.42", 8082)

    handleConnection(my_socket)

    my_socket.close()

