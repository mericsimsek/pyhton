class soru:
    def __init__(self,sayi,sayi2,sayi3):
        self.a=sayi
        self.b=sayi2
        self.__c=sayi3

    def getir(self):
        self.__c

    def listele(self):
        self.__c +=15

a1=soru(12,45,87)
print(a1.listele)
