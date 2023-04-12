# map ( fonksiyon, iterasyon yapılabilecek veritipi( liste,demet vb ),...)
from functools import reduce
def double(x):
    return x * 2

map( double, [1, 2, 3, 4, 5, 6, 7, 8]) # Burada oluşturduğumuz sayıları double fonksiyonuna gönderiyo daha sonra returndeki iki ile çarpılmış halini map diye bir objeye atıyo liste gibi.

df = list(map( double, [1, 2, 3, 4, 5, 6, 7, 8])) # Görmek için listeye değişken atarız.

print ( df ) # Burada map kısmına çevirilip sonra listeye atadığımız çıktıyı alırız.

aa = list(map( lambda x : x ** 2, ( 22, 43, 55, 42, 25, 12, 67 ) ) ) # Lambda ile birlikte daha pratik kullanılabilir.
print(aa)

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10]

ab = list( map ( lambda x,y : x * y, liste1, liste2  ) )

print( ab )
#-------------------------------------------------------------------------------

# reduce() Değer aldığı fonksiyonu soldan başlayarak listenin 2 elemanına uygular daha sonra çıkan sonucu listenin 3. elemanına uygular böyle devam eder faktoriyel gibi düşünebiliriz.

a = reduce(lambda x,y : x * y, [1, 2, 3, 4, 5]) # 1 ve ikiyi çarpıp sonrasında devam ederi tek tek çarpmaya
print(a)

def maksimum( x,y ):
    if ( x > y ):
        return x
    else:
        return y

b = reduce( maksimum, [-1, 2, 3, 5, 66, 7, 532, 23]) # -1 ve 2 yi alır sonra elinde maks değer olan 2 olduğu için onu tutar sonra 5 e gider 5 i alır sonra 66 sonra 7 yi almaz küçük olduğu için sıra sıra devam eder.

print(b)

#--------------------------------------------------------------------------------

# filter fonksiyonu birinci parametre olarak mutlaka true, false alır. Liste gibi veritiplerinin her bir elemanına bu fonksiyonu uygular.

c = list ( filter ( lambda x : x % 2 == 0, [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10] ) )

print(c) # Burada sadece true olan değerleri döndürür.

#----------------------------------------------------------------------------------

# Zip fonksiyonu listeleri vs gruplamamızı sağlar

liste3 = [1, 2, 3, 4, 5]
liste4 = [6, 7, 8, 9, 10, 11]

y = list ( zip ( liste3, liste4) ) # zip fonksiyonu ile kolayca birbirine eşleriz
print( y )

sozluk1 = {"Elma":1, "Armut":2, "Kiraz":3}
sozluk2 = {"Sıfır":0, "Bir":1, "İki":2}

for i,j in zip ( sozluk1,sozluk2): # listeler içinde gezerken kullanışlı hale gelir
    print(  i,j )

sozluk = list ( zip ( sozluk1,sozluk2)) #

print( sozluk )

keys = list ( zip ( sozluk1.values(), sozluk2.values() ) ) # Sadece anahtarları alır

print(keys)

#-----------------------------------------------------------------------------------

# listelerde veya başka formatlarda bulunan elemanları hem indekslerini hem de elemanlarını almak için enumerate kullanırız.

liste5 = ["Elma", "Armut", "Portakal", "Kiraz"]

f = list ( enumerate ( liste5 ) )

print( f )

for i,j in enumerate( liste5 ):  # Bu şekilde kullanıldığında 0 Elma diye başlayarak devam eder hem indeks numarası hem de elemanı görürüz.
    print( i,j )







