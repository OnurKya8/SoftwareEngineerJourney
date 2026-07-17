kullanici_adi = input("Kullanici adinizi giriniz: ") 
yas = int(input("Yasinizi giriniz: ")) 
kilo = float(input("Kilonuzu giriniz: ")) 
boy = int(input("Boyunuzu giriniz: "))

print("Sporcu Bilgi Karti") 
print(f"""
      Ad: {kullanici_adi.capitalize()} 
      Yaş: {yas} 
      Kilo: {kilo} Kg
      Boy: {boy} Cm
      """)
print(type(kullanici_adi))
print(type(yas))
print(type(kilo))
print(type(boy))
print(dir(kullanici_adi))
print(help(str))