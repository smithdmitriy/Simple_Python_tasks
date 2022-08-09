"""
9.3. Определите декоратор test, который выводит строку 'start' при вызове функции и строку 'end',
     когда функция завершает свою работу.
"""


def test(func):

    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return new_function


@test
def sum_print(a, b):
    print(a + b)
    return


sum_print(3.23364553456456, 5.5645657567566)
