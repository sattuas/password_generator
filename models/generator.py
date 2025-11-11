import random


class PasswordGenerator:
    def __init__(self, size, upper=True, lower=True, symbols=True):
        self.size = size
        self.upper = upper
        self.lower = lower
        self.symbols = symbols

    def generate(self):
        ...