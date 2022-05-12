import requests

URL_POPULATION = "https://countriesnow.space/api/v0.1/countries/population/cities"
URL_CURRENCY = "https://countriesnow.space/api/v0.1/countries/currency"


def checking_errors(dict_resp_population, dict_resp_currency):
    if dict_resp_population['error'] is not True:
        return take_city(dict_resp_population, dict_resp_currency)
    else:
        print(f"Invalid city name:{user_input}")
        pass


def take_city(dict_resp_population, dict_resp_currency):
    print(dict_resp_population['data']['city'].capitalize())
    print("\n")
    return take_country(dict_resp_population, dict_resp_currency)


"""
Почему в некоторые функции нужно передовать одну спец переменную которая будет в 
дальнейшем использоваться для другой функции, а в некотрые не нужно? 
"""
def take_country(dict_resp_population, dict_resp_currency):
    print(dict_resp_population['data']['country'])
    return take_currency(dict_resp_currency)  # Вот например тут


def take_currency(dict_resp_currency):
    print(dict_resp_currency['data']['currency'])
    return take_population(dict_resp_population)  # И тут

"""
И не лучше будет просто вместо того чтобы передовать какую-то переменную по 
всем функциям, использовать    global "названия переменной"?

Также как я делал в 20 домашке, вместо того чтобы передавать миллион переменных
по всем функциям которые нужно только для одной. Я использовал global. 

А также хотел спросить если у вас, в глобальном видении переменная например 
равна 0, и мы передали ее в функцию не через global, то как сделать так чтобы
она изменилась глобально?(я пробовал вписывать эту переменную в return вместе 
с другими функциями и переменными, но что-то пошло не так и она не изменилась)      
"""

def take_population(dict_resp_population):
    print(dict_resp_population['data']['populationCounts'][0]['value'])


if __name__ == '__main__':
    user_input = input("City:")
    payload_population = dict_resp_currency = \
        dict_resp_population = {}
    payload_currency = {}

    payload_population.update({"city": user_input.capitalize()})

    try:
        response_population = requests.request("POST", URL_POPULATION,
                                           data=payload_population)
    except Exception:
        raise SystemError

    else:
        dict_resp_population = response_population.json()
        if dict_resp_population['error'] is not True:
            payload_currency.update(
                {"country": dict_resp_population['data']['country']}
            )
        else:
            pass
    try:
        response_currency = requests.request("POST", URL_CURRENCY,
                                         data=payload_currency)
    except Exception:
        raise SystemError
    else:
        dict_resp_currency = response_currency.json()
        checking_errors(dict_resp_population, dict_resp_currency)

