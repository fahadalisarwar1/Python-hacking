import socket


SERVER_IP = ""
SERVER_PORT = 8080

if __name__  == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = (SERVER_IP, SERVER_PORT)
    sock.bind(address)

    sock.listen(1)

    print("[+] Waiting for incoming connection ", SERVER_PORT)
    client_sock, client_add = sock.accept()
    print("[+] Connection established :", client_add)


    msg = "This is the server speaking"

    client_sock.send(msg.encode())

    client_sock.close()
    sock.close()


