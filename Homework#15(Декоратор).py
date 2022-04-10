global_dict = {'user': "12345", 'qwerty': "pass", 'aBcD': "qwerty123"}


def check_password(log: str, password: str) -> bool:
    if log in global_dict.keys():
        return global_dict.get(account_login) == password
    return False


if __name__ == '__main__':
    for i in range(4):
        account_login = str(input("Login:"))

        account_password = str(input("Password:"))

        if check_password(account_login, account_password) is True:
            print("Вы в системе!")
            break

        elif i < 3:
            print("Не правильное Имя или Пароль" 
                  "\n" f"У вас осталось {3-i} попыток")

        if i == 3:
            print("Попытки истекли!")


