import requests, argparse


def live_currency(live_list, currency_now):
    if currency_now.upper()[0] == "U":
        return live_list[0]['sale']
    elif currency_now.upper()[0] == "E":
        return live_list[1]['sale']
    else:
        return float(live_list[2]['sale']) * float(live_list[0]['sale'])
"""
Здесь я не стал изобретать велосипед поэтому я беру из списка словарей по 
индексу(зная что Приват все время отдает данные в такой последовательности)
"""

def live_currency_dated(date_dict, currency_now):
    intermediate_dict = {}
    mega_list = date_dict['exchangeRate']
    for data in mega_list:
        try:
            try:
                intermediate_dict.update({data['currency']: data['saleRate']})
            except KeyError:
                intermediate_dict.update(
                    {data['currency']: data['saleRateNB']})
        except KeyError:
            pass
    print(intermediate_dict)
    return intermediate_dict.get(currency_now.upper(), "PrivatBank SUCKS!")
"""
Двойной try нужен в этом случае для того чтобы не ловить KeyError на ключе 
"currency" т.к. API Привата не постоянный на некоторых датах (2017,2018,
2019...) он выдает совершенно разные результаты(в некоторых словарях просто 
не было ключа "currency", а все доступные валюта есть ниже в списке 
"avaliable_currency_dict_date" и может случиться так что в списке эта валюта 
есть а по факту на какой-то дате ее нету)

И от сюда же сразу вопрос,если у нам есть "достоверная информация" про вывод 
валюты(или другой информации)(и мы знаем что она всегда по ключам одинаковая),
то лучше вывести эти ключи в лист и делать проверку
(если валюты не существует из доступных) до того как сделать запрос
на сервер(чтоб не занимать поток) или уже делать проверку после получения данных?   
"""



if __name__ == '__main__':
    avaliable_currency_dict_live = ["USD", "EUR", "BTC"]
    avaliable_currency_dict_date = ["USD", "EUR", "RUR", "CHF", "GBP", "PLZ",
                                    "SEK", "XAU", "CAD"]

    parser = argparse.ArgumentParser(description="Date(day.month.year) or live"
                                                 "exchange currency")
    parser.add_argument("-c", dest="currency")
    parser.add_argument("-d", dest="date")

    currency_now = parser.parse_args().currency
    currency_date = parser.parse_args().date or 0

    exchange_url_now = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"  # noqa
    exchange_url_with_date = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={currency_date}"  # noqa

    if currency_now.upper() in avaliable_currency_dict_live and \
            currency_date == 0:
        try:
            response_currency = requests.request("POST", exchange_url_now)
        except Exception:
            raise SystemError
        else:
            live_list = response_currency.json()
            print(live_list)
            print(currency_now.upper())
            print(live_currency(live_list, currency_now))

    elif currency_now.upper() in avaliable_currency_dict_date and \
            currency_date != 0:
        try:
            response_currency = requests.request("POST",
                                                 exchange_url_with_date)
        except Exception:
            raise SystemError
        else:
            date_dict = response_currency.json()
            if date_dict['exchangeRate']:
                print(f"{currency_now.upper()} \n \n"
                      f"{live_currency_dated(date_dict, currency_now)}")
            else:
                print(f"Invalid date: {currency_date}")
    else:
        print(f"Invalid currency name:{currency_now}")
