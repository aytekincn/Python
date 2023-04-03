# Inheritance ( kalıtım ) bir sınıfın başka bir sınıftan özelliklerini ( attribute ) ve metodlarını miras almasıdır.
# Örnek olarak bir şirketin proje direktörü ile yöneticisinin isim, soyisim, maaş, departman değiştirme gibi özellikler ortak özellikleri olabilir.

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




class Yonetici(Calısan):  # Bu şekilde başka classımızın içine miras almasını istediğimiz classı giriyoruz.
    pass # Bir bloğu sonradan tanımlamak için kullanılır.


yonetici = Yonetici("Aytekin Can", 5000, "Bilişim") # Miras aldığımız sınıfın içine değerleri gönderdik.

yonetici.bilgileriGoster() # Gönderdiğimiz bilgileri kontrol.

yonetici.departmanDegis("Project Management")

yonetici.bilgileriGoster()

print(dir(yonetici)) # Yonetici sınıfının özelliklerini görmemize yarar.




class Yonetici (Calısan): # Hem miras alıp hem de kendimiz yeni özellikler ekleyebiliyoruz.
    def zam_yap(self, zam_miktarı ):
        self.maas += zam_miktarı


yonetici = Yonetici("Mert Söylemez", 6500, "IT" )

yonetici.zam_yap(600)

yonetici.bilgileriGoster()




