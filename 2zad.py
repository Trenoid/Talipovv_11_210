from random import randint
n=int(input("Введите n:  "))
m=int(input("Введите m:  "))
print("У вас есть 4 хода")
print("")
pole=[]
kartoshek=0
  
pole=[[randint(-1,10) for g in range(n)] for i in range(m)]
for i in range(1,4+1):
	x = int(input("Введите x:  "))
	y = int(input("Введите y:  "))
	kartoshek+=pole[x-1][y-1]
	print("у вас осталось",4-i,"ходов")
print("Вам удалось собрать",kartoshek,"картошек")
if kartoshek>=20:
	print("Победа")
else:
	print("Поражение")

for l in range(n):
	for o in range(m):
		print(pole[l][o],end="  ")
	print("")