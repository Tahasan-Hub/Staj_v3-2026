class Ogrenci:
    def __init__(self,isim,numara):
        self.isim = isim
        self.numara = numara
        self.notlar = []

    def not_ekle(self,not_degeri):
        self.notlar.append(not_degeri)  

    def ortalama_hesapla(self):
        ort = sum(self.notlar) / len(self.notlar)
        return ort

    def durum(self):
        ortalama = self.ortalama_hesapla()

        if ortalama >= 50:
            print("Geçti.")
        else:
            print("Kaldı.")    

    def bilgi(self):
        print(f"Öğrenci: {self.isim} | No: {self.numara} | Notlar: {self.notlar} | Ortalama: {self.ortalama_hesapla():.2f}")        

ogrenci1 = Ogrenci("Taha",250)
ogrenci2 = Ogrenci("Elif",500)
ogrenci3 = Ogrenci("Buse",347)

ogrenci1.not_ekle(70)
ogrenci1.not_ekle(85)
ogrenci1.not_ekle(94)
ogrenci2.not_ekle(55)
ogrenci2.not_ekle(45)
ogrenci2.not_ekle(24)
ogrenci3.not_ekle(75)
ogrenci3.not_ekle(35)
ogrenci3.not_ekle(90)

ogrenci1.bilgi()
ogrenci2.bilgi()
ogrenci3.bilgi()

ogrenci1.durum()
ogrenci2.durum()
ogrenci3.durum()













