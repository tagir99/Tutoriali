stroka = input('vvod')
dlina = len(stroka)
integ = []
i = 0
while i < dlina:
    s_int = ''
    a = stroka[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < dlina:
            a = stroka[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))

print(integ)