dosya_adi = "veriler.txt"

# with open(dosya_adi,"w",encoding="utf-8") as dosya:
#     dosya.write("Şükrü Öztürk, İğdır, Çağrı")

# with open(dosya_adi,"r",encoding="utf-8") as f:
#     metin = f.read()
#     print(metin)

# with open(dosya_adi,"w",encoding="utf-8") as dosya:
#     dosya.write("Şükrü Öztürk, İğdır, Çağrı")

# with open(dosya_adi,"r",encoding="latin-1") as f:
#     metin = f.read()
#     print(metin)


kütüphaneler = [
    "opencv-python",
    "ultralytics",
    "mediapipe",
    "flask",
    "matplotlib",
    "requests"
]

with open("requirements.txt","w",encoding="utf-8") as f:
    for paket in kütüphaneler:
        f.write(paket + "\n")