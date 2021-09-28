"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n, x=1, result=1):
    if n < 0:
        raise ValueError("ValueError")
    if x <= n:
        return factorial(n, x + 1, result * x)
    else:
        return result


print(factorial(3))
