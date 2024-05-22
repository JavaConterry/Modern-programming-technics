import unittest
from unittest.mock import patch
from unittest import mock
import sys
import tkinter as tk
import os
from modules.password_generator import PasswordGenerator
# from modules.interface_app import Counter
from modules.consol_app import main
from io import StringIO

class TestClass(unittest.TestCase):

    def valid_password(password):
        def in_range(character):
            if(ord(character)<=126 and ord(character)>=33):
                return True
            return False

        count_in_range = 0
        for c in password:
            if(in_range(c)):
                count_in_range+=1
        return count_in_range == len(password)


    def test_password_generator(self):
        p_length = 5
        generated_p = PasswordGenerator.new_password(p_length)
        self.assertEqual(TestClass.valid_password(generated_p), True, 'Password generates wrong characters')


    @patch('sys.stdout', new_callable=StringIO)
    def test_any_stdout(self, stdout):
        input_data = StringIO("10\n0\n")
        with mock.patch('sys.stdin', input_data):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertTrue(len(stdout.getvalue()) > 0, 'No output')


    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_stdout(self, stdout):
        input_data = StringIO("10\n0\n")
        with mock.patch('sys.stdin', input_data):
            with self.assertRaises(SystemExit):
                main()
            self.assertTrue(len(stdout.getvalue())>9, 'Nonvalid output')

    @patch('sys.stderr', new_callable = StringIO)
    def test_stderr(self, stderr):
        input_data = StringIO("asdfasd\n")
        with mock.patch('sys.stdin', input_data):
            with self.assertRaises(SystemExit):
                main()
            self.assertEqual(stderr.getvalue(), 'Input type error')

    
    @patch('sys.stdin', StringIO('10\n'))
    @patch('sys.stdout', new_callable=StringIO)
    def test_stdin(self, stdin, stdout):
        main()
        self.assertTrue(len(stdout.getvalue())==10, 'no input')


    def test_exit_code(self):
        input = StringIO("10\n0\n")
        with sys.stdin as original_stdin, input as created_input:
            sys.stdin = created_input
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)
        sys.stdin = original_stdin


    

    # def test_interface(self):
    #     window = tk.Tk()
    #     app = Counter(window)
    #     self.assertEqual(app.state.get(), 0, 'Interface initialisation is failed')

if __name__ == '__main__':
    unittest.main()
