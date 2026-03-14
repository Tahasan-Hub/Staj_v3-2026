import csv
from gun4_db_logger import DBLogger

logger = DBLogger("guardwatch_goc.db")

sayac = 0

with open("ihlaller.csv","r",encoding="utf-8") as dosya:
    oku = csv.DictReader(dosya,skipinitialspace=True)
    oku.fieldnames = [baslik.strip() for baslik in oku.fieldnames]

    for satir in oku:
        logger.ihlal_kaydet(
            kisi_id=satir["kisi_id"],
            ihlal_turu=satir['ihlal_turu'],
            sure=float(satir['sure_sn']),
            ear=float(satir['ear_degeri']),
            frame_yolu=satir.get("frame_yolu","")
        )
        sayac += 1
print(f"\n{sayac} kayıt CSV'den SQLite'a aktarıldı.")   

print("\n--- VERİTABANINDAN DOĞRULAMA ---")
tum_kayitlar = logger.ihlalleri_getir()

print("Aktarılan ilk 5 kayıt:")
for kayit in tum_kayitlar[5]:
    print(kayit)
logger.kapat()    