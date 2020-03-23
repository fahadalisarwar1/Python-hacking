

def download_file(my_socket):
    print("[+] Downloading file")
    filename = my_socket.receive_data()

    my_socket.receive_file(filename)


