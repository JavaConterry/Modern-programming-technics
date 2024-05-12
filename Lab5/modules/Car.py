import sys

class Car:

    def __init__(self):
        self.im_used = False

    def move(self, arg):
        match arg:
            case 'Forward':
                self.move_forward()
            case 'Backward':
                self.move_backward()
            case 'Right':
                self.move_right()
            case 'Left':
                self.move_left()
            case 'Idk':
                self.babah()
            case _:
                sys.stderr.write('Unknown car command')

    def move_forward(self):
        print('Moving forward')
    def move_backward(self):
        print('Moving backward')
    def move_left(self):
        print('Moving left')
    def move_right(self):
        print('Moving right')
    def babah(self):
        print('!BABAH!')