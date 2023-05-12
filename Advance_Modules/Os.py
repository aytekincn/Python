# Os modülü Python'da hazır olarak gelen , dosya ve dizinlerde kolaylıkla işlemler yapmamızı sağlayan bir modüldür.
import os
from datetime import datetime
#os.chdir("C:\Users\user\Desktop\SQL") # Bulunduğumuz dizini değiştirebiliriz.
print ( os.getcwd() ) # Hangi klasörde olduğumuzu gösterir.


for i in os.listdir(): # Dosyalarımızı gösterir bulunduğumuz dizinde.
    print( i )

#os.mkdir("Deneme") # Bizim bulunduğumuz klasör altına bir tane daha klasör oluşturur. os.makedirs("Deneme1/Deneme2") bu şekilde yaptığımızda sırayla alt alta klasörlerimizi oluşturur.

# os.rmdir("Deneme1/Deneme2") bu metod deneme1 altındaki deneme2 klasörünü silmeye yarar.
# os.removedirs("Deneme1/Deneme2") her iki klasörü de siler
# os.rename("Os.py", "Os.py")  Klasörümüzün ismi değişir.

# print( os.stat("test.txt") ) klasörün bütün özelliklerini.
print ( datetime.fromtimestamp (os.stat ("test.txt") . st_mtime) ) # Klasörde yapılan değişikliğin zamanını gösterir.









































