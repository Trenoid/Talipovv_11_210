from random import randint
t = int(input(" Введите t "))
s = int(input(" Введите s "))
a = []
j = ""
for m in range(t):
    for n in range(s):
        j = j + str(randint(0,1))
    a.append(j)
    j = ""
print(a)
k = 0
l = ""
mas = []
udal = []
gt = "False"
for m in range(t):
    l = a[m]
    mas.append(a[m])
    dlina = len(l)
    for ch in range(dlina-1):
        if l[ch] == "1":
            for m in range(ch,dlina-1):
                if l[m] == "0":
                    for i in range(m,dlina):
                        if l[i] == "1":
                            gt = "true"
                    if gt == "true":
                        k +=1
                    gt = "False"
            break


    print(k)
    k = 0
    l = ""
    mas.clear()
