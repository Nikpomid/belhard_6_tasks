"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n):
    if n > 0:
        return sum_of_numbers(n // 10) + n % 10
    else:
        return 0


print(sum_of_numbers(4151))
