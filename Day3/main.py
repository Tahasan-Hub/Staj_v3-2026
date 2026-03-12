from guardwatch import Tracker,CSVLogger,Kisi,AlarmSistemi
import guardwatch
import math
import random
import time
"""
takip_sistemi = Tracker(max_mesafe=50)
kayit_sistemi = CSVLogger("ihlaller.csv")

alarm_sistemi = AlarmSistemi("beep.wav")

koordinatlar = [(100,100),(140,80)]
aktif_kisiler = takip_sistemi.guncelle(koordinatlar)
print("Takip edilen kişiler:",aktif_kisiler)

kisi_a = aktif_kisiler[0] #ID'si 0 olan ilk kişi
kisi_b = aktif_kisiler[1] #ID'si 1 olan ikinci kişi

mesafe = math.dist(kisi_a.konum,kisi_b.konum)
print(f"Kişiler arasındaki anlık mesafe: {mesafe:.2f}")

if mesafe < 50:
    print("Dikkat: Mesafe ihlali tespit edildi.")
    alarm_sistemi.cal()
    kayit_sistemi.ihlal_kaydet(f"İhlal: ID {kisi_a.kisi_id} ve ID {kisi_b.kisi_id} çok yakın. Mesafe: {mesafe}")
else:
    print("Mesafe güvenli,sorun yok.")    

print("GuardWatch Sürümü:",guardwatch.__version__)
"""

def simulasyon_baslat():
    takip_sistemi = Tracker(max_mesafe=50)
    kayit_sistemi = CSVLogger("ihlaller.csv")
    alarm_sistemi = AlarmSistemi("beep.wav")

    for tur in range(1,11):
        print(f"\n----- TUR {tur} BAŞLIYOR -------")
        koordinatlar = [(random.randint(0,100),random.randint(0,100)) for i in range(5)]
        aktif_kisiler = takip_sistemi.guncelle(koordinatlar)
        id_listesi = list(aktif_kisiler.keys())
        for i in range(len(id_listesi)):
            for j in range(i + 1,len(id_listesi)):
                k1 = aktif_kisiler[id_listesi[i]]
                k2 = aktif_kisiler[id_listesi[j]]
                mesafe = math.dist(k1.konum,k2.konum)
                if mesafe < 30:
                    print(f"Ihlal ID {k1.kisi_id} ve ID {k2.kisi_id} yakın: {mesafe:.2f}")
                    k1.toplam_ihlal += 1
                    k2.toplam_ihlal += 1
                    alarm_sistemi.cal()
                    kayit_sistemi.ihlal_kaydet(f"Tur {tur}: ID {k1.kisi_id} ve {k2.kisi_id} ihlali")
        time.sleep(2)
    alarm_sistemi.durdur()
    for k_id,kisi_nesnesi in aktif_kisiler.items():
        print(kisi_nesnesi)

if __name__ == "__main__":
    simulasyon_baslat()

        

