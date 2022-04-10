global_dict = {'user': "12345", 'qwerty': "pass", 'aBcD': "qwerty123"}


def login(func):
    def wrapper(*args, **kwargs):
        if authenticate():
            return func(*args, **kwargs)
        return False
    return wrapper


def authenticate() -> bool:
    return True


@login
def check_password(log: str, password: str) -> bool:
    if global_dict.get(log, None) == password:
        return True
    return False


if __name__ == '__main__':
    for i in range(4):
        account_login = input("Login:")
        account_password = input("Password:")

        if check_password(account_login, account_password) is True:
            print("Вы в системе!")
            break

        elif i < 3:
            print("Не правильное Имя или Пароль"
                  "\n" f"У вас осталось {3 - i} попыток")

        if i == 3:
            print("Попытки истекли!")


