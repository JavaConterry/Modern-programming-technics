import unittest

import tkinter as tk
from password_generator import PasswordGenerator
from interface_app import Counter
from consol_app import main

class TestClass(unittest.TestCase):


    def test_password_generator(self):
        p_length = 5
        generated_p = PasswordGenerator.new_password(p_length)
        def in_range(character):
            if(ord(character)<=126 and ord(character)>=33):
                return True
            return False

        count_in_range = 0
        for c in generated_p:
            if(in_range(c)):
                count_in_range+=1

        self.assertEqual(count_in_range, 5, 'Password generates wrong characters')

        
    def test_interface(self):
        window = tk.Tk()
        app = Counter(window)
        self.assertEqual(app.state.get(), 0, 'Interface initialisation is failed')
    

    # def test_console_app(self):


if __name__ == '__main__':
    unittest.main()
