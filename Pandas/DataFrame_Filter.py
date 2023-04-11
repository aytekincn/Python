import numpy as np
import pandas as dp
import pandas as pd
from numpy.random import randn

df =  pd.DataFrame( data = randn( 4,3 ), index = ["A", "B", "C", "D" ], columns = ["Column1", "Column2", "Column3"] )

print( df )

# pandas serilerinde olduğu gibi dataframeleri de filtreleyebiliyoruz.

booleanDf = df > -1 # Bu şekilde basit bir filtreleme işlemi yapabiliriz

print( booleanDf )

print( df[ booleanDf ] ) # Bu şekilde köşeli parantez içine atarsak true değerler gözüküp false olanlar ise NaN olarak çıkar
# Değişken zorunlu değil aynı şekilde print ( df[ df > -1 ] ) şeklinde direkt yazılabilir.

# df[ "Column1 " ] > 0 yazdığımızda column 1 deki değerleri true false olarak gösterir.

# Ancak

print( df[ df ["Column1"] < 0  ] ) # Sütundaki false olan indeksin hiçbirini almaz sadece true olanlar döner. Arattığımız sütun için geçerli


# Bu sorguları bağlaçlarla birleştiririz ancak pandas and kabul etmediği için & kullanılır.

print ( df[ ( df ["Column1"] < 0 ) & ( df["Column2"] > 0 ) ] ) # İkisinde de ortak olan kısımı döndürür burada D satırı olur.

# Aynı şekilde or ile de bağlayabilirz ancak or yerine | kullanırız.

df["Column4"] = randn(4)

print( df )

df["Column5"] = ["New1","New2","New3","New4"]

print( df )

df["Column6"] = [1, 2, 3, 4 ]  # Bu şekilde str, int veya başka türlerde datalar ekleyebiliriz.
print( df )


# Herhangi bir sütundaki değerleri indeks değerleri ile değiştirebiliriz.

df.set_index("Column5",  inplace = True )

print( df )

df.index.names(["Column5"]) # İndex isimlerini gösterir.















