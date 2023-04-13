# Concatenate iki tane dataframemizi sıralı bir şekilde birleştirmemizi sağlar.
import numpy as np
import pandas as pd
dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
    "C":["C1","C2","C3","C4"],
}

dataset2 = {
    "A": ["A5","A6","A7","A8"],
    "B":["B5","B6","B7","B8"],
    "C":["C5","C6","C7","C8"],
}

df1 = pd.DataFrame( dataset1 , index = [1,2,3,4])
df2 = pd.DataFrame( dataset2, index = [5,6,7,8])

data_frame = pd.concat( [ df1, df2 ] ) # concat kullanarak axisine göre aşağı veya yana doğru birleştirebiliriz. Köşeli parantez içine yazılır

print( data_frame )

# df1.join( df2 ) işlemi bize left join sonucunu verir.

#------------------MERGE-----------------------

dataset3 = {
    "A" : ["A1","A2","A3"],
    "B" : ["B1","B2","B3"],
    "anahtar" : ["K1","K2","K3"]
}

df3 = pd.DataFrame(dataset3,index = [1,2,3])

dataset4 = {
    "X" : ["X1","X2","X3","X4"],
    "Y" : ["Y1","Y2","Y3","Y4"],
    "anahtar" : ["K1","K2","K5","K4"]
}

df4 = pd.DataFrame(dataset4,index = [1,2,3,4])

# Merge sadece ortak kısımları alır datalarımızı birleştirir. SQL deki inner join ile benzerdir.

# join indeksler üzerinden gerçekleştirir merge ise sütunlar üzerinden işlemleri gerçekleştirir.

ab = pd.merge( df3,  df4, how = "inner") # inner yapmak istediğimiz framelerimizi gireriz ve how = ekleyerek hangi işlemi gerçekleştirmek istediğimizi söyleriz. left right da söylenebilir joinden daha pratik.

print( ab )
