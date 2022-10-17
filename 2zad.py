kolvo_zaprosov = int(input("Введите количество запросов "))
old_imena = []
new_imena = []


n = kolvo_zaprosov
for  i in range(kolvo_zaprosov):
    nik = input("Введите текущий никнейм")
    newnik = input("Введите new ник")

    if nik not in new_imena:
        old_imena.append(nik)
        new_imena.append(newnik)
    else:
        for i in range(len(new_imena)):
            if new_imena[i] == nik:
                new_imena[i] = newnik
        n -= 1
print(n)


for i in range(len(old_imena)):
    print(old_imena[i],new_imena[i],end="  ")
    print("")
