import random
import time


class Kumanda () :

    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["TRT"], kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if ( self.tv_durum == "Açık"):
            print("Televizyon zaten açık")
        else :
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if ( self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı.")

        else :
            print("Televizyon kapatılıyor...")
            self.tv_durum = "Kapalı"


    def ses_ayari(self):
        while True:
            cevap = input("Sesi Azalt : '<'\n Sesi Artır : '>'\n Çıkış : 'çıkış' ")

            if ( cevap == "<" ):
                if ( self.tv_ses != 0 ):
                    self.tv_ses -= 1
                    print("Ses : ", self.tv_ses )
            elif ( cevap == ">" ):
                if ( self.tv_ses != 30 ):
                    self.tv_ses += 1
                    print("Ses : ", self.tv_ses )

            else :
                print("Ses Güncellendi : ", self.tv_ses )
                break


    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append( kanal_ismi )

        print("Kanal Eklendi.")


    def rastgele_kanal(self):
        rastgele = random.randint(0, len (self.kanal_listesi ) -1 ) # Kanal listesi arasından en baştan sona index numarası şeklinde rastgele kanal vermesi.

        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal : ", self.kanal )

    def __len__(self):
        return len ( self.kanal_listesi )

    def __str__(self):
        return "Tv Durumu : {}\n Tv Ses : {}\n Kanal Listesi : {}\n Şimdiki Kanal : {}\n" .format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal )




print("""******************************

Tv Kumanda Programı

1.Tv Aç
2.Tv Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısı Öğrenme
6.Ratgele Kanal Seç
7.Televizyon Bilgileri

Çıkmak için 'Q'


**********************************""")

kumanda = Kumanda()



while True:
    islem = input("Lütfen İşlemi Seçiniz : ")

    if ( islem == "q" ):
        print("Program Sonlanıyor..")
        break

    elif ( islem == "1" ):
        kumanda.tv_ac()
    elif ( islem == "2" ):
        kumanda.tv_kapat()

    elif ( islem == "3" ):
        kumanda.ses_ayari()

    elif ( islem == "4" ):
        kanal_islemleri = input("Kanal isimlerini ',' ile ayırarak giriniz : ")

        kanal_listesi = kanal_islemleri.split(",")
        for eklenecekler in kanal_listesi :
            kumanda.kanal_ekle(eklenecekler)

    elif ( islem == "5"):
        print("Kanal Sayısı : ", len(kumanda) )

    elif ( islem == "6" ):
        kumanda.rastgele_kanal()
    elif ( islem == "7" ):
        print(kumanda)

    else :
        print("Gçersiz İşlem.")

















