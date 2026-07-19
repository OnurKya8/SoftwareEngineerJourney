print("Bakiye = 5000 TL")
cekilecek_miktar = int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
if cekilecek_miktar <= 0:
    print("Çekilecek miktar sıfırdan büyük olmalıdır")
elif cekilecek_miktar <= 5000:
    print(f"{cekilecek_miktar} TL çekildi. \nKalan bakiye: {5000 - cekilecek_miktar} TL")
else:
    print("Yetersiz bakiye")
