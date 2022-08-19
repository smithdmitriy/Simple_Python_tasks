from datetime import datetime


task_text = """
13.1. Запишите текущие дату и время как строку в текстовый файл today.txt.
"""
now = datetime.today
print(str(now()))
with open('today.txt', 'wt') as file:
     file.write(str(now()))
