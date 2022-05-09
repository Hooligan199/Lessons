import json
from datetime import datetime, timedelta

"""
Основная идея этого кода была в том, чтобы максимально возможно приблизить его
к реальному случаю(...Имя пользователя уже занято. Попробуйте еще раз!)
"""


def input_args():
    """

    Data entry function

    :return:
    """
    account_login = input("Login:")
    account_password = input("Password:")
    return check_login(account_login, account_password)


def check_login(account_login: str, account_password: str):
    """

    Function for checking user's login. If login exists, it returns
    check_password(account_login, account_password), if not it goes
    to registration

    :param account_login: str
    :param account_password: str
    :return: func
    """
    if account_login in global_dict.keys():
        return check_password(account_login, account_password)
    else:
        return registration(account_login, account_password)


def registration(account_login: str, account_password: str):
    """

    It's a registration function. At first, it asks if you want to registrate
    or not(if not, the function will be skipped).It's also checking if new
    username exists in old dictionary(If yes, asked user to create not yet
    existing name. if not, it saves new username and password into global_dict)

    :param account_login: str
    :param account_password: str
    :return: func
    """
    global ONLY_ONCE, ROUND_COUNTER

    if ONLY_ONCE == 0:
        input_reg_answer = input("Похоже вас нету в системе, "
                                 "не хотите зарегистрироваться? \n Yes/No: "
                                 ).strip()
        while ROUND_COUNTER == 0:
            if input_reg_answer.lower()[0] == "y":
                new_login = input("Введите новый логин: ").strip()
                new_password = input("Введите пароль: ").strip()
                if new_login in global_dict.keys():
                    print("Имя пользователя уже занято. Попробуйте еще раз!")
                else:
                    global_dict.update({new_login: new_password})
                    print(global_dict)
                    ONLY_ONCE += 1
                    ROUND_COUNTER += 1
                    input_args()
            elif input_reg_answer.lower()[0] == "n":
                ONLY_ONCE += 1
                ROUND_COUNTER += 1
                input_args()
    else:
        return check_password(account_login, account_password)


def check_password(account_login: str, account_password: str):
    """

    Checking user's password and is everything is ok it returns authenticate(),
    if not fail_attempt(account_login)

    :param account_login: str
    :param account_password: str
    :return: func
    """
    if global_dict.get(account_login) == account_password:
        return authenticate()
    else:
        return fail_attempt(account_login)


def authenticate():
    """

    Final user's authentiction (if login and password are correct)

    :return: -
    """
    save_to_json()
    print("Вы в системе!")


def fail_attempt(account_login):
    """

    This func is a counter(how many attempts left out of 3)
     and dictionary(fail_attempt_dict) updater

    :param account_login: str
    :return: func or nothing
    """
    global JUST_COUNTER
    if JUST_COUNTER < 3:
        fail_attempt_dict.update(
            {f"{account_login}_last_fail": str(datetime.now())}
        )
        print("Не правильное Имя или Пароль"
              "\n" f"У вас осталось {3 - JUST_COUNTER} попыток")
        JUST_COUNTER += 1
        print(fail_attempt_dict)
        save_to_json()
        return input_args()

    if JUST_COUNTER == 3:
        JUST_COUNTER += 1
        fail_attempt_dict.update(
            {f"{account_login}_last_fail": str(datetime.now())}
        )
        save_to_json()
        print("На этом все")


def save_to_json():
    """

    Function that dump jsonData into JSON file(main_args.json)

    :return: -
    """
    global jsonData, global_dict, fail_attempt_dict

    opened_file_write = open("main_args.json", "w")
    json.dump(jsonData, opened_file_write)
    opened_file_write.close()


if __name__ == '__main__':
    opened_file_read = open("main_args.json", "r")
    jsonData = json.loads(opened_file_read.read())

    global_dict = jsonData.get('global_dict')
    fail_attempt_dict = jsonData.get('fail_attempt_dict')
    ONLY_ONCE = jsonData.get('ONLY_ONCE')
    JUST_COUNTER = jsonData.get('JUST_COUNTER')
    ROUND_COUNTER = jsonData.get('ROUND_COUNTER')

    opened_file_read.close()
    """
    Промежуточный словарь для преобразования значений fail_attempt_dict в
    datetime.datetime формат
    """
    fail_dict_intermediate = {}
    for keys, value in fail_attempt_dict.items():
        value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
        fail_dict_intermediate.update({keys: value})


    account_login = input("Login:")
    account_password = input("Password:")

    ban_time = fail_dict_intermediate.get(
            f"{account_login}_last_fail",
            datetime.now() - timedelta(minutes=5))

    if ban_time + timedelta(minutes=5) <= datetime.now():
        check_login(account_login, account_password)
    else:
        print("Вы в бане!")
        print(
            f"Осталось {ban_time - datetime.now() + timedelta(minutes=5)} мин "
            f"до разблокировки!"
        )

