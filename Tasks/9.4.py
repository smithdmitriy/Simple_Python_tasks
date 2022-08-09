"""
9.4. Определите исключение OopsException. Сгенерируйте его и посмотрите, что произойдет. Затем напишите код,
     позволяющий поймать это исключение и вывести строку 'Caught an oops'.
"""

class OopsException(Exception):
    pass

text = input("Your text (not only digit)\n")
try:
    if text.isdigit():
        raise OopsException(text)
except OopsException:
    print('Caught an oops')
