from guardwatch.kisi import Kisi
import math

class Tracker:
    def __init__(self,max_mesafe = 50):
        self.max_mesafe = max_mesafe
        self.siradaki_id = 0
        self.kisiler = {}

    def kisi_getir(self,kisi_id):
        if kisi_id in self.kisiler:
            return self.kisiler[kisi_id]
        else:
            return None

    def aktif_kisiler(self):
        return self.kisiler

    def _kisi_ekle(self,konum):
        kisi = Kisi(self.siradaki_id,konum)
        self.kisiler[self.siradaki_id] = kisi
        self.siradaki_id += 1       

    def guncelle(self,yeni_konumlar):
        if len(yeni_konumlar) == 0:
            self.kisiler.clear()
            return self.kisiler
        if len(self.kisiler) == 0:
            for konum in yeni_konumlar:
                self._kisi_ekle(konum)    
        else:
            kullanilan_idler = []
            for yeni_konum in yeni_konumlar:
                eslesen_id = None
                en_kisa = self.max_mesafe
                for kisi_id,kisi in list(self.kisiler.items()):
                    if kisi_id in kullanilan_idler:
                        continue
                    mesafe = math.dist(kisi.konum , yeni_konum)
                    if mesafe < en_kisa:
                        en_kisa = mesafe
                        eslesen_id = kisi_id
                if eslesen_id != None:
                    self.kisiler[eslesen_id].konum_guncelle(yeni_konum)
                    kullanilan_idler.append(eslesen_id)
                if eslesen_id == None:
                    self._kisi_ekle(yeni_konum)                 
            for kisi_id in list(self.kisiler.keys()):
                if kisi_id not in kullanilan_idler:
                    del self.kisiler[kisi_id]
        return self.kisiler  

if __name__ == "__main__":
    takip = Tracker(max_mesafe=50)
    ilk_konum = [(10,10),(20,20),(30,30),(40,40),(50,50)]   
    sonuc = takip.guncelle(ilk_konum)
    for kisi_id , kisi in sonuc.items():
        print(f"ID: {kisi_id},konum: {kisi.konum}")  
    yeni_konum = [(15,12),(23,34),(32,27),(45,45)]
    sonuc2 = takip.guncelle(yeni_konum)
    for kisi_id , kisi in sonuc2.items():
        print(f"ID: {kisi_id},konum: {kisi.konum}")                     