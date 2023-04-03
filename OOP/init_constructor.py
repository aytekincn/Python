# init methodu yapıcı ( constructor ) fonksiyon olarak tanımlanmaktadır. Bu method objeleri oluştururken ilk çağırılan fonksiyondur.

"""
class Araba():
    marka = "Bentley"
    model = "Continental"
    beygir_gucu = "550"
    motor = "V12"
    def __int__(self):  # Buradaki self kelimesi objeyi oluşturduğumuz zaman o objeyi gösteren referanstır ve metodlarda en başta bulunması gereken parametredir.
        # Self parametresi otomatik olarak gönderilir ekstra yollamaya gerek yok.
        print("Fonksiyon çağırıldı")


araba1 = Araba()

"""

class Araba():
    def __init__(self, marka, model, beygir_gucu, motor):
        print("init fonksiyonu") # Otomatik çağırılan değer.
        self.marka = marka # Bunun anlamı kullanıcı bu özelliğe değer girecek biz de bunu özelliğe yüklüyoruz anlamı taşır.
        self.model = model
        self.beygir_gucu = beygir_gucu
        self.motor = motor


araba1 = Araba("Volkswagen", "Passat", 120, 1.6) # Objelerin özelliklerine değerleri sıralı bir şekilde direkt olarak atarız.
print(araba1.marka)
print(araba1.model)
print(araba1.beygir_gucu)



araba2 = Araba("Skoda", "Superb", 200, 2.0 ) # Class içinde oluşturduğumuz özellikler genel olduğu için başka bir obje tanımlayıp içine değerler atayabiliriz.
# Classların içine varsayılan değerler de atayabiliriz classı oluştururken  def __init__(self, marka = "Bilgi Yok", model, motor = "Bilinmiyor" ) gibi .
# Gönderdiğimiz değer varsayılan değer yerini alır ve o şekilde çıktı verir.







