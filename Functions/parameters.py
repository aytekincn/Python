# Fonksiyonun içine geçici bir değer verirsek fonksiyon boş çağırıldığında varsayılan değeri döndürür ancak içine değer atanırsa yerine geçer.

def bilgileriGoster ( isim = "Bilgi yok ", soyad = "Bilgi Yok", numara = "Bilgi yok"): # Geçici değer boş olarak fonksiyon çağırıldığında döner.
    print("İsim: " , isim," Soyisim :" ,soyad, " Numara : ", numara )

bilgileriGoster("Aytekin", "Can","180311017")

bilgileriGoster( numara = "180311018") # Sadece belirli bir değeri atamak için atanacak değer belirtilip sonra değer girilir. Özel olarak parametre belirtilir.



# Esnek sayıda değerler başına * koyarak oluşturulur gönderilen değerleri tuple olarak tutar. Birden fazla değer verilmesini sağlar.

def toplama ( *a ): # *a esnek sayıda değer olduğunu belirtir birden fazla değer içine atanabilir
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)

toplama(3,4,5,6,78,55) # İstediğimiz kadar değer yollarız bu değerler tuple olarak tutulur


# Global ve Yerel değişkenler
"""
def fonksiyon ():
    a = 4 # İçeride tanımladığımız değişken ise yerel değişken olur. Programın başka yerinde kullanılmaz sadece fonksiyon içine özgüdür.
    print(a)

fonksiyon()
print(a)
"""
"""
b = 10 # Burada tanımlanan değişken global değişken olur. Herhangi bir fonksiyon içinde tanımlanmadığı için programın her tarafında kullanılabilir.
def fonksiyonn():
    print(b)

fonksiyonn()
"""
"""
def fonksiyon ():
    print(s)

fonksiyon()

s = "Python"  # Burada s değişkeni fonksiyondan sonra tanımlandığı için hata verir ancak öncesinde tanımlanırsa bir sorun olmaz.
"""
# Globalde olan herhangi bir değeri fonksiyon içinde kullanmak için değişken isminin başına global getiririz.

c = 10

def fonksiyon():
    global c
    c = 3  # Burada globaldeki değeri alıp bizim verdiğimiz değerle değiştirdi.
    print(c) # Burada 3 ifadesi döner.

fonksiyon()
print(c)

# Local değişkenler fonksiyonlara özgüdür. Normal bi if bloğu içindeki bir değer de global olarak sayılır.
























