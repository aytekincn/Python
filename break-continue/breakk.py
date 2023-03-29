# Döngü herhangi bir yerde -break- ifadesiyle karşılaştığı zaman çalışmayı durdurur. Döngü sonlanır ancak iç içe döngüde kullanılmışsa kullanıldığı kısımı durdurur.

"""
while True:
    isim = input ("isminizi girin :")
    if ( isim == "q"):
        print ( "Programdan çıkılıyor")
        break
    print("İsminiz : " , isim)
"""
i = 0
while ( i < 10 ) :
     if ( i == 5 ) :
         break   #Yanına herhangi bir noktalama vs gelmeden bu şekilde kullanılır.
     i += 1
     print ( i )
