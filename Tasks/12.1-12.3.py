task_text = r""" 
12.1. Создайте строку Unicode с именем mystery и присвойте ей значение '\U0001f4a9'. 
      Выведите на экран значение строки mystery. Выведите на экран значение переменной mystery и ее имя Unicode.
"""

import unicodedata

mystery = '\U0001f4a9'

print(task_text)
print(f"{mystery} {unicodedata.name(mystery)}")
task_text = r""" 
12.2. Закодируйте строку mystery, на этот раз с использованием кодировки UTF-8,
      в переменную типа bytes с именем pop_bytes. Выведите на экран значение переменной pop_bytes.
"""
pop_bytes = mystery.encode("utf-8")
print(task_text)
print(pop_bytes)

task_text = r""" 
12.3. Используя кодировку UTF-8, декодируйте переменную popbytes в строку pop_string.
      Выведите на экран значение переменной pop_string. Равно ли оно значению переменной mystery?
"""
pop_string = pop_bytes.decode("utf-8")
print(task_text)
print(pop_string)
print(mystery==pop_string)