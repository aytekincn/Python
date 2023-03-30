# Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objeler özgü fonksiyonlardır.
# Örneğin obje.herhangi_bir_metod(değerler(opsiyonel))

a = [1,2,3,4,5]
a.insert( 0,"Aytekin") # Buradaki insert metoddur listeye ekleneceği indeksi belirleyip eklemek istediğiniz şeyi ekler.
print( a )
a.append("dsf")
print( a )
a.pop()
print( a )
help( a.pop ) # Help metodun ne işlem yaptığını göstermeye yarayan bir yazı çıkarır.