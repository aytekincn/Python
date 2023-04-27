# Decorator fonksiyonlar, Pythonda fonksiyonlara dinamik olarak ekstra eklediğimiz fonksiyonlardır ve decorator fonksiyonların kullanımı kod tekrarını önler.
import time
def kareleri_hesapla( sayılar ):
    sonuç = list()
    baslama = time.time()
    for i in sayılar:
        sonuç.append( i ** 2 )
        bitis = time.time()
        print("Bu fonksiyon " + str( bitis - baslama ) + "saniye sürdü.")
        return sonuç
def küpleri_hesapla ( sayılar ):
    sonuç = list()
    baslama = time.time()
    for i in sayılar:
        sonuç.append( i ** 3 )
        bitis = time.time()
        print("Bu fonksiyon " + str(bitis - baslama) + "saniye sürdü.")
        return sonuç

kareleri_hesapla( range( 100000 ) )
küpleri_hesapla( range( 100000 ) )