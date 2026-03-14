def ortalama_hesapla(notlar):
    if len(notlar) == 0:
        return 0
    
    toplam = 0
    for not_degeri in notlar:
        toplam += int(not_degeri)
    return toplam / len(notlar)

def basarili_ogrenciler(ogrenciler):
    basarililer = []
    for ogr in ogrenciler:
        ort = ortalama_hesapla(ogr["notlar"])
        if ort >= 70:
            basarililer.append(ogr)
    return basarililer

veriler = [
    {"isim":"Taha", "notlar": [80, 90, 70]},
    {"isim":"Ali", "notlar": []},
    {"isim":"Ayse", "notlar": [60, "85", 75]},
]       

sonuc = basarili_ogrenciler(veriler)
for s in sonuc:
    print(f"{s['isim']}: Basarili")