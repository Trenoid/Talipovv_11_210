class poiskovik:

    def __init__(self,massiv):
        self.massiv = massiv
        self.UporMassiv = sorted(self.massiv)
        self.ForPoiskUporMassiv = self.UporMassiv

    def poisk(self,number):
        self.dlina = len(self.ForPoiskUporMassiv)
        self.middle = self.dlina // 2
        self.averageNumber = self.ForPoiskUporMassiv[self.middle]

        if self.averageNumber != number:
            if self.averageNumber > number:
                self.ForPoiskUporMassiv = self.ForPoiskUporMassiv[0:self.middle]
                self.poisk(number)

            if self.averageNumber < number:
                self.ForPoiskUporMassiv = self.ForPoiskUporMassiv[self.middle:]
                self.poisk(number)

        if self.averageNumber == number:
            return self.UporMassiv.index(number)





a = poiskovik([4,12,15,17,54,34,23,36,78,45,65,39,45]) 
print(a.UporMassiv)
number = 34   #### какое число найти
print(f"{a.poisk(number)} ---index, {a.poisk(number)+1}--- Порядковый номер ")
