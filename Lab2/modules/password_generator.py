import random
import sys

class PasswordGenerator:
    def new_password(length=4):
        password=''
        for i in range(length):
            password+=chr(random.randint(33, 126))
        return password
    

if __name__=='__main__':
    for inp in sys.stdin:
        if(inp == '0'):
            break
        try:
            int_input = int(inp)
            print(PasswordGenerator.new_password(int_input))
        except:
            sys.stderr.write('Input type error')
    # sys.stdout.write('Program run seccessfuly, no errors occured')
    sys.exit(0)