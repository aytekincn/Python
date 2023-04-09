# Arraylerde de listelerde olduğu gibi [ : : 2 ] gibi metodları kullanabiliriz.
import numpy as np

arr = np.arange(1, 15 )

arr [ : 2]  = 25 # İkiye kadar olan kısmı 25 yapma.

print( arr )

# arr şeklinde arraylerimizi oluşturduktan sonra ismini verdiğimiz arr arr2 şeklindeki her array etkilenir bunun olmaması için.

arr2 = arr.copy() # Bunu kullanarak iki tane aynı array için farklı işlemler yapabiliriz.

newArray = np.arange(1, 21 )

newArray = newArray.reshape( 5,4) # Bu şekilde eşitleme yapmamız lazım yoksa kabul etmez geçici olur. Kullanılamaz
print( newArray )

# newArray [: , : 2] şeklinde yazdığımız zaman satırlarımızın hepsini alırız ancak sütunlardan sadece 2 tanesini alırız.
# newArray [ : 3 , : 3 ] 0 1 ve 2. satırı alır onun içinden de 0 1 2 yi alır.

print( newArray > 3 ) # Burada 3 ün üstündeki değerler true altındaki değerler false olarak döner. False olan değerleri içinden atmak için de şunu kullanırız.

booleanArray = newArray > 3

print ( newArray [ booleanArray ] )  # Yukarıda işlemi yapmasını istediğimiz yer ile eşleştiririz ardından bu şekilde yazdığımızda true olan değerler kalır false olanlar arrayden atılır.

# Bunun daha kısa bir yöntemi olan aşağıdaki yöntemi kullanırız.
print( newArray [ newArray > 5 ] )

# arraylerimizi aynı indeks büyüklüğüne sahipse toplarız direkt olarak ancak farklı ise düz toplanmaz. Aynı şekilde eksi çarpı bölüm şeklinde de yapabiliriz.
# arr adında bir değişkeni yazdıktan sonra +10 eklersek her elemana uygular diğer işlemeler de geçerli. sqrt() gibi fonksiyonlar da kullanılabilir.


np.arange(1,17).reshape(4,4) # 1'den 16'ya kadar değer bulunduran 4x4'lük bir matris.





