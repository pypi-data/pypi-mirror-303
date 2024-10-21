import random
import string

class PasswordGen():
    def __init__(self):
        pass
    
    def gen_password(self):
        special_char = "?!£$%&();"
        rand_number = str(random.randint(1, 999))
        password = "".join(random.choices(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + special_char + rand_number , k=18))
        return password