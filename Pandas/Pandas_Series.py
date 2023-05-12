# Pandas serileri bir tane indeks ve o indekse karşılık gelen bir değerden oluşur.
# numpy ve pandas import edilir
# pandas serisi oluşturmak için kullandığımız kısayol olan pd.Series( sırasıyla veri ve indeks listesi eklenir data_list, labels gibi sırayla da yazılabilir data = liste adı , index = indeks olacak kısım adı da yazılabilir.)
import numpy as np
import pandas as pd
labels = ["Aytekin", "Mert", "İsrafil", "Bedirhan"]

data = [10, 20, 40, 50 ]

a = pd.Series( data = data, index = labels) # Bu şekilde gelecek indeks ve data kısmını sırasyıla .Series kullanarak oluştururuz
# Herhangi bir index vermezsek default olarak 0 1 2 3 şeklinde indeksler.
print(a)

npArray = np.array( [10,20,30,40]) # Aynı şekilde array oluşturup pandasta kullanabiliriz.

b = pd.Series(npArray)
print( b )

c = pd.Series( data = npArray, index = ["A", "B", "C", "D"] ) # Bu şekilde indekslerimi içeride de belirleyebiliriz.
print( c )

# Sözlük veri tipini kullanarak data ve indekslerimizi oluşturabiliriz.

dataDict = {"Aytekin":10, "Mert":20, "İsrafil":30 }

d = pd.Series( dataDict ) # Bu şekilde direkt olarak series fonksiyonu içine attığımızda hem indeksi hem de key value olarak data kısmına otomatik atar.
print( d )

ser2017 = pd.Series([5, 10, 15, 20], ["Buğday", "Mısır", "Çilek", "Pancar"] ) # Hem data kısmını hem index kısmını belirleyebiliriz.



ser2018 = pd.Series( data = [10, 12, 33, 43], index = ["Buğday", "Mısır", "Erik", "Pancar"] )

print( ser2017 + ser2018 )  # Burada aynı olan değerler toplandı ancak farklı isimdeki değerlere NaN ( not a number ) çıktı. İkiside aynı olmadığı için bu NaN hatası aldık.

# İçerideki verilerimize ulaşmak için de

total = ser2017 + ser2018

print( total ["Buğday"] ) # Bu şekilde datamıza ulaşabiliriz.

print( total ["Pancar"])