# Generatorlar pythonda iterator objeler oluşturmak için kullanılan objelerdir ve bellekte yer kaplamazlar.
# Mesela 100.000 tane değer üretip, bu değerleri bir listede tutmak bellekte çok fazla yer kaplayacaktır. O yüzden generator fonksiyon şeklinde yazmak mantıklı olur.

def kareleri_al():
    for i in range(1, 6 ):
        yield i ** 2 # Burada yield dediğimiz için değerlerimiz henüz üretilmemiş oluyor. Fonksiyonu çağırsak bile. Return'e de ihtiyaç duymayız.

generator = kareleri_al()


iterator = iter( generator ) # Bu şekilde generator objemizi iterator objeye atarız


print(next( iterator ))
print(next( iterator ))
print(next( iterator ))
print(next( iterator ))
print(next( iterator ))
print(next( iterator ))


def carpim_tablosu():
    for i in range( 1, 11):
        for j in range( 1, 11):
            yield "{} x {} = {} ".format(i, j, i*j) # Bu şekilde basit bir çarpım tablosu oluştururuz ve bellekte yer kaplamak zorunda kalmamış oluruz.

for i in carpim_tablosu():
    print( i )

# Range de örnek olarak bir generator fonksiyondur.




