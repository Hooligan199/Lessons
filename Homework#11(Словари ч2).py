dict_1 = {'a': 1, 'b': 2, 'c': 3, 'z': 9000, 'x': 500, "lk": 321}

dict_2 = {'z': 1, 'x': 6000, 'c': 6, 'a': 3, 'b': 100, "qwerty": 852456}

dict_3 = {}

for keys1, values1 in dict_1.items():
    for keys2, values2 in dict_2.items():
        if keys1 == keys2 and values1 >= values2:

            dict_3.update({keys1: values1})

        elif keys2 == keys1 and values2 >= values1:

            dict_3.update({keys2: values2})

        elif keys2 != keys1 and keys1 != keys2:

            dict_3.update({keys2: values2})
            dict_3.update({keys1: values1})


print(dict_3)
