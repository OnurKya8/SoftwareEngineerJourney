puan = float(input("Lüten Öğrencinin notunu giriniz: "))
if puan < 0:
    print("Not sıfırdan küçük olamaz")
elif puan < 50:
    print("FF")
elif puan <= 59:
    print("DD")
elif puan <= 69:
    print("CC")
elif puan <= 79:
    print("BB")
elif puan <= 89:
    print("BA")
elif puan <= 100:
    print("AA")
else:
    print("100'den büyük not olamaz")