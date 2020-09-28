def solve(a,b):
    global how_many_zn
    how_many_zn = 0

    lst = [a+1]
    for i in range(a+2, b + 1, 2):
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

    print(lst)


    for n in lst:

        for i in range(0, 10):

            n = str(n)
            if len(n) < 2:
                n = int(n[0]) ** 2
                n = str(n)

            elif len(n) == 2:
                n = int(n[0]) ** 2 + int(n[1]) ** 2
                n = str(n)

            elif len(n) == 3:

                n = int(n[0])** 2 + int(n[1])** 2 + int(n[2])**2
                n = str(n)

            elif len(n) == 4:
                n = int(n[0])** 2 + int(n[1])** 2 + int(n[2])**2 + int(n[3])**2

            if n == '1':
                how_many_zn = how_many_zn + 1
                break
            if i == 10:
                break

    return how_many_zn

print(solve(100,1000))