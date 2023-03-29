# Verdiğimiz aralıklara göre sayı dizisi oluşturur. Herhangi bir başlangıç değeri vermezsek de otomatik 0 dan başlar.
# GÖrmek için başına * ekleriz gideceği kadarki sayıyı dahil etmez
# print ( * range ( 0, 20 ) )
# print ( * range ( 1, 100, 2 ) ) 1 den 100 e kadar 2 atlayarak git
# print ( * range ( 20, 0, -1 ) ) bu şekilde çoktan aza doğru sıralanır -1 şeklinde bir değer vermezsek otomatik olarak artırma yaptığı için herhangi bir değer döndürmez.

for i in range ( 1, 20 ) :
    print ("* " * i )