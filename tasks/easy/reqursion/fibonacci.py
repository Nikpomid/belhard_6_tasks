"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n, x=0, result=1):
    if n != 1:
        return fibonacci(n - 1, result, x + result)
    else:
        return result


print(fibonacci(6))
