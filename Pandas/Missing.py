import numpy as np
import pandas as pd

arr = np.array( [ [10, 20, np.nan ], [3, 5, np.nan ],  [21, np.nan, 34 ]  ] )

df = pd.DataFrame( arr, index = ["Index1", "Index2", "Index3"], columns= ["Column1", "Column2", "Column3"] )

print( df )

print( df.dropna() ) # Bu şekilde nan olan değerleri silmeye çalıştığımızda nan bulunan bütün satırları siler axi 0 olduğu için

print( df.dropna( axis = 1) ) # Axisini değiştirdiğimizde nan olmayan sütunları alır.

print( df.dropna( thresh= 2 ) ) # Buradaki thresh ve verdiğimiz sayı minimum 2 tane nan olmayan değer varsa onları getirir.

df.sum() # Burada sütunlardaki değerleri toplar.

print ( df.fillna( value= "Bilgi yok") )  # nan kısımlara bir değer atayabiliriz.

# Kaç tane verimizin olduğunu bulmak için df.size kullanırız. df.isnull().sum bir tane sütunda kaç tane nan değer olup olmadığını görürüz tam sayısı için bir tane daha .sum ekleriz.

def calculateMean ( df ):  # Datamızdaki verilerin ortalamalarını hesplayan bir fonksiyon
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum

print( df.fillna( value = calculateMean( df ), inplace= True ) ) # nan değerlerin yerinde koyacağımız için fillna ardından value yerine de fonksiyonumuzu yazarız.

print( df )







