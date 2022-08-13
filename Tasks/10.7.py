task_text = """
10.7. Вызовите функцию print(hydrogen). В определении класса Element измените имя метода dump на __str__,
      создайте новый объект hydrogen и затем снова вызовите метод print(hydrogen).
"""


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f"{self.name}\n{self.symbol}\n{self.number}"


dict1 = {'name': 'Hydrogen',
         'symbol': 'H',
         'number': 1}
hydrogen = Element(**dict1)
print(task_text)
print(hydrogen)
