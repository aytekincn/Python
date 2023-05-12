# Iteratorler bizim listeler üzerinde gezinmemizi sağlar

liste = [1, 2, 3, 4, 5 ]

iterator = iter( liste )

print( next(iterator) ) # Buradaki nexti kullanarak lsitemiz üzerinde gezinmiş oluruz sırasıyla bize listedeki elemanları gösterir.

print( next(iterator) ) # Bu şekilde liste üzerinde gezeriz gösterilecek eleman bittiğinde ise StopIteration hatası alırız.

# Iteratorlar bizim görmediğimiz ancak kullanılan fonksiyonlardır. For döngüsü ile liste üzerinde gezinirken biz görmesek bile python kendisi iterator kullanır.

while True:
    try:
        print( next( iterator ) )  # Burada yaptığımız işlem de kendi içerisinde bir for döngüsü.
    except StopIteration:
        break


class Kumanda():
    def __init__(self, kanal_listesi ):
        self.kanal_listesi = kanal_listesi
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if ( self.index < len ( self.kanal_listesi ) ) :
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda( ["Atv, TRT, Kanal D, TV8, Show TV, Star " ] )

iterator1 = iter( kumanda )

print( next( iterator1 ) ) # Burada sırasıyla kanallar üzerinde gezinmiş oluruz.




