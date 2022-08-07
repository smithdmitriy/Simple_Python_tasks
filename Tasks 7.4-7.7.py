"""
7.4. Создайте список things, содержащий три элемента: "mozzarella", "cinderella", "salmonella".
7.5. Напишите с большой буквы тот элемент списка things, который означает человека, а затем выведите список.
 Изменился ли элемент списка?
7.6. Переведите сырный элемент списка things в верхний регистр целиком и выведите список.
7.7. Удалите из списка things заболевание, получите Нобелевскую премию и затем выведите список на экран.
"""

things = ["mozzarella", "cinderella", "salmonella"]
index_of_human = things.index("cinderella")
things[index_of_human] = things[index_of_human].capitalize()
index_of_cheese = things.index("mozzarella")
things[index_of_cheese] = things[index_of_cheese].upper()
index_of_bacteria = things.index("salmonella")
del things[index_of_bacteria]
print(things)
