import pandas as pd

soccer = pd.read_csv("C:/Users/user/Desktop/SQL/mls-salaries-2017.csv")

print( soccer )

print( soccer.head( n = 10 ) ) # İlk 10 veriyi getirir.

print( len(soccer.index ) ) # Kaç tane verimizin olduğunu buluruz.

print( soccer["base_salary"].mean() ) # Maaşlarının ortalamasını alırız.

print( soccer["base_salary"].max() ) # En yüksek maaşı buluruz.

print( soccer[soccer["guaranteed_compensation"]  == soccer["guaranteed_compensation"].max() ]["last_name"].iloc[ 0 ] ) # En yüksek tazminata sahip oyuncunun soyadını buluruz. En sondaki last name kısmını çıkartırsak genel olarak bilgilerini almış oluruz.
# Direkt istediğimiz kısmı almak için de iloc kullanırızç

print( soccer [ soccer["last_name"]   == "Gonzalez Pirez" ]["position"].iloc[ 0 ] ) # Spesifik olarak istediğimiz oyuncuyu soyadı ile hangi pozisyonda oynadığını bulduk.

print(  ( soccer.groupby("position").mean( str ) ) ) # Pozisyonlarına göre ortalama maaşlarını bulduk "TypeError: can only concatenate str (not "int") to str" hatası ile karşılaşılması durumunda
# Outputu str e çevirebiliriz aldığımız outputlar mean yardımıyla geldiği için mean ( str ) kullanırız.

print( soccer["position"].nunique() ) # Kaç tane pozisyon olduğunu bulabiliriz.

print( soccer["position"].value_counts() ) # Her mevkide kaç tane oyuncu olduğunu bulabiliriz. Aynı şekilde diğer kategorilere göre de uygulayabiliriz. "soccer["club"].value_counts() gibi.

# Soyadının içinde -son- geçen futbolcuları bulacağız. Öncelikle bir tane fonksiyon yazıyoruz.

def son_find (last_name):
    if "son" in last_name.lower(): # Aradığımız kelime büyük de olabileceği için hepsini küçük yaparız.
        return True
    else:
        return False

print( soccer[soccer["last_name"].apply( son_find ) ]   )
