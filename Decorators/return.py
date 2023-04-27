
def anafonksiyon ( işlem_adı ):

    def toplama ( *args ):
        toplam = 0
        for i in args:
            toplam += i
        return print( toplam )
    def çarpım ( *args ):
        çarpım = 1
        for i in args:
            çarpım *= i
        return print( çarpım )

    if ( işlem_adı == "toplama") :
        return toplama
    else:
        return çarpım


fonk = anafonksiyon("toplama") # return yardımıyla fonksiyon döndürdük bunu da bir tane fonksiyona eşitledik.

fonk(1,2,3,4,5)

fonk2 = anafonksiyon("çarpım")

fonk2(2,3,4,5,6)



def toplama( a, b ):
    return a + b
def çıkarma( a, b):
    return a - b
def çarpma( a, b ):
    return a * b
def bölme( a, b ):
    return a / b

def mainfunction( funct1, funct2, funct3, funct4, işlem_adı ):

    if ( işlem_adı == "toplama" ):
        print( funct1( 3, 4 ) )
    elif ( işlem_adı == "çıkarma" ):
        print( funct2( 10, 4 ) )
    elif (işlem_adı == "çarpma"):
        print(funct3( 8, 4 ) )
    elif ( işlem_adı == "bölme" ):
        print( funct4( 40, 4 ) )
    else:
        print("Geçersiz İşlem")

mainfunction( toplama, çıkarma, çarpma, bölme, "toplama") # Burada parametrelerimizi eşitliyoruz ana fonksiyonumuz ile sonrasında işlem adını girip fonksiyonu döndürüyoruz.
mainfunction( toplama, çıkarma, çarpma, bölme, "çıkarma")
mainfunction( toplama, çıkarma, çarpma, bölme, "çarpma")
mainfunction( toplama, çıkarma, çarpma, bölme, "bölme")




















