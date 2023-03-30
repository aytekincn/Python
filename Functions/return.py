# Return fonksiyon işlemi bittikten sonra çağırıldığı yere değer döndürür.
# Fonksiyonda alınan değer bir değişkene depolanabilir ve değeri programın farklı yerlerinde kullanabiliriz.

def toplama ( a, b, c ):
    return a + b + c

def carp ( a ):
    return a * 2


toplam = toplama (2, 3, 5 ) # Yazılan fonksiyonu başka bir değere atadık sonra da carp fonksiyonu içinde kullandık.
#  Print ile yapılınca herhangi bir değer döndürmediği için dışarıya herhangi bir değer alamazdık. Return kullanılmazsa nonType değer döndürür.
# Returnden sonra gelen işlemler çalışmaz.
# Return kullanılmayan fonksiyonlar void fonksiyonlardır.
print( carp ( toplam ) )


