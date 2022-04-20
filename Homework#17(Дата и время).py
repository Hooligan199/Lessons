from datetime import datetime, timedelta
global_dict = {'user': "12345", 'qwerty': "pass", 'aBcD': "qwerty123"}
just_x = datetime.now()


def login(func):
    def wrapper():
        if check_password(account_login, account_password):
            return func()
        return False
    return wrapper


@login
def authenticate():
    if login(authenticate()) is False:
        global just_x
        just_x = datetime.now()
        return False, just_x
    else:
        return True


def check_password(account_login: str, account_password: str) -> bool:
    return global_dict.get(account_login, None) == account_password


if __name__ == '__main__':
    for i in range(4):
        account_login = input("Login:")
        account_password = input("Password:")

        if authenticate() is True:
            print("Вы в системе!")
            break

        elif i < 3:
            print("Не правильное Имя или Пароль"
                  "\n" f"У вас осталось {3 - i} попыток")

        if i == 3 and authenticate() is False:
            print("Попытки истекли!")
            print("Вы заблокированы! Следующая попытка через {} мин.".format
                  (just_x + timedelta(minutes=5) - just_x))





