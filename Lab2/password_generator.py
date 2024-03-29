import random


class PasswordGenerator:
    def new_password(length=4):
        password=''
        for i in range(length):
            password+=chr(random.randint(33, 126))
        return password