import numpy as np


def func(mul1, mul2):

    res = np.multiply(mul1, mul2)

    return res


if __name__ == "__main__":
    mul1 = 2
    mul2 = 3

    print(func(mul1, mul2))
