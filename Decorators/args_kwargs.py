# İç içe fonksiyonlar ve Fonksiyon parametreleri
# Bu yapılar, fonksiyon kullanırken bazen dışardan alacağımız parametre sayısını bilmiyorsak veya parametre sayısı değişkenlik gösteriyorsa kullanılır.
# Böylelikle fonksiyonumuza dinamiklik kazandırmış oluyoruz.
# Sınırsız sayıda parametreli fonksiyon oluşturmak için parametremizin önüne tek yıldız (*) koyabiliriz. Bunu da *args ile yaparız.

def fonksiyon1( *args ): # Gönderdiğimiz argümanlar parametreler burada demet haline dönüştürülür.
    for i in args:
        print( i )

fonksiyon1( 1, 2, 3, 4 )


def fonksiyon2 (isim, *args ):
    print( "İsim : ", isim )

    print("-------------")

    for i in args:
        print( i )

fonksiyon2("Aytekin", 1, 2, 3, 4, 5, 6 ,7) # Buradaki stringimiz isim değişkeni ile eşleşir sonrasında yolladığımız rakamlar args değişkeniyle eşleşir.


def topla( *args ):
    print(sum( args ) ) # Burada args parametresi ne kadar sayı verilirse öyle çalışır.

topla(10 ,3, 20, 30 )


# **kwargs da kaç tane parametre kullanacağımız bilmediğimiz durumlarda kullanıyoruz ancak **kwargs anahtar değer ilişkisine dayanıyor. Sözlük tipi olarak düşünebiliriz.

def fonksiyon3 ( **kwargs ) :
    print( kwargs )

fonksiyon3(isim = "Aytekin", soyisim = "Can", numara = 124124 )
def yazdir(**kwargs):
    print(kwargs)

yazdir(sayi1 = 5, sayi2 = 6, sayi3 = 7) # Burada gönderdiğimiz değerleri bize sözlük veritipinde çıkarır.

# *args ve **kwargs birlikte kullanılabilir. Ama *args fonksiyonda ilk yazılmalı yoksa Syntax hatası olur.

def yazdir1(*args,**kwargs):
    print(kwargs)
    print(args)

yazdir1(4 ,6 ,8 ,30 , sayi1 = 5,sayi2 = 6,sayi3 = 7 )



def fonksiyon4 ( *args, **kwargs ):
    for i in args:
        print( i )

    print("-------------")

    for i, j in kwargs.items(): # Sözlük içine atmak için .items kullanıyoruz.
        print( i, j )

fonksiyon4(1,2,3,4,5,6,7,8,9, isim = "Aytekin", soyisim = "Can", numara = 124124 )


















