import threading
import time
import os
import pygame

class AlarmSistemi:
    def __init__(self,ses_dosyasi):
        self.ses_dosyasi = ses_dosyasi
        self.aktif = False
        if not os.path.exists(self.ses_dosyasi):
            print("Ses dosyası yok.Kontrol Edin.")
        pygame.mixer.init()

    def sesi_oynat(self):
        pygame.mixer.music.load(self.ses_dosyasi)
        pygame.mixer.music.play()
        while self.aktif:
            time.sleep(0.5)
        pygame.mixer.music.stop()

    def cal(self):
        if self.aktif == True:
            print("Alarm zaten çalışıyor.")
            return
        self.aktif = True
        t = threading.Thread(target=self.sesi_oynat,daemon=True)
        t.start()

    def durdur(self):
        self.aktif = False
        print("Alarm susturuldu.")  

    def durum(self):
        if self.aktif == True:
            return "Alarm aktif"
        else:
            return "Alarm aktif değil"      

if __name__ == "__main__":
    alarm = AlarmSistemi("beep.wav")
    print(alarm.durum())
    alarm.cal()

    time.sleep(3)
    print(alarm.durum())
    alarm.durdur
