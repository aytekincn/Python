# Override ( İptal Etme )
# Miras alınan metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak, artık metodu çağırdığımızda miras alınan değil kendi yazdığımız metod çalışır.

class Calısan():
    def __init__(self, isim, maas, departman ):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("Çalışan sınıfı bilgileri.")
        print(" İsim : {}\n Maaş : {}\n Departman : {} " .format(self.isim,self.maas,self.departman ) )

    def departmanDegis(self, yeni_departman ):
        self.departman = yeni_departman


class Yonetici (Calısan): # Miras aldığımız classı kullandığımızda ekstra özellik ekleyemeyiz . Ekstra özellik eklemek için override etmemiz gerekli. init fonksiyonunu tanımlamamız lazım.
    def __init__(self, isim, maas, departman, kisi_sayisi): # Bu şekilde init fonksiyonu tanımlayıp ekstra özellik ekliyoruz classa.
        print("Yönetici sınıfının override init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi
        # Yönetici sınıfından normal bir obje oluşturduğumuz zaman override ettiğimiz init fonksiyonu çalışacak.

    def bilgileriGoster(self):
        print("Yönetici sınıfı bilgileri.")
        print(" İsim : {}\n Maaş : {}\n Departman : {}\n Sorumlu Olduğu Kişi : {}  " .format(self.isim,self.maas,self.departman, self.kisi_sayisi ) )
        # Burada bilgileri göster fonksiyonunu da override ederiz.

    def zam_yap(self, zam_miktarı ):
        self.maas += zam_miktarı

yonetici = Yonetici("İsrafil Emin ", 7000, "Java Tester", 12 )

yonetici.bilgileriGoster()






























