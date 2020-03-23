from core.connection import ServerConnection

from core.handleConnection import handleConnection

 
if __name__ == "__main__":

    my_socket = ServerConnection()
    print("[+] Waiting for incoming connection on port 8080")
    my_socket.CreateConnection("", 8082)


    my_socket.Listen()


    my_conn, _ = my_socket.AccepConnection()


    handleConnection(my_socket)

    my_conn.close()
    