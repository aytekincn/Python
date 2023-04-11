# DataFrame serilerin aynı kümede bulunmasına denebilir sql tablolarına benzerdir.
import numpy as np
import pandas as dp
import pandas as pd
from numpy.random import randn

df = pd.DataFrame( data = randn ( 3,3 ), index = ["A", "B", "C"], columns=["Column1","Column2","Column3"] )

print( df ) # Burada hem sütun hem de satırlarımızı birleşmiş halde görürüz.

# Bir tane columnu almak için df[ "Column1" ] Şeklinde sütun ismini yazarak o kısımı alırız.

print( df[ "Column1" ] ) # Column1 ismine denk gelen sütunları alırız.

print( df.loc ["A"] ) # Bu şekilde indekse karşılık gelen değerlerimizi almak için kullanırız. Burada sütun isimlerimiz yeni indekslerimiz olur.

print( df.head() ) # İlk sıraları gösterir df.tail() yaparsak da son kısımları bize gösterir.

print( df[ ["Column1","Column3"] ] ) # Burada da almak istediğimiz sütunlar için içeriye bir köşeli parantez daha açıp istediğimiz sütunları yazarız.

df["Column4"] = pd.Series( randn(3), ["A", "B", "C"] ) # Yeni bir column eklemek  için pandas serisi gibi oluştururuz ancak karşılık gelen indeksleri yazmamız lazım.

print( df )

df["Toplam"] = df["Column1"] + df["Column2"] + df["Column3"] # Bu şekilde son kısmına columnların toplamı olan bir column daha ekleyebiliriz.

print( df )

# Bir sütunu silmek için drop kullanırız ancak yatay kısmının axisi 0 dikey olan ise 1 anlamına gelir. Eğer axis değerini vermezsek dafault olarak 0 yani yatay olarak uygular ancak column ismini verdiğimiz için hata ile karşılaşırız.

df.drop("Toplam",axis = 1, inplace = True ) # Buradaki inplace parametresi dataya uygulamak için kullanılır eğer kullanılmazsa verilerin içinde uygulanmaz tekrardan veri eski haline döner default olarak false kullanır bunu true yapmalıyız.
print( df )

# df.iloc[ 0 ] buradaki iloc bize satır içindeki değerleri verir bizim df.loc[ "A"] şeklinde kullandığımız gibi indeks değerine göre alırız satırları.

print( df.iloc[1] ) # Bu şekilde kullanılır.

print ( df.loc["A","Column1"] )  # Bu şekilde kullandığımız zaman spesifik olarak istediğimiz satır ve sütunu alırız.

print ( df.loc[ [ "A", "B"], ["Column1","Column2"] ] ) # Burada da column1 ve column2 deki satırları alırız.

