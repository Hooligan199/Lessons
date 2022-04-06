x = int(input("X равен: "))
y = int(input("У равен: "))

operation = str(input("Математическая операция: "))


def arithmetic(x, y, operation):
    """
    This func takes 3 variables (x, y ,operation), use them to make a
    math operation (only: *, /, +, -) and return the result

    :param x: 2
    :param y: 2
    :param operation: *
    :return: 4
    """

    dict_of_operations = {"*": int.__mul__(x, y), "/": int.__truediv__(x, y),
                          "-": int.__sub__(x, y), "+": int(x + y)}

    return \
        dict_of_operations.get(operation, "Неизвестная операция")


if __name__ == '__main__':
    print(f"x {operation} y =", arithmetic(x, y, operation))
