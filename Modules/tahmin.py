import random
import time

print('''***********************************

Sayı Tahmin Etme Programı

1 ile 40 arasında sayı tahmin edin.

**********************************''')

random_number = random.randint(1, 40)  # Bize 1 ile 40 arasında rastgele bir sayı vermesini sağlar.
tahmin_hakkı = 7

while True:
    tahmin = int ( input("Tahmininiz : ") )
    print("Tahmin Hakkınız = ", tahmin_hakkı )

    if ( tahmin < random_number ):
        print("Bilgiler Kontrol Ediliyor...")
        time.sleep(2) # Bu fonksiyonu  kullanarak programı yazdığımız saniye kadar durdurmuş oluruz.

        print("Daha yüksek bir sayı söyleyin...")
        tahmin_hakkı -= 1
        print("Tahmin hakkınız = " , tahmin_hakkı )

    elif ( tahmin > random_number ) :
        print("Bilgiler Kontrol Ediliyor...")
        time.sleep(2)

        print("Daha küçük bir sayı söyleyin...")
        tahmin_hakkı -= 1
        print("Tahmin hakkınız = ", tahmin_hakkı )

    else :
        print("Bilgiler kontrol ediliyor...")
        time.sleep(2)
        print("Tebrikler! Sayımız = ", random_number )
        break

    if ( tahmin_hakkı == 0 ) :
        print("Tahmin hakkınız bitti :( ")
        print("Sayımız = ", random_number )
        break
