task_text = """
10.9. Определите три класса: Bear, Rabbit и Octothorpe. Для каждого из них определите всего один метод — eats().
      Он должен возвращать значения 'berries' (для Bear), 'clover' (для Rabbit) или 'campers' (для Octothorpe).
      Создайте по одному объекту каждого класса и выведите на экран то, что ест указанное животное.
"""


class Bear:
    def eats(self):

        return 'berries'


class Rabbit:
    def eats(self):

        return 'clover'


class Octothorpe:
    def eats(self):

        return 'campers'

print(task_text)
b = Bear()
r = Rabbit()
o = Octothorpe()

print(b.eats())
print(r.eats())
print(o.eats())
