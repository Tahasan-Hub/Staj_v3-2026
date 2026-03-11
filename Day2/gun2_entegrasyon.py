from gun2_csv_logger import CSVLogger
from gun2_alarm import AlarmSistemi
from gun1_kisi import Kisi
import random
import time

k1 = Kisi(0,(10,20))
k2 = Kisi(1,(50,60))
k3 = Kisi(2,(100,110))

kisiler_listesi = [k1,k2,k3]

logger = CSVLogger("ihlal_takip.csv")
alarm = AlarmSistemi("beep.wav")

for i in range(10):
    sec = random.choice(kisiler_listesi)
    sec.toplam_ihlal += 1
    logger.ihlal_kaydet(sec,"Simülasyon",0.0,0.0)
    print(f"Tur {i+1}: {sec.kisi_id} ID'li kişi ihlal yaptı. Toplam: {sec.toplam_ihlal}")
    if sec.toplam_ihlal >= 3:
        alarm.cal()
    time.sleep(2)

for i in kisiler_listesi:
    print(f"ID: {i.kisi_id} | Son Konum: {i.konum} | Toplam İhlal: {i.toplam_ihlal}")



