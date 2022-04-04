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

    if operation == "*":
        return x * y

    elif operation == "/":
        return x / y

    elif operation == "+":
        return x + y

    elif operation == "-":
        return x - y

    else:
        return "Неизвестная операция"


if __name__ == '__main__':
    print(f"x {operation} y =", arithmetic(x, y, operation))
