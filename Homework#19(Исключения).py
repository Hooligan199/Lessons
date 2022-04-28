import argparse

global_dict = {'user': "12345", 'qwerty': "pass", 'aBcD': "qwerty123"}

JUST_X = 0


class UserDoesNotExist(Exception):
    pass


def login(func):
    def wrapper(account_login, account_password):
        if check_password(account_login, account_password):
            return func()
        return False

    return wrapper


@login
def authenticate() -> bool:
    return True


def check_password(account_login: str, account_password: str) -> bool:
    try:
        return global_dict[account_login] == account_password
    except KeyError:
        print("Error")
        raise UserDoesNotExist


def one_more_time(account_login, account_password, JUST_X):
    if authenticate(account_login, account_password) is True:
        print("Вы в системе!")
        pass

    elif JUST_X < 3 and authenticate(account_login, account_password) \
            is False:
        print("Не правильное Имя или Пароль"
              "\n" f"У вас осталось {3 - JUST_X} попыток")
        from_terminal(JUST_X)

    elif JUST_X == 3 and authenticate(account_login, account_password) \
            is False:
        print("На этом все!")


def from_terminal(JUST_X):
    account_login = input("Login:")
    account_password = input("Password:")
    JUST_X += 1
    return one_more_time(account_login, account_password, JUST_X)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter to the sys with "
                                                 "login and password")
    parser.add_argument("-l", dest="username")
    parser.add_argument("-p", dest="password")

    account_login = parser.parse_args().username or input("Login:")
    account_password = parser.parse_args().password or input("Password:")

    one_more_time(account_login, account_password, JUST_X)
