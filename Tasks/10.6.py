task_text = """
10.6. Для класса Element определите метод с именем dump(), который выводит на экран значения
      атрибутов объекта (name, symbol и number). Создайте объект hydrogen из этого нового определения и
      используйте метод dump(), чтобы вывести на экран его атрибуты.
"""


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        return f"{self.name}\n{self.symbol}\n{self.number}"


dict1 = {'name': 'Hydrogen',
         'symbol': 'H',
         'number': 1}
hydrogen = Element(**dict1)
print(task_text)
print(hydrogen.dump())
