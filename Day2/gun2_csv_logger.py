import csv
import os

class CSVLogger():
    def __init__(self,dosya_adi):
        self.dosya_adi = dosya_adi
        if not os.path.exists(self.dosya_adi):
            with open(self.dosya_adi,"w",newline="") as dosya:
                yaz = csv.writer(dosya)
                yaz.writerow(["Kisi_Id","Ihlal_Turu","Sure","EAR"])
    
    def ihlal_kaydet(self,kisi_id,ihlal_turu,sure,ear):
        with open(self.dosya_adi,"a",newline="") as f:
            f = csv.writer(f)
            f.writerow([kisi_id,ihlal_turu,sure,ear])

    def ozet_getir(self):
        toplam_ihlal = 0
        kisi_ozet = {}
        with open(self.dosya_adi,"r") as r:
            oku = csv.reader(r)
            next(oku)
            for satir in oku:
                toplam_ihlal += 1
                kisi_id  = satir[0]
                if kisi_id in kisi_ozet:
                    kisi_ozet[kisi_id] += 1
                else:
                    kisi_ozet[kisi_id] = 1
        print("Toplam İhlal:",toplam_ihlal)
        print("Kişi Bazlı Özet:",kisi_ozet)

    def temizle(self):
        with open(self.dosya_adi,"w",newline="") as dosya:
            yaz = csv.writer(dosya)
            yaz.writerow(["Kisi_Id","Ihlal_Turu","Sure","EAR"])
        print("Log dosyası başarıyla temizlendi.")                        

logger = CSVLogger("ihlal_test.csv")
logger.ihlal_kaydet("1","Goz_Kapali",2.5,0.22)
logger.ihlal_kaydet("2","Hareketsizlik",8.7,0.35)
logger.ihlal_kaydet("3","Hareketsizlik",4.8,0.18)
logger.ihlal_kaydet("3","Goz_Kapali",8.7,0.14)
logger.ihlal_kaydet("1","Hareketsizlik",3.4,0.19)
logger.ihlal_kaydet("3","Goz_Kapali",2.4,0.13)

logger.ozet_getir()

logger.temizle()
