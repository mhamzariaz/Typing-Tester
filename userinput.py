import keyboard
from time import time


class UserInput:

    def __init__(self):
        self.backspaces = 0

    def set_key(self):
        self.backspaces += 1

    def get_user_input(self):
        keyboard.add_hotkey("delete", lambda: self.set_key())

        print('\nUser Typed:', end=" ")
        start_time = time()
        char = input()
        end_time = time()

        return {
            'Input': char,
            'Backspaces': self.backspaces,
            'Start Time': start_time,
            'End Time': end_time
        }
