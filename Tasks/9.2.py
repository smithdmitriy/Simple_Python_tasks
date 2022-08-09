"""
9.2. Определите функцию генератора get_odds(), которая возвращает нечетные числа из диапазона range(10).
     Используйте цикл for, чтобы найти и вывести третье возвращенное значение.
"""


def get_odds(first=1, last=10, step=2):
    num: int = first
    while num < last:
        yield num
        num += step


counter = 1
for number in get_odds():
    if counter == 3:
        print(number)
    counter += 1
