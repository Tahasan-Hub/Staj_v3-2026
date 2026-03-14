import sqlite3
import random
import datetime

veri_tabani = sqlite3.connect("ihlaller.db")
imlec = veri_tabani.cursor()

imlec.execute(
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
veri_tabani.commit()

kisi_havuzu = ["kisi_1","kisi_2","kisi_3","kisi_4"]
ihlal_havuzu = ["uyku_hali","dikkat_daginikligi","telefon_kullanimi"]

sahte_veriler = []

for i in range(10):
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    kisi_id = random.choice(kisi_havuzu)
    ihlal_turu = random.choice(ihlal_havuzu)
    sure_sn = round(random.uniform(1.5,6.0),2)
    ear_degeri = round(random.uniform(0.15,0.30),2)
    frame_yolu = f"frames/kamera_{random.randint(1,5)}_{i}.jpg"
    sahte_veriler.append((zaman,kisi_id,ihlal_turu,sure_sn,ear_degeri,frame_yolu))

imlec.executemany(
    "INSERT INTO ihlaller (zaman,kisi_id,ihlal_turu,sure_sn,ear_degeri,frame_yolu) VALUES (?,?,?,?,?,?)",
    sahte_veriler
)
veri_tabani.commit()

print("10 adet sahte ihlal kaydı başarıyla eklendi.")


print("\n--- TÜM İHLALLER LİSTESİ ---")
imlec.execute("SELECT * FROM ihlaller")
tum_ihlaller = imlec.fetchall()
for ihlal in tum_ihlaller:
    print(ihlal)

print("\n--- KİŞİ BAZLI İHLAL SAYISI (GROUP BY) ---")
imlec.execute("SELECT kisi_id,COUNT(*) FROM ihlaller GROUP BY kisi_id")
kisi_ihlalleri = imlec.fetchall()    

for kisi in kisi_ihlalleri:
    print(f"{kisi[0]} adlı kişinin toplam ihlali: {kisi[1]}")

print("\n--- EN UZUN SÜREN İHLAL (ORDER BY DESC ve LIMIT 1) ---")
imlec.execute("SELECT * FROM ihlaller ORDER BY sure_sn DESC LIMIT 1")

en_uzun_ihlal = imlec.fetchone()
print(f"En Uzun İhlal Kaydı: {en_uzun_ihlal}")

print("\n--- SON 5 İHLAL (ORDER BY DESC ve LIMIT 5) ---")
imlec.execute("SELECT * FROM ihlaller ORDER BY id DESC LIMIT 5")
son_ihlaller = imlec.fetchall()
for ihlal in son_ihlaller:
    print(ihlal)

print("\n--- BELİRLİ BİR KİŞİNİN İHLALLERİ (WHERE) ---")
aranan_kisi = "kisi_1"
imlec.execute("SELECT * FROM ihlaller WHERE kisi_id = ?",(aranan_kisi,))

kisi_listesi = imlec.fetchall()

print(f"{aranan_kisi} adlı kişinin kayıtları:")
for ihlal in kisi_listesi:
    print(ihlal)

veri_tabani.close()