from matematik import topla,cikar,carp

sayi1 = int(input("Lütfen birinci sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
islem = input("Lütfen Toplama için + , Çıkarma için - , Çarpma için * birini giriniz? ")
if islem == "+":
    print("Toplam Sonucu:",topla(sayi1,sayi2))
elif islem == "-":
    print("Çıkarma Sonucu:",cikar(sayi1,sayi2))
elif islem == "*":
    print("Çarpma Sonucu:",carp(sayi1,sayi2))   
else:
    print("Yanlış komut girdiniz.")     