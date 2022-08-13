"""
10.5. Создайте словарь со следующими ключами и значениями: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1.
      Далее создайте объект с именем hydrogen класса Element с помощью этого словаря.
"""


# 10.5
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


pass

dict1 = {'name': 'Hydrogen',
         'symbol': 'H',
         'number': 1}
hydrogen = Element(**dict1)
