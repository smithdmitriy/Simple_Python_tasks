"""
7.11. Попробуйте создать генератор рифм для прыжков через скакалку.
 Напечатайте последовательность двухстрочных рифм. Начните программу с этого фрагмента:
start1 = ["fee", "fie", "foe"]
rhymes = [
("flop", "get a mop"),
("fope", "turn the rope"),
("fa", "get your ma"),
("fudge", "call the judge"),
("fat", "pet the cat"),
("fog", "walk the dog"),
("fun", "say we're done"),
]
start2 = "Someone better"
Затем следуйте инструкциям.
Для каждого кортежа (first, second) в списке rhymes.
Для первой строки:
выведите на экран каждую строку списка start1: начните ее с большой буквы,
 а закончите восклицательным знаком с пробелом;
выведите на экран значение переменной first, также записав его с большой буквы и с восклицательным знаком на конце.
Для второй строки:
выведите на экран значение переменной start2 и пробел;
выведите на экран значение переменной second и точку
"""

start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

for rhyme_string in rhymes:
    for word in start1:
        print(word.capitalize(), end='! ')
    print(rhyme_string[0].capitalize(), end='! ')
    print(start2, end=' ')
    print(rhyme_string[1], ' ')
