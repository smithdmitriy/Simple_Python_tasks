import re


mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze, 
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees, 
Or as the leaves upon the trees,
It did require to make thee please, 
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris 
Intends to send you off as far as 
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze 
And bite your cheek, then songs or glees 
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""
print("""
12.5. Импортируйте модуль re, чтобы использовать функции регулярных выражений в Python.
      Примените функцию re.findall() для вывода на экран всех слов, которые начинаются с буквы с.
      """)
print(re.findall(r"\b[cC]\w*", mammoth))

print("""
12.6. Найдите все четырехбуквенные слова, которые начинаются с буквы c.
      """)
print(re.findall(r"\b[cC]\w{3}", mammoth))

print("""
12.7. Найдите все слова, которые заканчиваются на букву r.
      """)
print(re.findall(r"\w*r\b", mammoth))

print("""
12.8. Найдите все слова, которые содержат три гласные подряд.
      """)
print(re.findall(r"\w[aeiouyAEIOUY]{3}\w*", mammoth))
