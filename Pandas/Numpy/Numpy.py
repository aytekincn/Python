import numpy as np  # Numpy paketini np ismi ile kullanıyoruz.

data_list = [ 1, 2, 3, 4, 5] # Basit bir liste oluşturuyoruz.

arr = np.array( data_list ) # arr değişkeninde elimizdeki listeyi np.array yaparak data olarak atıyoruz

a = np.arange( 10, 20, 2 ) # Tıpkı range fonksiyonundaki değer aralığı verebiliriz.

print( a )

np.zeros( 10 ) # burada arraylerin her elemanın sıfır olur 10 tane sıfır eleman yazdırır.

np.ones(4) # Burada da aynı şekilde her bir değer 1 olur numpy daha doğru sonuçlar almak için int değerleri floata çevirip alır.

np.zeros( (3,4)) # Üçe dörtlük bir matris oluşturur burada 3 tane liste içine 4 tane sıfır değeri atar. ones kullanarak da aynısı yapılır

np.linspace( 0, 100 , 5 ) # Burada 0 ile 100 arasındaki değerleri 5 parçaya böleriz. 0 ile 100 dahil olur.
b = np.linspace (0 , 1, 6 ) # 0 ile 1 i 6 parçaya böleriz 0.2, 0.4 şeklinde değer verir.
print( b )

c = np.eye(6) # Burada 6 ya 6 bir matris oluşturur köşegenlere de 1 değerini verir.
print( c )

np.random.randint( 15 ) # 0 ile 15 arasında ( 15 dahil değil ) random değer döndürür.

np.random.randint( 1, 10, 5 ) # 1 ile 10 arasında 5 tane değer üretir.

np.random.rand( 5 ) # 0 ile 1 arasında 5 tane değeri depolayan array döndürür.

np.random.randn( 5 ) # Hem eksi hem artı değerlerimiz oluşur.

arr3 = np.arange( 25 ) # 0 dan 25 e kadar olan bir array oluştururuz bunları 5 e 5 lik bir matris içine atmak istersek
print( arr3 )

arr3.reshape(5,5) # Ancak burada değerlerin tam şekilde oluşması lazım 4, 5 olursa mesala burada hata verir

print( arr3 )

print( arr3.max() ) # Array içindeki en büyük değeri gösteririr aynı şekilde min kullanımı da en küçük olanı. arr3.sum() kullanarak da hepsinin toplamını alabiliriz. Ortalaması için .mean.

print( arr3.argmax() ) # En büyük değerin olduğu indeksi verir. Min de aynı şekilde en küçüğü verir.