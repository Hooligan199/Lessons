import math

square_side = int(input("Сторона квадрата: "))

def square(square_side):
    """
    This func takes 1 variable (square_side), calculate 3 values
    (square_perimetr, square_area, square_diagonal) and the result is printed
    in tuple type

    :param square_side: 2
    :return: (square_perimetr(8), square_area(4),
     square_diagonal(2.8284271247461903))
    """
    square_perimetr = square_side * 4
    square_area = square_side * square_side
    square_diagonal = square_side * math.sqrt(2)

    return print((square_perimetr, square_area, square_diagonal))


if __name__ == '__main__':
    square(square_side)
