import time
import random
import string


def typewritter_effect(text: str, min_delay: float = 0.05, max_delay: float = 0.03, error_chance: float = 0.12):
    for char in text:
        delay = random.uniform(min_delay, max_delay)

        if random.random() < error_chance:
            error_char = random.choice(string.ascii_lowercase + " ")    # In case of "punctuation" errors: error_char = random.choice(string.ascii_lowercase + string.punctuation + " ")
            print(error_char, end = '', flush = True)
            time.sleep(delay)

            print('\b', end = '', flush = True)
            time.sleep(min_delay)


        print(char, end = '', flush = True)
        time.sleep(delay)


typewritter_effect("Hyoo! this is a test of a typewritter machine effect with a 12% chance of miss-spelling a word!", 0.2, 0.1, error_chance = 0.12)