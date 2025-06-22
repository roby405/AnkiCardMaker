from pynput import keyboard
import threading
import time
from overlay import create_tkinter_overlay, show_overlay


def start_shortcut_listener():
    hotkeys = keyboard.GlobalHotKeys({
        '<alt>+,': show_overlay
    })
    hotkeys.start()


if __name__ == "__main__":
    listener_thread = threading.Thread(target=create_tkinter_overlay, daemon=True)
    listener_thread.start()
    
    start_shortcut_listener()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exited")