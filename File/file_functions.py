# Dosyaları kendimiz kapatmak yerine with open fonksiyonunu kullanırız blok bitince otomatik olarak kendisi kapatır dosyayı.

with open("C:/Users/user/Desktop/week 2/Çalışma2.txt", "r", encoding = "utf-8") as file: # Bu şekilde sonuna dosya değişken ismi vererek yapabiliriz.
    for i in file:
        print(i, end = "")
# Buradaki bloklar bittiği için kendisi dosyayı kapattı close yazmamıza gerek  kalmadı.

with open("C:/Users/user/Desktop/week 2/Çalışma2.txt", "r", encoding = "utf-8") as file:
    file.seek(3)# Burada imleci  istediğimiz indekse götürürüz. 0 dan başlayıp satırların en başından.
    print(file.tell()) # Gidildiği kısmı gösterir.
    bilgi = file.read(10) # 3.indeksten başlatıp 10 a kadar götürdük.
    print(bilgi)


with open("C:/Users/user/Desktop/week 2/Çalışma2.txt", "a", encoding = "utf-8") as file:
    file.write("Mert Söylemez")

with open("C:/Users/user/Desktop/week 2/Çalışma2.txt", "r", encoding = "utf-8") as file:
    print(file.read())