import random
import sys

class PasswordGenerator:
    def new_password(length=4):
        try:
            length = int(length)
        except:
            raise ValueError("Wrong type given.")
        if(length<=1):
            raise ValueError("Length should be rational.")
        password=''
        for i in range(length):
            password+=chr(random.randint(33, 126))
        return password
    

# if __name__=='__main__':
#     for inp in sys.stdin:
#         if(inp == '0'):
#             break
#         try:
#             int_input = int(inp)
#             print(PasswordGenerator.new_password(int_input))
#         except:
#             sys.stderr.write('Input type error')
#     # sys.stdout.write('Program ran seccessfuly, no errors occured')
#     # sys.exit(0)