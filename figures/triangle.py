import math


def area(a, b, c):
    """
    Calculates the area of a triangle.

        Parameters:
            a (int): side of the triangle.
            b (int): side of the triangle.
            c (int): side of the triangle

        Return value:
            (int) : the area of a triangle.

        Example:
            area(3, 4, 5)
            p = (a + b + c) / 2
            p = (3 + 4 + 5) / 2 = 6
            area = sqrt(p*(p - a)*(p - b)*(p-c))
            sqrt(6(6 - 3)(6 - 4)(6 - 5)) = 6
            returns 6
    """
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle.

        Parameters:
            a (int): side of a triangle.
            b (int): side of a triangle.
            c (int): side of a triangle.

        Return value:
            (int) : the perimeter of a triangle.

        Example:
            perimeter(4, 4, 4)
            (4 + 4 + 4) = 12
            returns 12
    """
    return int(a + b + c)
