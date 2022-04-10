global_dict = {'user': "12345", 'qwerty': "pass", 'aBcD': "qwerty123"}


def login(func):
    def wrapper(log: str, password: str):





@login
def authenticate() -> bool:
    return True


@login
def check_password(log: str, password: str) -> bool:
    if global_dict.get(log, None) == password:
        return True
    return False

if __name__ == '__main__':
    for i in range(4):
        account_login = str(input("Login:"))

        account_password = str(input("Password:"))




