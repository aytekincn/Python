class Yazılımcı() :
    def __init__(self, isim, soyisim, numara, maas, bildigi_diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.bildiği_diller = bildigi_diller
    def bilgileriGoster(self): # Obje üzerinde herhangi bir özelliğe erişmek için self referansı göndeririz.
        # Objeye method ekleme bu şekilde olur.

        print("""
        Yazılımcı objesinin özellikleri...
        
        İsim : {} 
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Diller : {}
               
        """ .format(self.isim, self.soyisim, self.numara, self.maas, self.bildiği_diller ) ) # Erişim için bilgiler methodu içinde self kullanırız.

    def zamYap (self, zam_miktarı ) :
        print("Zam yapılıyor..")
        self.maas += zam_miktarı  # Bu şekilde çeşitli methodlar tanımlayabiliriz.
    def dilEkle (self,yeni_dil):
        print ("Dil ekleniyor..")
        self.bildiği_diller.append( yeni_dil )




yazılımcı = Yazılımcı("Aytekin ", "Can", 1822482, 10000, ["Pyhton", "Java"] )


yazılımcı.bilgileriGoster()  # Normal bi obje üzerinde method kullanmak gibi çağırabiliriz.


yazılımcı.dilEkle("JavaScript") # Oluşturduğumuz methodlar içine bu şekilde yeni eklenecek bilgileri gönderebiliriz.

yazılımcı.bilgileriGoster()

yazılımcı.zamYap(500)

yazılımcı.bilgileriGoster()

# Hepsinin ortak özelliklerinden biri method olduğu için self referansını göndermemiz gerek.





