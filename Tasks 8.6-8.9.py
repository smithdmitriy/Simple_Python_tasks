"""
8.6. Создайте многоуровневый словарь life. Используйте следующие строки для ключей верхнего уровня:
     'animals', 'plants' и 'other'. Сделайте так, чтобы ключ 'animals' ссылался на другой словарь,
     имеющий ключи 'cats', 'octopi' и 'emus'. Сделайте так, чтобы ключ 'cats' ссылался на список строк
     со значениями 'Henri', 'Grumpy' и 'Lucy'. Остальные ключи должны ссылаться на пустые словари.
8.7. Выведите на экран высокоуровневые ключи словаря life.
8.8. Выведите на экран ключи life['animals'].
8.9. Выведите значения life['animals']['cats'].
"""

# 8.6
plants = {}
other = {}
octopi = {}
emus = {}
cats = ['Henri', 'Grumpy', 'Lucy']
animals = {'cats': cats, 'octopi': octopi, 'emus': emus}
life = {'animals': animals, 'plants': plants, 'other': other}

# 8.7
print('\n8.7. Выведите на экран высокоуровневые ключи словаря life.')
print(list(life.keys()))

# 8.8
print("\n8.8. Выведите на экран ключи life['animals'].")
print(list(life['animals'].keys()))

# 8.9
print("\n8.9. Выведите значения life['animals']['cats'].")
print(life['animals']['cats'])
