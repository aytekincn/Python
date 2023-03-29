# Döngü herhangi bir yerde continue ifadesiyle karşılaştığında geri kalan işlemleri yapmadan direkt bloğun başına döner.

liste = list(range(11))
for i in liste :
    if( i == 2  ):
        continue

print ("i : " , i)