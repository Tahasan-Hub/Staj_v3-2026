class BankaHesabi:
    def __init__(self,isim,bakiye):
        self.isim = isim
        self.bakiye = bakiye

    def para_yatir(self,miktar):
        self.bakiye += miktar
        print(miktar,"Tl yatırıldı.")

    def para_cek(self,miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print(miktar,"Tl çekildi.")
        else:
            print("Yetersiz Bakiye")

    def bakiye_goster(self):
        print(f"İsim: {self.isim} | Bakiye: {self.bakiye}")     

musteri1 = BankaHesabi("Taha",200)
musteri2 = BankaHesabi("Elif",400)

musteri1.para_yatir(100)
musteri2.para_cek(100)        
musteri2.bakiye_goster()