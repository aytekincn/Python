# str ve len fonksiyonu class içi kullanımı

class Kitap ():
    def __init__(self,kitap_adi, yazar, sayfa_sayisi, yayinevi ):
        print("init fonksiyonu")
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.yayinevi = yayinevi

    def __str__(self):  # String değerde bir method yazabiliriz.
        return " Kitap İsmi : {}\n Yazar : {}\n Sayfa : {}\n Yayınevi : {}" .format(self.kitap_adi, self.yazar, self.sayfa_sayisi, self.yayinevi )

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):
        print("Kitap objesi siliniyor")

kitap = Kitap("İstanbul Hatırası", "Ahmet Ümit", 560, "Pegasus")

print(kitap)

print( len( kitap ) )  # Bu şekilde len fonksiyonlu bir metod yazabiliriz

del kitap