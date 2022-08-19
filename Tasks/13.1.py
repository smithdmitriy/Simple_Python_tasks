from datetime import date

task_text = """
13.1. Запишите текущие дату и время как строку в текстовый файл today.txt.
"""
now = date.today()
print(task_text)
print(now)
with open('today.txt', 'wt') as file:
    file.write(str(now))
