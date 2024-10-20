import random
import string
import time

class HumanBehavior:
    def type_text_slowly(self, page, selector, text, error_probability=0.25, delay_range=(0.1, 0.3)):
        """Realistically mimics a user's input"""
        if not isinstance(delay_range, tuple) or len(delay_range) != 2:
            raise ValueError("delay_range must be a tuple with two values (min, max).")
        for char in text:
            if random.random() < error_probability and char.islower():
                wrong_char = random.choice(string.ascii_lowercase)
                page.type(selector, wrong_char)
                time.sleep(random.uniform(delay_range[0], delay_range[1]))
                page.keyboard.press("Backspace")
                time.sleep(random.uniform(delay_range[0], delay_range[1]))
            page.type(selector, char)
            time.sleep(random.uniform(delay_range[0], delay_range[1]))

