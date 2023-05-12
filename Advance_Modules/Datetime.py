from datetime import datetime
import locale # Konumu değiştirmek için kullanırız.

locale.setlocale(  locale.LC_ALL, "") # Burada konumumuza bakıp Türkçeye çevirmemize yarar.

print( datetime.now()) # Anlık zamanı görmek için kullanılır.

şu_an = datetime.now()

print( şu_an.year )
print( şu_an.month ) # O anki zamnın gün, ay, yıl, saat gibi verilerini almak için kullanılır.
print( şu_an.hour )


print( datetime.ctime( şu_an ) ) # Datetime ile ctime kullanıp içine değişkeni verdiğimiz şu an fonksiyonu ile daha güzel bi tarih saat görüntüsü alırız.

print( datetime.strftime( şu_an, "%Y %B") ) # Sadece ay, yıl, gün, saat gibi belirli bir kısmı almak için kullanılır. Yan yana  istediğimiz zamanları yazarız.
# Yıl için %Y, Ay için %B, Gün için %A, Saat için %X, Gün için de %D kullanılır.

# Epoch zamanı 1970 den başlar.

tarih = datetime( 2000, 6, 25 ) # İki tarih arasındaki farkı bulmak için kullanılan yöntem.

print( şu_an - tarih )





















