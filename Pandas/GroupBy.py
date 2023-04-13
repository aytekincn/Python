# Bir grubun içindeki verilere erişmek için kullanılır sql  sorgusuna benzerdir.
import numpy as np
import pandas as pd
dataset = {
        "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
        "Çalışan": ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
        "Maaş":[3000,3500,2500,4500,4000,2000]
        }

df = pd.DataFrame( dataset )

print( df )


DepGroup = df.groupby("Departman") # Departmana göre groupby işlemi. Bu groupby işleminde departman üzerinde sorgularımızı yaparız.

print ( DepGroup.sum() ) # Departmanlarına göre kişilerin toplam maaşlarını görmüş oluruz.

print ( df.groupby("Departman").sum() ) # Bu şekilde tek satırda da sorgumuzu yazabiliriz.


print ( df.groupby("Departman").sum().loc["Bilişim"] ) # Indeksteki değeri almak için .loc kullanırız. Sorgunun başına int ekleyerek sorgumuzu sadece int değer döndürebiliriz.


print( df.groupby("Departman").count() ) # Gruplara göre kaç kişi olduğunu sayar.

print( df.groupby("Departman").max() ) # En yüksek maaş olan değeri döndürür str değerlerde de alfabetik sıraya göre sıralar. Aynı şekilde min de kullanabiliriz.

print( df.groupby("Departman").min()["Maaş"] ) # İstediğimiz sütunu almak için column kısmını köşeli parantez ile yazarız. Belirli bir indeksteki değeri almak için de köşeli parantezle indeks ismini yazarız.

# .mean kullanarak ortalamalarını alabiliriz.# .mean kullanarak ortalamalarını alabiliriz. Yine köşeli parantez kullanarak spesifik sorgu gerçekleştireiliriz.



























