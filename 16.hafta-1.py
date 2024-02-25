
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

# Teknoloji hisselerinin listesini tanımla
teknoloji_hisseleri = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'INTC', 'AMD', 'ORCL']

# Bitiş tarihini bugün olarak ve başlangıç tarihini bugünden 12 ay önce olarak tanımla
bitis_tarihi = datetime.today()
baslangic_tarihi = bitis_tarihi - timedelta(days=365)

# Tarihsel hisse senedi verilerini indir
veri = yf.download(teknoloji_hisseleri, start=baslangic_tarihi, end=bitis_tarihi)['Adj Close']

# Geçmiş 11 ayın kümülatif getirilerini hesapla (en son ayı hariç tut)
kumulatif_getiriler = veri.pct_change().fillna(0).add(1).cumprod().iloc[-22]  # Ayda yaklaşık 22 iş günü olduğunu varsayarak

# Hisseleri kümülatif getirilerine göre sırala
sirali_hisseler = kumulatif_getiriler.sort_values()

# Alınacak hisseler, en yüksek getiriye sahip olanlar (10. decil)
alinacak_hisseler = sirali_hisseler.tail(int(len(sirali_hisseler) * 0.1)).index.tolist()

# Açığa satılacak hisseler, en düşük getiriye sahip olanlar (1. decil)
aciga_satacak_hisseler = sirali_hisseler.head(int(len(sirali_hisseler) * 0.1)).index.tolist()

print("Alınacak Hisseler:", alinacak_hisseler)
print("Açığa Satılacak Hisseler:", aciga_satacak_hisseler)
