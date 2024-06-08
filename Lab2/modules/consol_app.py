from .password_generator import PasswordGenerator
import sys

# EXCEPTIONS_NUMBER = 0

def main():
    for inp in sys.stdin:
<<<<<<< HEAD
        try:
            sys.stdout.write(PasswordGenerator.new_password(inp))
        except ValueError as e:
            sys.stderr.write(f'Error occured: {e}\n')
    # sys.stdout.write('Program run seccessfuly, no errors occured')
    sys.exit(4)
=======
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
>>>>>>> 207f238d673c0804545dc98c95378120d363d74a


if __name__ == '__main__':
    main()