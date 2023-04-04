"""
       try :

            Hata çıkarabilecek kodlar buraya yazılır.
            Eğer hata çıkarsa program uygun olan except bloğuna girer.
            Hata oluşursa try bloğunun geri kalan işlemleri çalışmaz.

       except Hata1 :
            Hata1 oluşunca bu kısım çalışır.
       except Hata2 :
            Hata2 oluşunca bu kısım çalışır.

            //
            //
            //
        finally :
                Mutlaka çalışması gereken kodlar bu kısma yazılır.
                Bu blok her türlü çalışır.

"""



try :    # Hata olabilecek kodu bu kısma yazıyoruz.
    a = int ( input("Sayı1 : ") )
    b = int ( input("Sayı2 : ") )
    print( a / b )

except ValueError: # Hatayı belirtmezsek  burada bütün hatalar bu blok içine girer. Hata ismine göre except bloğu açıp hatayı yazdırabiliriz.
    print("Lütfen doğru bir sayı girin.")
except ZeroDivisionError:
    print("Bir Sayı 0' a Bölünemez.")
print("Bloklar sona erdi...")

# Except kısımlarını ayrı ayrı yazmak yerine birlikte de yazılabilir.

try :
    a = int ( input("Sayı1 : ") )
    b = int ( input("Sayı2 : ") )
    print( a / b )

except ( ValueError, ZeroDivisionError ) : # Bu şekilde hataları yan yana yazıp birlikte kullanabiliriz.
    print("ValueError veya ZeroDivisionError Hatası.")

finally:
    print("Burası Çalıştı")

# Hata fırlatmak kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatalarımızı üretip Pythonda bu hataları fırlatabiliriz.
# Bunun için raise keyword kullanılır.

def terscevir (s):
    if ( type(s) != str ):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]

print ( terscevir(12) )

try :
    print(terscevir(12))
except ValueError:
    print("Fonksiyon hata verdi")