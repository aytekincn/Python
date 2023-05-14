import sys


print( dir(sys))

a = int(input("a: ") )
b = int(input("b: ") )

sys.exit() # Bunun altındaki hiçbir fonksiyon kullanılmaz program direkt sona erer.

c = int(input("c:") )


# Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.
# stdin : Bu standard dosya, işlemimizin kullanıcan input almasını sağlar.
# stdout : Bu standart dosya, işlemimizin çıktı vermesini sağlar.
# stderr : Bu standart dosya, işlemimizin hata mesajlarını çıktı olarak vermemizi sağlar.


sys.stderr.write("Bu bi hata mesajıdır.\n") # Bu şekilde bir hata mesajı yazdırabiliriz. Kırmızı bir şekilde yazılır.
sys.stderr.flush()

sys.stdout.write("Bu normal bir mesajdır.\n")









