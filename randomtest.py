import random

tmp = 0
for i in range(0, 10000):
    ta = random.randint(1, 1000) % 100
    if ta < 75 and ta > 55:
        tmp += 1
print(tmp)
