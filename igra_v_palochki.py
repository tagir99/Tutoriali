a = 20

while a > 0:

    st1 = input('step for 1 p;ayer')
    st1 = int(st1)
    if st1 <= 3 :
        a = a - st1

    if a == 0:
        print('player1 win')
    elif a != 0:
        print('otalos' + str(a))

    st2 = input('step for 2 p;ayer')
    st2 = int(st2)
    if st2 <= 3:
        a = a - st2

    if a == 0:
        print('p;ayer 2 win')
    elif a != 0:
        print('ostalos' + str(a))