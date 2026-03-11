class Arac:
    def __init__(self,marka,model,hiz=0):
        self.marka = marka
        self.model= model
        self.hiz = hiz

    def calistir(self):
        print("Motor çalıştı.")   

    def hizlan(self,miktar):
        self.hiz = miktar

    def durdur(self):
        self.hiz = 0

    def bilgi(self):
        print(f"Aracın markası: {self.marka} | Modeli: {self.model} | Hızı: {self.hiz}")

class Araba(Arac):
    def __init__(self, marka, model, yolcu_sayisi):
        super().__init__(marka, model)
        self.yolcu_sayisi = yolcu_sayisi

    def bagaj_ac(self):
        print("Bagaj açıldı.")

class Motosiklet(Arac):
    def hizlan(self,miktar):
        self.hiz = miktar * 1.5

araba1 = Araba("Ford","Focus",4)
motor1 = Motosiklet("Yamaha","MT-07")

araba1.calistir()
araba1.hizlan(60)
araba1.bagaj_ac()
araba1.bilgi()


motor1.hizlan(80)
motor1.bilgi()
motor1.durdur()     
motor1.bilgi()        
        