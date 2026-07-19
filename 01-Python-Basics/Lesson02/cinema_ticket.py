yas = int(input("Yaşınızı giriniz: "))
if yas < 0:
    print("Yaş sıfırdan küçük olamaz")
elif yas <= 6:
    print("Ücretsiz bilet")
elif yas <= 17:
    print("Çocuk bilet")
elif yas <= 64:
    print("Tam bilet")
else:
    print("İndirimli bilet")