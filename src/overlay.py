import tkinter as tk
from tkinter import ttk
import threading
from pynput import keyboard
import time

from screenshotter import take_screenshot_of_subsection

root = None
app = None

class TkinterOverlay:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Picker")
        self.root.geometry("500x70")
        
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.7)
        
        self.create_widgets()
        
        self.root.after(100, self.ensure_topmost)
        
        self.entry.bind("<Return>", self.on_submit)
        self.entry.focus_set()
        
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="5")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        label = ttk.Label(main_frame, text="Choose a word/phrase:")
        label.pack(pady=5)
        self.entry = ttk.Entry(main_frame)
        self.entry.pack(pady=5, fill=tk.X)
        
        button = ttk.Button(main_frame, text="Submit", command=self.on_submit)
        button.pack(pady=5)
        self.is_topmost = True
        
    def on_submit(self, event=None):
        entered_text = self.entry.get()
        if not entered_text.strip():
            return
        print(f"Creating an image with the sentence for the phrase '{entered_text}'")
        take_screenshot_of_subsection(output_filename=f"{entered_text}.png")
        print(f"Image saved as {entered_text}.png")
        self.hide()
        
    
    def ensure_topmost(self):
        if self.is_topmost:
            self.root.attributes("-topmost", True)
            self.root.lift()
    
    def hide(self):
        self.is_topmost = False
        self.entry.delete(0, tk.END)
        self.root.withdraw()
    
    def show(self):
        self.is_topmost = True
        self.root.deiconify()
        self.entry.focus_set()
        self.ensure_topmost()

    
def create_tkinter_overlay():
    global root, app
    root = tk.Tk()
    root.withdraw()
    app = TkinterOverlay(root)
    root.mainloop()
    # app = TkinterOverlay(root)

def show_overlay():
    global app
    app.show()
