import random
import sys

class PasswordGenerator:
    def new_password(length=4):
<<<<<<< HEAD
        try:
            length = int(length)
        except:
            raise ValueError("Wrong type given.")
        if(length<=1):
            raise ValueError("Length should be rational.")
=======
>>>>>>> 207f238d673c0804545dc98c95378120d363d74a
        password=''
        for i in range(length):
            password+=chr(random.randint(33, 126))
        return password
    

<<<<<<< HEAD
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
=======
if __name__=='__main__':
    for inp in sys.stdin:
        if(inp == '0'):
            break
        try:
            int_input = int(inp)
            print(PasswordGenerator.new_password(int_input))
        except:
            sys.stderr.write('Input type error')
    # sys.stdout.write('Program ran seccessfuly, no errors occured')
    # sys.exit(0)
>>>>>>> 207f238d673c0804545dc98c95378120d363d74a
