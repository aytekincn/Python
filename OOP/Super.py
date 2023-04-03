# SUPER --------------------------------------
# Override ettiğimiz metodun içinde aynı zamanda miras aldığımız metodu kullanmak istersek kullanılır.
# super genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar.

class Calısan():
    def __init__(self, isim, maas, departman ):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("Çalışan sınıfı bilgileri.")
        print(" İsim : {}\n Maaş : {}\n Departman : {} " .format(self.isim,self.maas,self.departman ) )



class Yonetici (Calısan):
    def __init__(self, isim, maas, departman, kisi_sayisi):

        super().__init__(isim, maas, departman, ) # Buradaki gibi almak istediğimiz özellikleri kısa bir şekilde yazarak alabiliriz.
        self.kisi_sayisi = kisi_sayisi  # Ekstra eklemek istediğimiz özelliği ekleriz.

        print("Yönetici sınıfının override init fonksiyonu")

    def bilgileriGoster(self):
            print("Yönetici sınıfı bilgileri.")
            print(" İsim : {}\n Maaş : {}\n Departman : {}\n Sorumlu Olduğu Kişi : {}  ".format(self.isim, self.maas, self.departman, self.kisi_sayisi ) )


        # self.isim = isim
        # self.maas = maas      >>> Buradaki gibi özellikleri tek tek  yazmak yerine super kullanıp yanın ekstra eklemek istediğimiz özelliği ekleyebiliriz.
        # self.departman = departman


yonetici = Yonetici("Aytekin Can ", 3000, "Bilişim", 5 ) # İki classında içindeki print fonksiyonları çalıştı.

yonetici.bilgileriGoster()