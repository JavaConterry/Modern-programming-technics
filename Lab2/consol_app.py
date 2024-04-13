from password_generator import PasswordGenerator
import sys

# EXCEPTIONS_NUMBER = 0

def main():
    for inp in sys.stdin:
        if(inp == '0'):
            break
        try:
            int_input = int(inp)
            print(PasswordGenerator.new_password(int_input))
        except:
            sys.stderr.write('Input type error')

    # if(EXCEPTIONS_NUMBER == 0):
    sys.exit(0)


if __name__ == '__main__':
    main()