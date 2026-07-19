yas = int(input("Lütfen yaşınızı giriniz: "))
if yas <= 0 or yas >= 100:
    print("Lütfen geçerli bir yaş giriniz")
elif yas < 18:
    print("Ehliyet alamazsınız")
else:
    print("Ehliyet alabilirsiniz")