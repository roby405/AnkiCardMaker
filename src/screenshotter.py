import mss
from PIL import Image

points = [(75, 566), (1164, 704)]

def take_screenshot_of_subsection(points=points, output_filename="default.png"):
    height = points[1][1] - points[0][1]
    width = points[1][0] - points[0][0]
    
    with mss.mss() as sct:
        monitor_region = {
            "top": points[0][1],
            "left": points[0][0],
            "width": width,
            "height": height
        }
        
        sct_img = sct.grab(monitor_region)
        img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
        img.save(output_filename)
    
    return True if img else False
        
if __name__ == "__main__":
    success = take_screenshot_of_subsection(points, "screenshot.png")
    if success:
        print("Screenshot taken successfully.")
    else:
        print("Failed to take screenshot.")
        