from math import sqrt


def quadratic(a, b, c):

    """Finds a root of a quadratic polynomial y = a x^2 + b x + c.

    Arguments:
        a (float): The x^2 coefficient.
        b (float): The x coefficient.
        c (float): The constant.

    Returns:
        float: The result of the quadratic formula.

    Examples:

        >>> print(quadratic(1, 0, 0))
        0.0

        >>> print(quadratic(2, 0, -8))
        2.0

        >>> print(quadratic(-2, 40, -182))
        7.0

    """
    # calculate the quadratic formula
    root = sqrt((b * b) - (4 * a * c))

    # calculate and print the first root
    numerator = -b + root
    x = numerator / (2 * a)
    return x


if __name__ == "__main__":

    # don't use input!
    print(quadratic(2, 0, -1))
