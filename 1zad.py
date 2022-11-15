spisok_chisel = []
Proizvedenie = 1
kolvo_chisel= int(input())
for i in range(kolvo_chisel):
    chislo = float(input())
    spisok_chisel.append(chislo)
for j in range(kolvo_chisel):
    if spisok_chisel[j] >0:
        Proizvedenie *= spisok_chisel[j]

print(Proizvedenie)
