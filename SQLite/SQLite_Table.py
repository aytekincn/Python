"""
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık ( İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT )")
    con.commit()

tablo_olustur()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES('Istanbul Hatırası','Ahmet Ümit','Everest', 561)") # Verilerimizi sql sorgularında olduğu gibi ekleyebiliriz. Büyük küçük harf fark etmeden sorgular yazılabilir.
    con.commit()

veri_ekle()


def veri_ekle2( isim, yazar, yayinevi, sayfa_sayisi ): # Kullanıcıdan aldığımız değerleri girmek için fonksiyon oluştururuz.
    cursor.execute("INSERT INTO kitaplık VALUES( ?, ?, ?, ?)", ( isim, yazar, yayinevi, sayfa_sayisi ) ) # Buradaki soru işaretleri kullanıcıdan aldığımız değerleri girmek istediğimiz için yanına tuple içinde bilgileri vermemiz gerekir.
    # isim yazar vs gönderdiğimizde sırasıyla soru işaretlerinin yanına geçecek.
    con.commit()

isim = input("İsim ? ")
yazar = input("Yazar  ? ")
yayinevi = input("Yayınevi ? ")
sayfa_sayisi = int(input("Sayfa Sayısı ? "))

veri_ekle2( isim, yazar, yayinevi, sayfa_sayisi )

#---- Veritabanı Üzerinde Sorgular ----
def verileri_al():
    cursor.execute("Select * From kitaplık") # Burada veritabanındaki tüm verileri almak için select * komutunu kullanırız. SQL sorgularında olduğu gibi.
    liste = cursor.fetchall() # Buradaki fetchall bize işlem yaptığımız cursor üzerindeki bütün bilgileri döndürecek. Ve döndüğü bilgiler listeye eşit olacak o yüzden liste adlı değişkene ekleriz.
    # Veritabanı üzerinde herhangi bir değişiklik yapmadığımız için con.commi() kullanmayız. Bunun yerine direkt bize döndüreceği listeyi printleriz.
    print ("Kitaplık Tablosunun Bilgileri....")
    for i in liste: # Burada for döngüsünü kullanarak daha güzel bir görünüm sağlayabiliriz.
        print ( i )

verileri_al()


def verileri_al2():
    cursor.execute(" Select İsim, Yazar From kitaplık ") # Sadece kitap ismi ve yazarı almak için kullandığımız sorgu.
    liste = cursor.fetchall() # Verilerimizin hepsini seçmek için fetchall fonksiyonunu kullanırız.
    print ("Kitaplık Tablosu İsim ve Yazar Bilgileri...")
    for i in liste:
        print ( i )

def verileri_al3( yayinevi ):
    cursor.execute(" Select * From kitaplık WHERE Yayınevi = ?", ( yayinevi, ) ) # Önceki sorguda yaptığımız gibi burada da yayınevine verdiğimiz değer soru işareti yerine geçecek.
    liste = cursor.fetchall()
    for i in liste:
        print ( i )

verileri_al3( "Metis Edebiyat" ) # Burada fonksiyon içindeki sorgumuza hangi yayınevinin bilgilerini almak istiyosak onu söylüyoruz.

def verileri_guncelle( eski_yayinevi, yeni_yayinevi ): # Değiştireceğimiz hem eski hem de yeni yayınevini yazacağımız için değerlerimizi bu şekilde göndeririz.
    cursor.execute("UPDATE kitaplık set Yayınevi = ? WHERE Yayınevi = ? ", (yeni_yayinevi, eski_yayinevi ) ) # Önce update edeceğimiz yeni değeri yazıyoruz ardından hangisiyle değiştireceğimiz where komutu ile yazıyoruz.
    con.commit() # Veritabanını güncellemek istediğimiz için commit kullanırız. Aynı şekilde ekleme çıkarma işlemlerinde de commit kullanılır.

verileri_guncelle("Doğan Kitap", "Everest") # Burada yolladığımız değerleri fonksiyon parantezinin içindeki sıraya göre göndeririz.

def verileri_sil( yazar ):
    cursor.execute(" DELETE From kitaplık WHERE yazar = ? ", ( yazar, )) # Verilerimizi silmek için kullandığımız method hepsini silmek için * kullanırız.
    con.commit()


verileri_sil()

con.close()


"""