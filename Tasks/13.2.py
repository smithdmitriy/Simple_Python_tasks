import datetime


task_text = """
13.2. Прочтите текстовый файл today.txt и разместите данные в строке today_string.
"""
with open('today.txt', 'rt') as file:
    today = file.readline()
print(task_text)
print(today)

fmt = '%Y-%m-%d'
print(datetime.datetime.strptime(today, fmt))