import random
import string
import time

class HumanBehavior:
    def type_text_slowly(self, page, selector, text: str, error_probability: float = 0.25, delay_range: tuple = (0.1, 0.3)) -> None:
        """
        Realistically mimics a user's input by typing text slowly, introducing random errors and pauses.

        This method simulates human-like typing behavior by inserting random errors and delays
        between keystrokes.

        Args:
            page: The page context where the input should be typed (e.g., context.new_page()).
            selector: The input selector for the text field where the text will be entered.
            text (str): The text to write in the specified selector.
            error_probability (float, optional): The probability of introducing an error for each lowercase character. Defaults to 0.25 (25%).
            delay_range (tuple, optional): A tuple specifying the minimum and maximum delay (in seconds) between keystrokes. Defaults to (0.1, 0.3).

        Returns:
            None: This method does not return a value. It performs actions directly on the specified page.
    
        Raises:
            ValueError: If delay_range is not a tuple with two values (min, max).
    """
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

