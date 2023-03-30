# Fonksiyonlar belirli işlevleri olan ve tekrar tekrar kullanılan yapılardır.
"""
  Fonksiyonların Tanımlanması

     def fonksiyon_adı ( parametre1, parametre2,..... ( opsiyonel ) ):
        # Fonskiyon bloğu
        Yapılacak işlemler
        # Dönüş değeri - opsiyonel
"""

def selamla ( isim ): # Fonksiyonu tanımlıyoruz. İçine parametre atarsak verilen parametreye göre çalışır.
    print("Merhaba...." , isim )



selamla( "Aytekin" ) # Fonksiyonu çağırma bu şekilde eğer içine atanacak değer varsa parantez içinde gönderilir. Burada içine gönderdiğimiz değer argüman olarak geçer.
# Type belirlemeye gerek olmadığı için hangi değeri girersek o değeri içine atar.


def toplama ( a, b ):
    print(a + b)


toplama(30, 50 )



def faktoriyel ( sayı ) :
    faktoriyel = 1
    if ( sayı == 0 or sayı == 1 ):
        print("Faktoriyel : ", faktoriyel )
    else :
        while ( sayı >= 1 ):
            faktoriyel *= sayı
            sayı -= 1

        print ( faktoriyel )


faktoriyel( 5 )








