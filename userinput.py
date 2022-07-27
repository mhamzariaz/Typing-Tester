from time import time
import keyboard


class UserInput:

    def __init__(self):
        self.backspaces = 0

    def set_key(self):
        self.backspaces += 1

    def get_user_input(self):
        keyboard.add_hotkey("delete", lambda: self.set_key())

        print('\nUser Typed:', end=" ")
        start = time()
        char = input()
        end = time()

        total_time = end - start
        return char, total_time, self.backspaces
