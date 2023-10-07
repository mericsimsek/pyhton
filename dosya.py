def nothesap(i):
    i=i[:-1]
    liste=i.split(":")
    ogrenciad=liste[0]
    ogrencinot=liste[1].split(",")

    onot1=int(ogrencinot[0])
    onot2=int(ogrencinot[1])
    onot3=int(ogrencinot[2])
    
    ortalama=(onot1+onot2+onot3)/3

    if ortalama>90 and ortalama <100:
        harf="AA"
    elif ortalama>70 and ortalama <90:
        harf="BB"
    elif ortalama >50 :
        harf="CC"
    else:
        harf="FF"
    return ogrenciad+":"+harf+"\n"


def notoku():
    with open("sinavnot.txt","r",encoding="utf-8") as dosyam:
        for i in dosyam:
            print(nothesap(i))


def notgir():
    ad=input("Öğrencinin adı:")
    soyad=input("Öğrencinin soyadı:")
    not1=input("Not1:")
    not2=input("Not2:")
    not3=input("Not3:")

    with open("sinavnot.txt","a",encoding="utf-8")as dosyam:
        dosyam.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")


def notkayit():
    with open("sinavnot.txt","r",encoding="utf-8") as dosyam:
        liste = []

        for x in dosyam:
            liste.append(nothesap(x))
        
    with open("sonuc.txt","w",encoding="utf-8") as dosyam2:
        for x in liste:
            dosyam2.write(x)

while True:
    islem=(input("1-Notları oku \n2-Notları gir \n3- Notları kayıt et\n4-Çıkış:"))

    if islem=="1":
        notoku()

    elif islem=="2":
        notgir()

    elif islem=="3":
        notkayit()
        
    else:
        break