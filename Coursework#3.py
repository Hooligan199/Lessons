import requests, argparse


def live_currency(live_list, currency_now):
    if currency_now.upper()[0] == "U":
        return live_list[0]['sale']
    elif currency_now.upper()[0] == "E":
        return live_list[1]['sale']
    else:
        return float(live_list[2]['sale']) * float(live_list[0]['sale'])


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
