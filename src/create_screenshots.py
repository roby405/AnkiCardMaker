import tkinter as tk
from pynput import keyboard
from pynput.keyboard import Key
import threading
import os

current_keys = set()

def on_press(key, injected):
    try:
        print('alphanumeric key {} pressed; it was {}'.format(
            key.char, 'faked' if injected else 'not faked'))
        current_keys.add(key)
        check_shortcut()
    except AttributeError:
        current_keys.add(key)
        print('special key {} pressed'.format(
            key))
        check_shortcut()

def on_release(key, injected):
    current_keys.remove(key)
    print(current_keys)
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))

def check_shortcut():
    if Key.shift_l in current_keys and Key.ctrl_l in current_keys and '/' in current_keys:
        print("yay win")

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    pass