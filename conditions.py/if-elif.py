'''
yas = int ( input ("Lütfen yaşınızı giriniz :  "))
if ( yas < 18 ) :
    print ("Bu mekana giremezsınız...")
else :
    print ("Mekana girebilirsiniz.")
  '''

'''
note = float ( input ("Lütfen notunuzu giriniz : "))
if ( note >= 90 ):
    print ("Harf notunuz AA ")
elif ( note >= 85 ) :
    print ("Harf notunuz BA ")
elif ( note >= 80) :
    print ("Harf notunuz BB")
elif ( note >= 75) :
    print ("Harf notunuz BC")
elif ( note >= 65) :
    print ("Harf notunuz CC")
elif ( note >= 50) :
    print ("Harf notunuz DC")
else :
    print ("Harf notunuz FF dir ")
    '''
'''
print (""""
       ************************
       Hesap Makinesi

       1. Toplama İşlemi
       2. Çıkarma İşlemi
       3. Çarpma İşlemi 
       4. Bölme işlemi 
       **************************""")

islem = input ("Yapmak istediğiniz işlemi seçin..")
a = int ( input ("Birinci sayıyı giriniz :"))
b = int ( input ("İkinci sayıyı giriniz :"))

if ( islem == "1"):
    print (" {} sayısı ile {} sayısının toplamı = {}' dir " .format (a, b, a + b ) )
if ( islem == "2") :
    print (" {} sayısı ile {} sayısının farkı = {}' dir " .format (a, b, a - b ) )
if ( islem == "3") :
    print (" {} sayısı ile {} sayısının çarpımı = {}' dir " .format (a, b, a * b ) )
if ( islem == "4") :
    print (" {} sayısı ile {} sayısının bölümü = {}' dir " .format (a, b, a / b ) )
else :
    print ("Geçersiz işlem..")
'''
'''
sys_kullanici_adi = "aytekincn"
sys_sifre = "1234567"

kullanici_adi = input ("Kullanıcı adını giriniz : ")
sifre = input ("Şifreyi giriniz : ")

if ( sys_kullanici_adi == kullanici_adi and sys_sifre != sifre ):
    print ("Hatalı şifre...")
elif ( sys_kullanici_adi != kullanici_adi and sys_sifre == sifre ) :
    print ("Hatalı kullanıcı adı...")
elif ( sys_kullanici_adi != kullanici_adi and sys_sifre != sifre ) :
    print ("Hatalı şifre ve kullanıcı adı")
else :
    print ("Giriş başarılı.")
'''

a = int(input("Birinci sayıyı giriniz :"))
b = int(input("İkinci sayıyı giriniz :"))
c = int(input("Üçüncü sayıyı giriniz :"))

if (a >= b and a >= c):
    print(" En büyük sayı {} ' dır ".format(a))
elif (b >= a and b >= c):
    print("En büyük sayı {} ' dir ".format(b))
elif (c >= a and c >= b):
    print("En büyük sayı {} ' dir ".format(c))

