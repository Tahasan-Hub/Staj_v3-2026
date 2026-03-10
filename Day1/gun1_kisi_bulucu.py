import random
import time

class Kisi:
    def __init__(self,kisi_id,konum):
        self.id = kisi_id
        self.konum = konum
        self.uyku_baslangic = None
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
        return f"Kişi: {self.id} | Konum: {self.konum} | İhlal: {self.toplam_ihlal}"

kisiler = []
for i in range(1,6):
    x = random.randint(0,100)
    y = random.randint(0,100)
    yeni_kisi = Kisi(i,(x,y))
    kisiler.append(yeni_kisi)

for tur in range(1,11):
    print(f"\n---- TUR {tur} ----")

    for kisi in kisiler:
        x = random.randint(0,100)
        y = random.randint(0,100)
        kisi.konum_guncelle((x,y))
        uyuyor_mu = random.choice([True,False])
        if uyuyor_mu == True:
            kisi.uyku_baslat()
            if kisi.uyku_kontrol(0):
                kisi.toplam_ihlal += 1
                kisi.uyku_sifirla()
        print(kisi)
    time.sleep(1)            
    