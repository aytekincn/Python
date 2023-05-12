import time

from kitaplık import *  # Kütüphane sınıfımızdaki her şeyi kullanmak için dosyaları Sources Root'a çevirdik.

print("""************************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekleme
4. Kitap Sil
5. Baskı Yükselt
Çıkış için q' ya basın.


************************************""")

kitaplık = Kütüphane() # Sqlite veritabanımızı oluşturmak için kütühane classımızı tanımlıyoruz.


while ( True ):
    işlem = input("Yapmak İstediğiniz İşlemi Seçin : ")

    if ( işlem == "q" ):
        print("Programdan Çıkılıyor...")
        break

    elif ( işlem == "1"):
        kitaplık.kitaplari_goster()

    elif ( işlem == "2"):
        isim = input("Hangi Kitabı İstiyorsunuz? : ") # Kullanıcının sorgulamak istediği kitap için input alırız.
        print("Kitap Sorgulanıyor...")
        time.sleep( 2 )  # Gerçekçilik adına kitap sorgumuzu 2 sn delayliyoruz.
        kitaplık.kitap_sorgula( isim )
        print(  isim )

    elif ( işlem == "3"):
        print("Lütfen Eklemek İstediğiniz Kitabın Bilgilerini Girin..")
        isim = input("İsim : ")
        yazar = input("Yazar : ")
        yayinevi = input("Yayınevi : ")
        tur = input("Tür : ")
        baskı = int ( input("Baskı : ") )

        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baskı ) # Yeni bir tane kitap objesi oluşturduk.

        print("Kitap Ekleniyor...")
        time.sleep( 2 )

        kitaplık.kitap_ekle( yeni_kitap )
        print("Kitap Eklendi.")

    elif ( işlem == "4"):
        isim = input("Hangi Kitabı Silmek istiyorsunuz? : ")
        cevap = input("Emin Misiniz? E/H : ")
        if (  cevap == "E" ):
            print("Kitap Siliniyor...")
            kitaplık.kitap_sil( isim )
            print("Kitap Silindi.")
        else:
            print("Kitap Silme İşlemi İptal Edildi.")

    elif ( işlem == "5"):
        isim = input("Hangi Kitabın Baskısını Yükseltmek İstiyorsunuz? : ")
        print("Baskı Yükseltiliyor...")
        time.sleep( 2 )
        kitaplık.baskı_arttır( isim )
        print("Baskı Yükseltildi.")

    else:
        print("Geçersiz İşlem...")
















































