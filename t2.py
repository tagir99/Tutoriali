def solve(a,b):
    global how_many_one
    how_many_one = 0

    lst = [2]
    for i in range(3, b + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)


    for n in lst:

        for i in range(0, 10):

            n = str(n)
            if len(n) < 2:
                n = int(n[0]) ** 2
                n = str(n)

            if len(n) == 3:
                n = n + str(0)
                n = int(n[0]) ** 2 + int(n[1]) ** 2 + int(n[2])
                n = str(n)

            if len(n) == 2:
                n = int(n[0]) ** 2 + int(n[1]) ** 2
                n = str(n)

            if n == '1':
                how_many_one = how_many_one + 1
                break
            if i == 10:
                break

    return how_many_one

print(solve(1,100))