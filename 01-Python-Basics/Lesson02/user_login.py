kullanici_adi = input("Kullanıcı adınızı giriniz: ")
sifre = input("Şifrenizi giriniz: ")
if kullanici_adi == "admin" and sifre == "1234":
    print("Giriş başarılı")
else:
    print("Kullanıcı adı veya şifre hatalı")
