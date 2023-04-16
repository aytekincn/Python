import numpy as np
import pandas as pd
df = pd.DataFrame({
    "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})


print( df["Column2"].unique() ) # Tekrar eden değerleri filtreleyip almak istediğimiz yerin değerlerini döndürür. unique olan değerleri verir başına nunique getirirsek de kaç tane olduğunu bize gösterir.

print( df["Column2"].value_counts() ) # Bir değerden kaç tane olduğunu bize gösterir.


print( df[ ( df["Column1"] >= 4 )  & ( df["Column2"] == 300  ) ]  ) # Burada datalar içindeki verileri filtleyerek sorgu yapabiliriz.

# Bir data içinde sütunlara çeşitli fonksiyonları gönderebiliriz.
def times3( a ):
    return a * 3

print( df["Column2"].apply(times3)) # Bu şekilde oluşturduğumuz fonksiyonu datamızın içine uygulayabiliriz. Pandas otomatik olarak değerleri gönderdiği için değer vermiyoruz

df["Column2"] = df["Column2"].apply(times3) # column2 ile fonksiyonlu yazdığımız kısmı eşitlersek yaptığımız işlemi kaydetmiş oluruz.

print( df )

df["Column2"] = df["Column2"].apply( lambda x : x + 100 ) # apply içine lambda kullanarak daha kısa bir şekilde işlemleri gerçekleştirebiliriz. Fonksiyon oluşturmaya gerek kalmaz.

print( df )

print( df["Column3"].apply( len) ) # Pythonun kendi içindeki fonksiyonlarını kullanabiliriz.


# df.columns bize kaç tane sütun olduğunu gösterir. df.index ise kaç tan index olduğunu gösterir

print( df.sort_values("Column2", ascending= False ) ) # sort_values istediğimiz sütunu küçükten büyüğe sıralamaya yardım eder ascending değerini True False olarak değiştirebiliriz default True.

df2 = pd.DataFrame({
    "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem":[10,25,50,21,67,80,30,70,75]
})

print( df2 )

print ( df2.pivot_table(index = "Ay", columns = "Şehir", values = "Nem") ) # Pivot tablo oluştururuz tablonun indeks, sütun ve satır verilerinin isimlerini değiştirip daha düzgün bir tablo haline getirebiliriz.


print ( df2.pivot_table(index = "Şehir", columns = "Ay", values = "Nem") ) # Spesifik bir data için indks ve sütun yerlerine bilgileri yazıp tablo oluşturabiliriz.

dataset =  pd.read_csv('C:/Users/user/Desktop/SQL/USvideos.csv') # pandas değişkeni pd.read_"hangi dosya biçimi ise" yazılıp data okunur datayı direkt dosya ismi ile alamazsanız dosya konumunu yazarak alabilirsiniz.

print( dataset )

new_data1 = dataset.drop(["video_id","trending_date"], axis= 1 )

print( new_data1 )

# new_data1.to_csv("NewUsVideos1.csv", index= False ) # İndeksleri almak istemezsek indeks değerini false yapabiliriz.

# Aynı şekilde excel gibi diğer dosya türünde de okuma yapılabilir.

new = pd.read_html("https://www.contextures.com/xlsampledata01.html", header= 0) # Burada header kısmında 0 indeksinde olan değerleri aldığımız datadaki gibi başlıklar olarak atayabiliriz.

print(  len(new ) )

print( new)


