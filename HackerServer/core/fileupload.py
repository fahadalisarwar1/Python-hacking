from glob import glob
import os
# read file from the disk {Hacker machine }
# read it in the form of bytes
# append a delimeter to the end of bytes
# transfer file over the network
# receive file on clien
#t side
# remove the delimeter from the bytes to recover the original data
# write the file to the client disk

# /home/fahad/sample.csv



def upload_files(my_socket):
    print("[+] Upload files")

    files = glob("*")
    for index, filename in enumerate(files):
        
        new_filename = os.path.basename(filename)
        print("\t\t", index, "\t", new_filename)




    while True:
        try:
            file_index = int(input("[+] Select file : "))
            if len(files) >= file_index >=0:
                fileName = files[file_index]
                break
        except:
            print("[-] Invalid file selected")

    print("[+] Selected File = ", fileName)
    my_socket.send_data(fileName)

    my_socket.send_file(fileName)



    
