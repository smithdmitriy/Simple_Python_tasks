"""
7.1. Создайте список years_list, содержащий год, в который вы родились,
 и каждый последующий год вплоть до вашего пятого дня рождения.
 Например, если вы родились в 1980 году, список будет выглядеть так: years_list = [1980, 1981, 1982, 1983, 1984, 1985].
Если вам меньше пяти лет, но вы уже читаете эту книгу, то я даже не знаю, что сказать.
7.2. В какой год из списка years_list был ваш третий день рождения? Учтите, в первый год вам было 0 лет.
7.3. В какой год из списка years_list вам было больше всего лет?
"""
bithday_year = 1989
long_of_life = 85
years_list = [year for year in range(bithday_year, bithday_year + 6)]
print(f'3-year bithday in {years_list[3]}')
print(f'The oldest in {years_list[-1]}')