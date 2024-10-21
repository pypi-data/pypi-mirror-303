import pyautogui
import time

class RealTimeCords:
    def __init__(self):
        pass
    def print_mouse_position():
        """Description: 
        - sends the cords on which you are moving the mice on the screen Args: Nobody Return: X and y coordinates
        
        Return:
        - x and y coordinates
        """
        try:
            while True:
                x, y = pyautogui.position()
                print(f"X: {x}, Y: {y}", end='\r') 
                time.sleep(0.01)  
        except KeyboardInterrupt:
            print("\nRegistration Interrupted!")
