import argparse
import sys
global_dict = {'user': "12345", 'qwerty': "pass", 'aBcD': "qwerty123"}
just_x = 0


def login(func):
    def wrapper(account_login, account_password):
        if check_password(account_login, account_password):
            return func()
        return False
    return wrapper


@login
def authenticate() -> bool:
    if login:
        return False
    return True


def check_password(account_login: str, account_password: str) -> bool:
    return global_dict.get(account_login, None) == account_password


def one_more_time():
    for i in range(4):
        global just_x
        just_x = i
        from_terminal(account_login, account_password)

        if check_password(account_login, account_password) is True:
            print("Вы в системе!")
            sys.exit()

        elif i < 3:
            print("Не правильное Имя или Пароль"
                  "\n" f"У вас осталось {3 - i} попыток")

        elif i == 3 and authenticate() is False:
            print("На этом все!")


def from_terminal(account_login, account_password):
    if just_x == 0:
        if account_login == 0:
            account_login = input("Login:")
            return check_password(account_login, account_password)

        elif account_password == 1:
            account_password = input("Password:")
            return check_password(account_login, account_password)

    if just_x > 0:
        account_login = input("Login:")
        account_password = input("Password:")

        return check_password(account_login, account_password)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter to the sys with "
                                                 "login and password")
    parser.add_argument("-l", dest="username", default=0)
    parser.add_argument("-p", dest="password",  default=1)

    account_login = parser.parse_args().username
    account_password = parser.parse_args().password

    one_more_time()

