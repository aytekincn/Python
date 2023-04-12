# multiIndex İndekslerimizi grup altında toplamamıza yarar.
import numpy as np
import pandas as pd
from  numpy.random import randn

outerIndex = ["Group1", "Group1", "Group1", "Group2", "Group2", "Group2", "Group3", "Group3", "Group3",]
innerIndex = ["Index1", "Index2", "Index3", "Index1", "Index2", "Index3", "Index1", "Index2", "Index3",]

tables = list ( zip( outerIndex, innerIndex) )

tables = pd.MultiIndex.from_tuples( tables )

print( tables )

df = pd.DataFrame( randn( 9,3 ), tables, columns = ["Column1", "Column2", "Column3"]  )   # Burada 3 tane indeksi grupların içine atarız ayrı ayrı

print( df.loc["Group2"] ) # Gruptaki verilere ulaşabiliriz.


print( df.loc[ ["Group1","Group3"] ] )

# Grup içindeki spesifik bir indeksi almak için

print( df.loc["Group3"].loc["Index3"]["Column2"] ) # Bu şekilde datayı parçalayabiliriz.

df.index.names = ["Groups", "Indexes"] # Gruplara ve indekslere başlık ekleyebiliriz.

print( df )

# .xs kullanarak da sorgularımızı yapabiliriz.

print( df.xs("Group1").xs("Index2") ) # İndeks içindeki sorgulara kadar yapılabilir.
print( df.xs("Index1", level = "Indexes" ) ) # Grupların içindeki 1.indeksleri almak için level belirterek kullanıyoruz. Sorguyla içerideki indeksleri seçmek istediğimizi söylemiş oluruz.






















