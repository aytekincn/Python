import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get( url )

html_icerigi = response.content

soup = BeautifulSoup( html_icerigi, "html.parser")

"""for i in  soup.find_all ("td", {"class":"titleColumn"} ) :
    print( i.text )        - BU KISIMI DAHA DA PRATİK HALE GETİREBİLİRİZ.
    print("***********************************************************")
"""
a = float( input("Rating' i giriniz : ") )



basliklar = soup.find_all ("td", {"class":"titleColumn"} )
ratingler = soup.find_all("td", {"class":"ratingColumn imdbRating"} )

print( len( basliklar), len( ratingler ) )

# İki tane listemizi zip fonksiyonu ile birleştirip isimlere karşı gelen ratingleri birleştirebiliriz.

for baslik, rating in zip( basliklar, ratingler ): # Buradaki zip fonksiyonu iki tane listeyi bize birleştirecek.
    rating = rating.text
    baslik = baslik.text

    baslik = baslik.strip() # Buradaki strip fonksiyonu baştaki ve sondaki boşlukları siler ve daha güzel bir görüntü sağlar.
    baslik = baslik.replace("\n", " ")

    rating = rating.strip()
    rating = rating.replace("\n", " ")

    if ( float( rating) > a ):
        print("Film ismi : {}  Filmin Ratingi {} ".format( baslik, rating ) ) # Sadece kullanıcının girdiği değerden yukarı olan filmleri yazdırmış oluruz.

    # Yukarıda yaptığımız işlem daha düzenli bir görüntü sağlar.