import sqlite3
import time

class Kitap():

    def __init__(self, isim, yazar, yayinevi, kitap_tur, baskı ):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.kitap_tur = kitap_tur
        self.baskı = baskı

    def __str__(self):
        return "Kitap isim : {}\nKitap Yazarı : {}\nKitap Yayınevi : {}\nKitap Türü : {}\nKitap Baskı : {}" .format(self.isim, self.yazar, self.yayinevi, self.kitap_tur, self.baskı)



class Kütüphane():
    def __init__(self):
        self.baglantı_olustur()

    def baglantı_olustur(self):  # sqlite veritabanına ulaşmak için kullanılan fonksiyon.
        self.baglantı = sqlite3.connect("kitaplık.db") # Veritabanı oluşturduk.
        self.cursor = self.baglantı.cursor() # Veritabanı üzerinde işlem gerçekleştireceğim cursor oluşturma.

        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar ( isim TEXT, Yazar TEXT, Yayınevi TEXT, Tür TEXT, Baskı INT )" # Kitaplığımızı oluşturacak sorgu.
        self.cursor.execute( sorgu ) # Sorguyu çalıştırırız.

        self.baglantı.commit() # Tabloda değişiklik işlemi için commit komutumuzu yazdık.

    def baglantıyı_kes(self):
        self.baglantı.close() # Bağlantıyı kesmemize yarayan fonksiyon.

    def kitaplari_goster(self): # Kitap bilgilerimizi göstermek için bir fonksiyon.
        sorgu = "SELECT * From kitaplar"
        self.cursor.execute( sorgu )
        kitaplar = self.cursor.fetchall()

        if ( len( kitaplar ) == 0 ) :
            print("Kütüphanede Kayıtlı Kitap Yok..")
        else:
            for i in kitaplar:
                kitap = Kitap( i[0], i[1], i[2], i[3], i[4] ) # Kitaplarımızı demet içine yazarız.
                print( kitap )


    def kitap_sorgula(self, isim ): # Kitap sorgulamak için bir fonksiyon yazıyoruz
        sorgu = "SELECT * From kitaplar WHERE İsim = ? "
        self.cursor.execute( sorgu, ( isim, ) )
        kitaplar = self.cursor.fetchall()

        if ( len(kitaplar) == 0 ):
            print("Böyle bir kitap bulunmuyor..")
        else:
            kitap = Kitap( kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], kitaplar[0][4] )
            print( kitap )

    def kitap_ekle(self, kitap ): # Kitap eklemek için fonksiyon yazıyoruz.
        sorgu = "INSERT INTO kitaplar VALUES (?, ?, ?, ?, ? )"
        self.cursor.execute( sorgu, (kitap.isim, kitap.yazar, kitap.yayinevi, kitap.kitap_tur, kitap.baskı ) )
        self.baglantı.commit() # Bilgilerimizi güncellemek için commit kullanırız.


    def kitap_sil(self, isim): # Silmek istenilen kitap için bir fonksiyon oluştururuz.
        sorgu = "DELETE From kitaplar WHERE isim = ? "
        self.cursor.execute( sorgu, ( isim, ) )
        self.baglantı.commit()

    def baskı_arttır(self, isim ): # Baskı sayısını arttırmak için fonksiyon.
        sorgu = "SELECT * From kitaplar WHERE isim = ? "
        self.cursor.execute( sorgu, ( isim, ))

        kitaplar = self.cursor.fetchall()

        if ( len(kitaplar) == 0 ):
            print("Böyle bir kitap bulunmuyor.")
        else:
            baskı = kitaplar[0][4] # Baskı sayımızın olduğu 4.indeksi alırız. Üzerinde işlem yapabilmek için.
            baskı += 1

            sorgu2 = "UPDATE kitaplar SET baskı = ? WHERE isim = ? "
            self.cursor.execute(sorgu2, ( baskı, isim, ))
            self.baglantı.commit()


















