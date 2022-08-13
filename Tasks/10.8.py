task_text = """
10.8. Модифицируйте класс Element, сделав атрибуты name, symbol и number приватными.
      Определите свойство получателя для каждого атрибута, возвращающее его значение.
"""


# 10.8
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def __str__(self):
        return f"{self.__name}\n{self.__symbol}\n{self.__number}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if str(name).isdecimal():
            raise ValueError("not only numbers")
        self.__name = name

    name = property(get_name, set_name)

    @property
    def symbol(self):
        return self.__symbol

    def set_number(self, number):
        if str(number).isdigit():
            self.__number = int(number)
        else:
            raise ValueError("INT please")

    def get_number(self):
        return self.__number

    number = property(get_number, set_number)


dict1 = {'name': 'Hydrogen',
         'symbol': 'H',
         'number': 1}
hydrogen = Element(**dict1)
print(f"{hydrogen.number = }")
print(task_text)
print(hydrogen)
