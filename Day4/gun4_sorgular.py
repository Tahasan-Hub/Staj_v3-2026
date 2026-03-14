import sqlite3

veri_tabani = sqlite3.connect("ogrenciler.db")
imlec = veri_tabani.cursor()

imlec.execute("SELECT COUNT (*) FROM ogrenciler")
toplam_sayi = imlec.fetchone()[0] # Sadece içindeki sayıyı almak için kodun sonuna [0] ekledik

print(f"Toplam Öğrenci Sayısı: {toplam_sayi}")

imlec.execute("SELECT MAX(ortalama) FROM ogrenciler")

#Tek bir sonuç döneceği için yine fetchone() kullanacağız
# Tek bir sonuçtan kastımız en büyük sayı
en_yuksek_not = imlec.fetchone()[0]
print(f"En Yüksek Not: {en_yuksek_not}")

imlec.execute("SELECT AVG(ortalama) FROM ogrenciler")

genel_ortalama = round(imlec.fetchone()[0],2)
print(f"Sınıfın Genel Ortalaması: {genel_ortalama}")


print("\n--- İSME GÖRE SIRALI LİSTE (ORDER BY) ---")
imlec.execute("SELECT * FROM ogrenciler ORDER BY isim")

sirali_ogrenciler = imlec.fetchall()
for ogrenci in sirali_ogrenciler:
    print(ogrenci)

print("\n--- ORTALAMASI 50 İLE 80 ARASI OLANLAR (BETWEEN) ---")
imlec.execute("SELECT * FROM ogrenciler WHERE ortalama BETWEEN 50 AND 80")
aralik_ogrenciler = imlec.fetchall()
for ogrenci in aralik_ogrenciler:
    print(ogrenci)    



# LIKE 'A%': A ile başlasın, gerisi ne olursa olsun.
# Eger '%A' yazsaydık: Sonu A ile bitenler olurdu.
# Eger '%A%' yazsaydık: İçinde A harfi geçenler olurdu.
print("\n--- İSMİ 'A' İLE BAŞLAYANLAR (LIKE) ---")
imlec.execute("SELECT * FROM ogrenciler WHERE isim LIKE 'A%'")

a_ile_baslayanlar = imlec.fetchall()
for ogrenci in a_ile_baslayanlar:
    print(ogrenci)

veri_tabani.close()