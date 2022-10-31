perv = input()
vtor = input()
kolvo = 0
dlina = len(perv)
counter = 0


for i in vtor:
    if i == perv[counter]:
        counter += 1

    else:
        counter = 0

    if counter == dlina:
        kolvo += 1
        counter = 0

print(kolvo)
