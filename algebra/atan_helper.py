from math import atan2, pi

# y, x
y = 0
x = 0

flag = False

for i in range(11):
    if i % 2 == 0:
        if flag:
            x += i
        else:
            x -= i
        flag = not flag
    else:
        if flag:
            y += i
        else:
            y -= i
    if x > 0 and y < 0:
        at = 630 - (90 - atan2(x, y) * 180 / pi)
        print(x, y, at)
    else:
        print(x, y, 270 - (90 - atan2(x, y) * 180 / pi))
