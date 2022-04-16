from threading import Timer
from datetime import datetime, timedelta
global_dict = {'user': "12345", 'qwerty': "pass", 'aBcD': "qwerty123"}
just_x = None


def login(func):
    def wrapper():
        if check_password(account_login, account_password):
            return func()
        return False
    return wrapper


@login
def authenticate() -> bool:
    return True


def check_password(account_login: str, account_password: str) -> bool:
    return global_dict.get(account_login, None) == account_password


def one_more_time():
    for i in range(4):
        account_login = input("Login:")
        account_password = input("Password:")

        if check_password(account_login, account_password) is True:
            print("Вы в системе!")
            break

        elif i < 3:
            print("Не правильное Имя или Пароль"
                  "\n" f"У вас осталось {3 - i} попыток")

        if i == 3 and authenticate() is False:
            print("На этом все!")


if __name__ == '__main__':
    DEFAULT_TIMER = Timer(10.0, one_more_time)
    # Таймер сделал специально небольшим чтобы долго не ждать
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
            just_x = datetime.now()
            print("До след попытки осталось {} минут".format(
                just_x + timedelta(minutes=5) - just_x))
            DEFAULT_TIMER.start()


