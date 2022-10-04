from random import randint
chislo=0
spisok=[]
counter = 0
allcounter = 0
while chislo !="q":
	chislo=input("Введите число:  ")
	if chislo== "q":
		break
	randomchislo=randint(1,9)
	
	if (int(chislo) >0) and (int(chislo) <10):
		if int(chislo)==randomchislo:
			print("Угадано загаданное число -",randomchislo)
			counter +=1
		else:
			print("Не угадано загаданое число -",randomchislo)
		spisok.append(randomchislo)
		print("Список загаданных чисел -"," ".join(map(str,spisok)))
		allcounter+=1
		ugadano=int(100*counter/allcounter)
		neugadano=int(100*(allcounter-counter)/allcounter)
		print("Статистика угадано/не угадано:",ugadano,"%",neugadano,"%")
		print("")
		print("")
	
	else:
		print("Введите число от 1 до 9")