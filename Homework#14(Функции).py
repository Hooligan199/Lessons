x = int(input("Number:"))

def without_nul(x):
    """
    This func remove 0 in any number(type: int) and multiply each number wiyh
    each other
    :param x: 123405
    :return: 120
    """
    y = [int(i) for i in str(x)]
    y = [x for x in y if x != 0]

    if y != []:
        tot = 1
    else:
        tot = "Error"


    for g in y:

        tot *= g

    return tot


if __name__ == '__main__':
    print(without_nul(x))

