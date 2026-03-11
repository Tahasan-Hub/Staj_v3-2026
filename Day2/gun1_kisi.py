import time

class Kisi:
    def __init__(self,kisi_id,konum):
        self.kisi_id = kisi_id
        self.konum = konum
        self.uyku_baslangic = None
        self.hareketsizlik_baslangic = None
        self.toplam_ihlal = 0

    def konum_guncelle(self,yeni_konum):
        self.konum = yeni_konum

    def uyku_baslat(self):
        self.uyku_baslangic = time.time()

    def uyku_kontrol(self,esik):
        if self.uyku_baslangic != None:
            gecen_sure = time.time() - self.uyku_baslangic
            if gecen_sure > esik:
                return True
            else:
                return False

    def uyku_sifirla(self):
        self.uyku_baslangic = None

    def __str__(self):
        return f"Kişi: {self.kisi_id} | Konum: {self.konum} | İhlal: {self.toplam_ihlal}"     
if __name__ == "__main__":
    kisi1 = Kisi(1,(100,200))
    kisi2 = Kisi(2,(150,300))
    kisi3 = Kisi(3,(140,200))

    kisi1.konum_guncelle((120,210))
    kisi2.uyku_baslat()

    time.sleep(3)

    if kisi2.uyku_kontrol(2):
        kisi2.toplam_ihlal += 1
        print("İhlal Tespit Edildi!")
    kisi2.uyku_sifirla()
    print(kisi1)
    print(kisi2)
