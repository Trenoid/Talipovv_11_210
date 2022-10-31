man = ["ов", "ев", "ин", "ын", "ский", "цкий"]
woman = ["ова", "ева", "ина", "ына", "ская", "цкая"]
spisok = input()
delimetr = " "
a = []
a.append(spisok)
a = delimetr.join(a)
a = a.split(delimetr)
kolvo_man = 0
kolvo_woman = 0
dlina = 0
okonch = ""
const = 4
neconst = 0
vrem = 0

for i in a:
    dlina = len(i)
    for j in range(dlina-1,0-1,-1):
        if neconst != 4:
            okonch += i[j]
            neconst += 1
    okonch = okonch[::-1]


    for m in range(len(woman)):
        perv = woman[m]
        vtor = okonch
        dlina = len(perv)
        counter = 0

        for i in vtor:
            if i == perv[counter]:
                counter += 1

            else:
                counter = 0

            if counter == dlina:
                kolvo_woman +=1
                counter = 0
                vrem= 1
    if vrem == 0:
        for n in range(len(man)):
            perv = man[n]
            vtor = okonch
            kolvo = 0
            dlina = len(perv)
            counter = 0

            for i in vtor:
                if i == perv[counter]:
                    counter += 1

                else:
                    counter = 0

                if counter == dlina:
                    kolvo_man += 1
                    counter = 0
    vrem = 0





    neconst = 0
    okonch = ""

print(kolvo_woman)
print(kolvo_man)
