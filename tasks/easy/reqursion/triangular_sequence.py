"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, x=1, string=""):
    string += str(x) * x + '\n'
    if n < 0:
        raise ValueError("ValueError")
    if x != n:
        return triangular_sequence(n, x + 1, string)
    else:
        return string


print(triangular_sequence(3))
