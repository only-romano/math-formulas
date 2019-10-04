def corellation(data):
    sums = {"x": 0, "y": 0, "x2": 0, "y2": 0, "xy": 0}
    length = len(data)
    for value in data:
        x = value[0]
        y = value[1]
        sums["x"] += x
        sums["y"] += y
        sums["x2"] += x*x
        sums["y2"] += y*y
        sums["xy"] += x*y

    devident = length * sums["xy"] - sums["x"] * sums["y"]
    devider1 = (length * sums["x2"] - sums["x"] ** 2) ** 0.5
    devider2 = (length * sums["y2"] - sums["y"] ** 2) ** 0.5

    return devident / (devider1 * devider2)


data = [[77, 85], [45, 58], [64, 83], [59, 71], [79, 87], [87, 88], [94, 113], [52, 62], [65, 71], [87, 101]]

print(corellation(data))

"""
from random import randint

print("Новая игра - угадай число 2019!")

guess = 0
count = 0
number = randint(1, 100)
win = False

while count < 5:
    try:
        guess = int(input("Ваша догадка? "))
    except Exception:
        guess = 0
    if guess == number:
        print("ВЫ победили!")
        win = True
        break

    if guess < number:
        print("Ваша догадка меньше моего числа!")
    else:
        print("Ваша догадка больше моего числа!")

if not win:
    print("Жаль, но вы проиграли.. Загаданное число - " + str(number) + ".")
"""
