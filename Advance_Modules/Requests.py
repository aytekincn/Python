# Requests internetten veri çekmemize yardımcı olur.
import requests # Web sayfasından bilgileri requests ile çekicez.

from bs4 import BeautifulSoup # Web sitesinin içindeki bilgilerini de BeautifulSoupile çekicez.

url = "https://www.kap.org.tr/tr/bist-sirketler"  # Site url'mizi bir değişkene atadık.

response = requests.get( url ) # response değişkeni içine de sayfa bilgilerini get fonksiyonu ile alıyoruz.

# print( response )

html_icerigi = response.content # Bunu yazdığımızda web sayfasının html dökümanını bize verir.

soup = BeautifulSoup( html_icerigi, "html.parser") #  İçerideki bilgileri almak için BeautifulSoup kullanırız bilgileri parçalamak için de parser kullanırız.

# print( soup.prettify() ) # Dökümanı güzel bir şekilde görüntülemek için prettify fonksiyonunu kullanıyoruz.

"""
for i in soup.find_all("a"): # for döngüsü kullanarak a etiketleri bulunan kısımları alıyoruz.
    print( i.get("href") )  # burada ekran bastırdığımız kısımda ise href geçen yani linklerin olduğu kısımları ekliyoruz sadece.
    print("*******************************************************")
"""

for i in soup.find_all("a"):
    print( i.text ) # a etiketlerinin içindeki sadece yazıları almak için kullanırız.
    print("*******************************************************")

# print (soup.find_all ("div", {"class":"yp-poi-box-2"))) bir bloktaki classı almak için ekstra sözlük içinde yazarız class ve key value kısmını yazarak.


































