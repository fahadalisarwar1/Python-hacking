

def run_command(my_socket):
    print("[+] Running commands")
    while True:
        command  = input(">> ")

        my_socket.send_data(command)
        if command == "":
            continue

        if command == "stop":
            break
        result = my_socket.receive_command_result()
        print(result)