import random

print('task 4.1')
secret = random.randint(1, 10)
guess = random.randint(1, 10)
print(f'{secret = } {guess = }')
if guess == secret:
    print('just right')
elif guess < 7:
    print('too low')
elif guess > 7:
    print('too high')
else:
    print(f'{guess = }')

print()

print('task 4.2')
small = bool(random.randint(0, 1))
green = bool(random.randint(0, 1))
print(f'{small = } {green = }')
if small and green:
    print('peas')
elif not small and not green:
    print('watermelon')
elif small and not green:
    print('cherry')
elif not small and green:
    print('pumpkin')
