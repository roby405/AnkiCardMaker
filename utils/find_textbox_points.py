from pynput import mouse

def on_click(x, y, button, pressed):
    """
    This function is called whenever a mouse button is pressed or released.
    """
    if pressed:  # Check if the button was pressed (not released)
        if button == mouse.Button.left:
            print(f"Left click at: x={x}, y={y}")
            # If you want to stop listening after the first click, uncomment the next line:
            # return False # This stops the listener

def main():
    print("Listening for left clicks... Press Ctrl+C to stop.")
    # Create a listener for mouse events
    with mouse.Listener(on_click=on_click) as listener:
        listener.join() # Keep the script running until the listener is stopped

if __name__ == "__main__":
    main()