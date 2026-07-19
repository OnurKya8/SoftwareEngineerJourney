yas = int(input("Yasinizi giriniz: "))
if yas < 18:
    print("Kayit olamaz")
elif yas <= 60:
    print("Normal kayit")
else:
    print("Saglik raporu gerekiyor")