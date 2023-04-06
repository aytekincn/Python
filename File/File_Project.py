def not_Hesapla(satır):

    satır = satır[:-1]
    liste = satır.split(",")
    isim =  liste[0]
    not1 = int ( liste[1] )
    not2 = int ( liste[2] )


    final_not = not1 * ( 4 / 10 ) + not2 *  ( 6 / 10 )

    if ( final_not >= 90 ):
        harf =  "AA"
    elif ( final_not >= 80 ):
        harf =  "BB"
    elif ( final_not >= 70 ):
        harf = "CC"
    elif ( final_not >= 60 ):
        harf =  "DC"
    elif ( final_not >= 50 ):
        harf =  "DD"
    else:
        harf =  "FF"
    return isim + "-------------> " + harf + "\n"







with open("C:/Users/user/Desktop/week 2/Çalışma2.txt", "r", encoding = "utf-8") as file:
    eklenecekler = []

    for i in file:
        eklenecekler.append(not_Hesapla(i))
    print(eklenecekler)

