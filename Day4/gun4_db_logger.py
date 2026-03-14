import sqlite3
import random
import datetime

class DBLogger:
    def __init__(self,db_dosyasi):
        self.veri_tabani = sqlite3.connect(db_dosyasi)
        self.imlec = self.veri_tabani.cursor()

        self.imlec.execute(
            """
            CREATE TABLE IF NOT EXISTS ihlaller(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                zaman TEXT NOT NULL,
                kisi_id TEXT NOT NULL,
                ihlal_turu TEXT NOT NULL,
                sure_sn REAL,
                ear_degeri REAL,
                frame_yolu TEXT
            )
            """
        )
        self.veri_tabani.commit()

    def ihlal_kaydet(self,kisi_id,ihlal_turu,sure,ear,frame_yolu=""):
        zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.imlec.execute(
            "INSERT INTO ihlaller (zaman,kisi_id,ihlal_turu,sure_sn,ear_degeri,frame_yolu) VALUES (?,?,?,?,?,?)",
            (zaman,kisi_id,ihlal_turu,sure,ear,frame_yolu)
        )
        self.veri_tabani.commit()

    def ihlalleri_getir(self,kisi_id = None):
        if kisi_id is None:
            self.imlec.execute("SELECT * FROM ihlaller")
        else:
            self.imlec.execute("SELECT * FROM ihlaller WHERE kisi_id = ?",(kisi_id))
        return self.imlec.fetchall()
    
    def ozet(self):
        print("\n--- İHLAL ÖZETİ ---")

        self.imlec.execute("SELECT kisi_id,COUNT(*) FROM ihlaller GROUP BY kisi_id")
        kisi_özeti = self.imlec.fetchall()

        for kisi in kisi_özeti:
            print(f"Kişi: {kisi[0]} | Toplam İhlal: {kisi[1]}")
        self.imlec.execute("SELECT * FROM ihlaller ORDER BY sure_sn DESC LIMIT 1")
        en_uzun = self.imlec.fetchone()

        if en_uzun:        
            print(f"En Uzun İhlal: {en_uzun[4]} saniye (Kişi: {en_uzun[2]})")

    def kapat(self):
        self.veri_tabani.close()
        print("Veritabanı bağlantısı güvenle kapatıldı.")   

print("\n--- TEST BAŞLIYOR ---")

logger = DBLogger("guardwatch_lod.db")

for i in range(10):
    kisi = f"kisi_{random.randint(1,3)}"
    ihlal = random.choice(["uyku","telefon","dikkat_daginikligi"])
    sure = round(random.uniform(1.0,5.0),2)
    ear = round(random.uniform(0.15,0.25),2)

    logger.ihlal_kaydet(kisi,ihlal,sure,ear,f"frame_{i}.jpg")
print("10 test verisi başarıyla eklendi.")
logger.ozet()
logger.kapat()    