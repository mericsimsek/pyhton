class cocuk:
    def __init__(self,ad,soyad,yas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        print("{} {} {} bilgili cocuktur".format(self.ad,self.soyad,self.yas))

class adam(cocuk):
    def __init__(self, ad, soyad, yas,isi):
        super().__init__(ad, soyad, yas)
        self.isi=isi

    def cagir(self):
        print("{} {} {} bilgili bir {} adamdır.".format(self.isim, self.soyisim, self.yas, self.isi))


p2=adam("Meriç","Şimşek",29,"Müdür")
