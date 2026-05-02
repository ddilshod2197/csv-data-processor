import csv
import pandas as pd

def saralash(fayl_nomi):
    # CSV fayldan ma'lumotlarni o'qib olamiz
    ma'lumotlar = pd.read_csv(fayl_nomi)

    # Yuqori o'rta daraja (46-70) bo'lgan ma'lumotlarni saralaymiz
    saralangan_ma'lumotlar = ma'lumotlar[(ma'lumotlar['daraja'] >= 46) & (ma'lumotlar['daraja'] <= 70)]

    # Yangi faylga yozamiz
    saralangan_ma'lumotlar.to_csv('saralangan_ma'lumotlar.csv', index=False)

# Fayl nomini kiritamiz
fayl_nomi = 'ma'lumotlar.csv'
saralash(fayl_nomi)
```

```python
import csv

def saralash(fayl_nomi):
    # CSV fayldan ma'lumotlarni o'qib olamiz
    with open(fayl_nomi, 'r') as f:
        oqilgan_ma'lumotlar = list(csv.reader(f))

    # Yuqori o'rta daraja (46-70) bo'lgan ma'lumotlarni saralaymiz
    saralangan_ma'lumotlar = [satir for satir in oqilgan_ma'lumotlar if 46 <= int(satir[1]) <= 70]

    # Yangi faylga yozamiz
    with open('saralangan_ma'lumotlar.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(saralangan_ma'lumotlar)

# Fayl nomini kiritamiz
fayl_nomi = 'ma'lumotlar.csv'
saralash(fayl_nomi)
