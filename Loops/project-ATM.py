print("""
*********************************    
ATM Programı
********************************* 
İşlemler ;
    1.İşlem Bakiye Sorgulama
    2.İşlem Para Yatırma
    3.İşlem Para Çekme 
    Programdan çıkmak için 'q' ya basın. 
      """)

bakiye = 1000

while True :
    islem = input("Lütfen Yapmak İstediğiniz İşlemi Seçin : ")

    if ( islem == "q" ) :
        print("ATM den çıkılıyor...")
        break

    elif ( islem == "1" ) :
        print("Bakiyeniz {} ' tl dir. ".format( bakiye ) )


    elif ( islem == "2") :
        miktar = int ( input("Yatırmak istediğiniz miktarı girin : " ) )
        print(" {} 'tl hesabınıza yatırılıyor... ".format( miktar ) )
        bakiye += miktar
        print("Yeni bakiyeniz : ", bakiye )

    elif ( islem == "3" ) :
        miktar = int ( input("Çekmek istediğiniz miktarı girin :") )
        if ( bakiye - miktar < 0 ) :
            print("Bakiyeniz yetersiz...")
            continue

        bakiye -= miktar
        print("Kalan bakiyeniz : " , bakiye )

    else :
        print("Geçersiz işlem")


























































