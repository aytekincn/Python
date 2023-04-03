# Kendi veri tiplerimizi  oluşturmak ve bu veri tiplerinden objeler üretmemiz için önce objeleri üreteceğimiz yapıları oluşturmamız lazım bunlara da class diyoruz.
# Classlar objelerimizi oluştururken objelerin özelliklerini ve metodlarını tanımladığımız bir yapıdır.

class Araba():   # Bu şekilde sınıfımızı (class) oluşuturuyoruz ve içine özellikler ekliyoruz.
    marka = "Bentley"
    model = "Continental"
    beygir_gucu = "550"
    motor = "V12"

araba1 = Araba() # Objeyi classdan üretmek için bu yöntemi kullanırız. Objenin ismi ve veri tipini gireriz veri tipimiz burada class ismi olur.

print( araba1.marka )  # Objelere erişmek için verdiğimiz ismi kullanarak . fonksiyonunu kullanırız.
print(Araba.model)  # Özelliklere erişmek için class ismini de kullanabiliriz.
