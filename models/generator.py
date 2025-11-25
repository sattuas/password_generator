import random
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.constants import *


class PasswordGenerator:
    def __init__(self, size, upper=True, lower=True, symbols=True, numbers=True):
        self.size = size
        self.upper = upper
        self.lower = lower
        self.symbols = symbols
        self.numbers = numbers
        self.characters = {
            "upper": LETTERS_UPPER,
            "lower": LETTERS_LOWER,
            "symbols": SYMBOLS,
            "numbers": NUMBERS
        }

    def generate(self):
        lettersUpper = self.characters["upper"]
        lettersLower = self.characters["lower"]
        symbols = self.characters["symbols"]
        numbers = self.characters["numbers"]
        password = ""
        verified = False
        
        options = []
        if self.upper == True:
            options.append(lettersUpper)
        if self.lower == True:
            options.append(lettersLower)
        if self.symbols == True:
            options.append(symbols)
        if self.numbers == True:
            options.append(numbers)

        for i in range(0, self.size):
            characters = random.choice(options)
            password += random.choice(characters)

        while True:
            verified = self._verify_password(password)
            if verified:
                return password

    
    def _verify_password(self, password):
        all_characters = ''
        final_password = ''

        if self.upper == True:
            all_characters += self.characters["upper"]
        if self.lower == True:
            all_characters += self.characters["lower"]
        if self.symbols == True:
            all_characters += self.characters["symbols"]
        if self.numbers == True:
            all_characters += self.characters["numbers"]

        for char in password:
            if char in all_characters:
                final_password += char
            else:
                return False
        
        return True


if __name__ == "__main__":
    pw = PasswordGenerator(16, True, False, True, True)

    print(f'Senha gerada {pw.generate()}')