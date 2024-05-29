from .password_generator import PasswordGenerator
import sys

# EXCEPTIONS_NUMBER = 0

def main():
    for inp in sys.stdin:
        try:
            sys.stdout.write(PasswordGenerator.new_password(inp))
        except ValueError as e:
            sys.stderr.write(f'Error occured: {e}\n')
    # sys.stdout.write('Program run seccessfuly, no errors occured')
    sys.exit(4)


if __name__ == '__main__':
    main()