import pyautogui
import time

class RealTimeCords:
    def __init__(self):
        pass
    def print_mouse_position(duration=10):
        """Print mouse coordinates in real-time"""
    
        try:
            while True:
                x, y = pyautogui.position()
                print(f"X: {x}, Y: {y}", end='\r') 
                time.sleep(0.01)  
        except KeyboardInterrupt:
            print("\nRegistration Interrupted!")
