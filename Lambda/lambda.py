# Fonksiyonları tek satırda oluşturmaya yarar. Gerekilen yerlerde kullanılabilir. Uzun fonksiyonlar hariç aşağıdaki gibi kısa fonksiyonlarda.
# Yapısı =>  etiket = lambda parametre1, parametre2.... : işlem  şeklinde olur

def ikiylecarp (x) :
    return x * 2
# Üstteki fonksiyonu daha kısa yazmak için

ikiyleçarp = lambda x : x * 2

print(ikiyleçarp(3))

def toplama (x, y, z) :
    return x + y + z

print(toplama(23,45,67))

toplama = lambda x,y,z : x + y + z  # Bu şekilde daha pratik bir biçimde yazılır.

print(toplama(12,45,66))

def terscevir ( s ) :
    return s [::-1]

print(terscevir("Aytekin"))


terscevir = lambda s : s[::-1]

print(terscevir("Python Programlama"))


def ciftek ( sayi ) :
    return sayi % 2 == 0

print( ciftek (44) )

cifttek = lambda sayi : sayi % 2 == 0

print( cifttek (65) )











