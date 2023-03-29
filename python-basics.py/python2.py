
print ("Oyuncu Kaydetme Programı")
ad = input ("Oyuncunun Adı: ")
soyad = input ("Oyuncunun Soyadı: ")
yas = int ( input ("Oyuncunun Yaşı: "))
takım = input ("Oyuncunun Takımı: ")

bilgiler = [ad, soyad, yas , takım]

print("Bilgiler Yükleniyor")

print ("Oyuncun Adı: {}\n Oyuncunun Soyadı: {}\n Oyuncunun Yaşı {}\n Oyuncunun Takımı: {}\n " .format( bilgiler [0], bilgiler [1], bilgiler [2], bilgiler [3]) )

