"""
8.1. Создайте англо-французский словарь с названием e2f и выведите его на экран. Вот ваши первые слова: dog/chien,
    cat/chat и walrus/morse.
8.2. Используя словарь e2f, выведите французский вариант слова walrus.
8.3. Создайте французско-английский словарь f2e на основе словаря e2f. Используйте метод items.
8.4. Используя словарь f2e, выведите английский вариант слова chien.
8.5. Выведите на экран множество английских слов из ключей словаря e2f.
"""
from typing import Dict

# 8.1
e2f: dict[str, str] = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

e2f: dict[str, str] = dict(dog='chien', cat='chat', walrus='morse')

# 8.2
print(f"\n8.2. Используя словарь e2f, выведите французский вариант слова walrus.\n{e2f['walrus']}")
#print(e2f.get('walrus'))

# 8.3
f2e = {key:val for (val, key) in e2f.items()}

# 8.4
print(f"\n8.4. Используя словарь f2e, выведите английский вариант слова chien.\n{f2e['chien']}")
#print(f2e.get('chien'))

# 8.5
print(f"\n8.5. Выведите на экран множество английских слов из ключей словаря e2f.\n{list(e2f.keys())}")

