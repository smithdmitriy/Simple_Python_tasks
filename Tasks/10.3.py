"""
10.3. Создайте еще один класс, который, конечно же, называется Thing3.
      В этот раз присвойте значение 'xyz' атрибуту объекта letters. Выведите на экран значение атрибута letters.
      Понадобилось ли вам создавать объект класса, чтобы сделать это?
"""


class Thing3:
    pass


example = Thing3()
example.letters = "abc"
print("\n10.3. Создайте еще один класс, который, конечно же, называется Thing3. \
В этот раз присвойте значение 'xyz' атрибуту объекта letters. Выведите на экран значение атрибута letters. \
Понадобилось ли вам создавать объект класса, чтобы сделать это?\n")
print(f"{example.letters = }\n")
