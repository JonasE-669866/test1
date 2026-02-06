import numpy as np


def func(mul1, mul2):

    res = np.multiply(mul1, mul2)

    return res


def func2(a, b):
    return np.add(a, b)


def func3(a, b):
    return a*b


if __name__ == "__main__":
    mul1 = 2
    mul2 = 3

    print(func(mul1, mul2))
    print(func2(mul1, mul2))
    print(func3(mul1, mul2))
