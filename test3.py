import random

def quest(min, max, n):
    for i in range(n):
        yield random.randint(min, max)

for c in quest(1, 50, 1):
    print(c)
    vp = c

popitki = 0
while popitki < 6:

    popitki +=1
    a = input('vvedite kakoi bydet vp')
    a = int(a)
    if a < vp:
        print('print integer more')
    elif a > vp:
        print('print integer small')
    elif a == vp:
        print('good, it is required integer')
