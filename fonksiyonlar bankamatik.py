
hesapa={
    "ad":"Meriç",
    "soyad":"Şimşek",
    "ekhesap":1089780,
    "bakiye":100000000
}
hesapb={
    "ad":"Alex",
    "soyad":"Dani",
    "ekhesap":200,
    "bakiye":150
}

def hesapcek(hesap,miktar):
    print(f"Hoşgeldin {hesap['ad']}")

    if hesap['bakiye']>=miktar:
        print("parani aldin hesapta kalan bakiye:")
        hesap['bakiye']-=miktar 
    else: 
        toplam=hesap['ekhesap']+hesap['bakiye']
        if toplam>miktar:  
           ekhesapkul=input("ekhesap kullanilsin mi (e,h)?:")

           if ekhesapkul =="e":
                ekkullanilcakmiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0 
                hesap['ekhesap']-=ekkullanilcakmiktar 
           else:
               print("teşekkürler")
        else:
            print("bakiye yetersiz")     

def hesapsorgu(hesap):
        print(f"{hesap['soyad']} soyadli hesapta {hesap['bakiye']} tl bulunmakta.Ek hesapta {hesap['ekhesap']} bulunmakta.")


hesapcek(hesapb,300)
hesapsorgu(hesapb)