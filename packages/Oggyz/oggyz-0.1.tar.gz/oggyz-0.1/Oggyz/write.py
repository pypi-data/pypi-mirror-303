# Oggyz/write.py

import random
from .colors import Colors

class Write:
    @staticmethod
    def Print(text, color=Colors.reset, interval=0.1):
        for char in text:
            print(f"{color}{char}{Colors.reset}", end="", flush=True)
        print()  # In xuống dòng sau khi hoàn thành

    @staticmethod
    def PrintRainbow(text, interval=0.1):
        for char in text:
            color = random.choice(Colors.rainbow)
            print(f"{color}{char}{Colors.reset}", end="", flush=True)
        print()
