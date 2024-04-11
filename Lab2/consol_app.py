from password_generator import PasswordGenerator
import sys

def main():
    while(True):
        input_str = input('Input password length: ')
        if(input_str == '0'):
            break
        try:
            int_input = int(input_str)
            print(PasswordGenerator.new_password(int_input))
        except:
            print('Input error', file=sys.stderr)

    sys.exit(0)


if __name__ == '__main__':
    main()