"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n == 1:
        return True
    if n & 1:
        return False
    return check_number(n >> 1)


print(check_number(2))
