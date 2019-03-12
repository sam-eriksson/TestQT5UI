import string
import random

class TextGen():
    
    def randomText(self):
        min_char = 8
        max_char = 12
        allchar = string.ascii_letters + string.digits
        #string.ascii_letters + string.punctuation + string.digits
        text = "".join(random.choice(allchar) for x in range(random.randint(min_char, max_char)))
        return text