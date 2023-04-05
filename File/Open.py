# open("bilgiler.txt","w") # open fonksiyonu dosya açmamıza yarar dosya_adı ve erişme_kipi diye sırayla yazılır 'w' dosyayı açıp yazmak için kullanılır.
"""
r modu Dosyayı Okur dosya yoksa hata verir - FileNotFoundError
w modu Yazma modu Dosyo yoksa oluşturur
r+ modu hem okuma hem yazma modu
a modu dosyanın sonuna ekleme
b modu binary mode
bunların hepsi erişim kipi kısmında yazılır



"""
# file = open("bilgiler.txt","w") # Bu şekilde file ismi altında dosya işlemlerini yapabiliriz
# file.close() # Bu fonksiyonu kullanarak dosyayı kapatırız. Eğer kapatılmazsa açık kalıp hataya yol açabilir.

# Dosyayı istediğimiz bir kısıma açmak istersek de aşağıdaki gibi kullanıyoruz.
file = open("C:/Users/user/Desktop/week 2/bilgiler.txt","w") # Dosya konumlarını sırayla yazarak açabiliriz

file.write("Aytekin Can Ş") # Yazmak istediğimiz şeyi gireriz.
# Dosya içi yazı yazmada türkçe veya başka harfler kullanıldığında sorun çıkarırsa açtığımız dosya içine erişme kipinden sonra - encoding = "utf-8"- yazarız
file.close()

file = open("C:/Users/user/Desktop/week 2/bilgiler.txt","a")
file.write("Aytekin cann")
file.close()
# Alt satıra yazmak için dosyalarda da geçerli olan \n karakterini kullanırız.
file = open("C:/Users/user/Desktop/week 2/bilgiler.txt","a")
file.write("Python\n") # Bu şekilde sonuna bırakırsak bir sonraki yazıda alt satıra geçer
file.write("Programlama")
file.close()

file = open("C:/Users/user/Desktop/week 2/bilgiler.txt","r")
for i in file:  # For döngüsü kullanarak dosyayı okuyabiliriz.
    print(i, end = "") # Ekstra satır koymaması içine sonuna end kullanarak hiçbir şey koyma diye belirtiriz.



icerik = file.read() # Read fonksiyonunu kullanarak bütün dosyayı okuyabiliriz
print(icerik)
print(file.readline()) # Buradaki fonksiyon sadece bir satırı okur sonrasında okuduğu satırı atlayarak devam eder

liste = file.readlines()
print(liste)
file.close()
# readlines fonksiyonu ise içerisindeki herbir satırı listeye atar