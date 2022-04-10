x = [int(i) for i in str(input("Number:")) if int(i) != 0]
print(x)

def without_nul(x):
    """
    This func remove 0 in any number(type: int) and multiply each number with
    each other
    :param x: 123405
    :return: 120
    """
    tot = 1
    for g in x:

        tot *= g

    return tot


if __name__ == '__main__':
    print(without_nul(x))

