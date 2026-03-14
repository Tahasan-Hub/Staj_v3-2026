import sqlite3


ogrenci_listesi = [
    ("Ali", "100", 80),
    ("Mehmet", "101", 85),
    ("Ayşe", "102", 90),
    ("Zeynep", "103", 45),
    ("Ahmet", "200", 75)
]

veri_tabani = sqlite3.connect("ogrenciler.db")

imlec = veri_tabani.cursor()

imlec.execute(
    """
    CREATE TABLE IF NOT EXISTS ogrenciler(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT NOT NULL,
        numara TEXT UNIQUE,
        ortalama REAL
    )    """
)

veri_tabani.commit()

imlec.executemany("INSERT INTO ogrenciler(isim,numara,ortalama) VALUES(?,?,?)",ogrenci_listesi)
veri_tabani.commit()

imlec.execute("SELECT * FROM ogrenciler")
tum_ogrenciler = imlec.fetchall()

for ogrenci in tum_ogrenciler:
    print(ogrenci)

print("\n--- ORTALAMASI 70'ten BÜYÜK OLANLAR ---")
imlec.execute("SELECT * FROM ogrenciler WHERE ortalama > ?",(70,))
basarili_ogrenciler = imlec.fetchall()

for ogrenci in basarili_ogrenciler:
    print(ogrenci)

imlec.execute("UPDATE ogrenciler SET ortalama = ? WHERE isim = ?",(100,'Ali'))
veri_tabani.commit()
print("Güncelleme başarılı.")

imlec.execute("DELETE FROM ogrenciler WHERE isim = ?",('Zeynep',))
veri_tabani.commit()
print("Silme başarılı.")

veri_tabani.close()

