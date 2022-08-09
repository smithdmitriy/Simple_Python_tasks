"""
7.8. Создайте список с элементами "Groucho", "Chico" и "Harpo"; назовите его surprise.
7.9. Напишите последний элемент списка surprise со строчной буквы,
 затем выведите эту строку в обратном порядке и с прописной буквы.
"""

surprise = ["Groucho", "Chico", "Harpo"]
print(surprise[-1].lower())
print(surprise[-1].lower()[::-1].capitalize())
