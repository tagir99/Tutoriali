
def sort_array(source_array):
    global i
    i = 0
    global spisok

    spisok = source_array

    while i < 50:
        for j in range(len(spisok)):
            for j2 in range(j, len(spisok)):
                if (spisok[j] % 2 != 0 and spisok[j2] % 2 != 0 and spisok[j] > spisok[j2]):
                    spisok[j], spisok[j2] = spisok[j2], spisok[j]
                    break

                i = i + 1

        i = i  + 1


    return (spisok)


print(sort_array([5, 3, 1, 8, 0]))

#промежуточный вариант
def sort_array(source_array):

    for j in range(len(source_array)):
        for j2 in range(j, len(source_array)):
            if (source_array[j] % 2 != 0 and source_array[j2] % 2 != 0 and source_array[j] > source_array[j2]):
                source_array[j], source_array[j2] = source_array[j2], source_array[j]
                break

    return (source_array)

print(sort_array([3, 1, 5, 8, 0]))