from .password_generator import PasswordGenerator
import sys

# EXCEPTIONS_NUMBER = 0

def main():
    for inp in sys.stdin:
        print(inp)   
        if(inp == '0'):
            break
        try:
            int_input = int(inp)
            sys.stdout.write(PasswordGenerator.new_password(int_input))
        except:
            sys.stderr.write('Input type error')
    # sys.stdout.write('Program run seccessfuly, no errors occured')
    sys.exit(0)


if __name__ == '__main__':
    main()