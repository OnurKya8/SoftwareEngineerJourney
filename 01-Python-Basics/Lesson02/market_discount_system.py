ucret = float(input("Lütfen ücreti giriniz: "))
if ucret < 0 : 
    print("Ücret sıfırdan az olamaz")
elif ucret <= 1000:
    print("İndirim yok" "\nÖdenecek tutar: " + str(ucret))
elif ucret <= 3000:
    print("%10 indirim uygulanmıştır. \nÖdenecek tutar: " + str(ucret - (ucret * 0.1)))
else:
    print("%20 indirim uygulanmıştır. \nÖdenecek tutar: " + str(ucret - (ucret * 0.2)))