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





a = poiskovik([4,12,15,17,54,34,23,36,78,45,65,39,21,56])
print(a.UporMassiv)
print(f"{a.poisk(34)} ---index, {a.poisk(34)+1}--- Порядковый номер ")
