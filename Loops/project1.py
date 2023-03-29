print(""""
***************************
Kullanıcı girişi programı
***************************
      """)

sys_nick_name = "aytekincn"
sys_password = "123456"
giris_hakki = 3
while True :
    kullanici_adi = input("Kullanıcı adı : ")
    password = input("Parola : ")
    if ( kullanici_adi != sys_nick_name and password == sys_password ) :
        print("Geçersiz Kullanıcı Adı...")
        giris_hakki -= 1
        print("Giriş Hakkınız : ", giris_hakki)

    elif ( kullanici_adi == sys_nick_name and password != sys_password ) :
        print("Geçersiz Parola...")
        giris_hakki -= 1
        print("Giriş Hakkınız : " , giris_hakki )

    elif ( kullanici_adi != sys_nick_name and password != sys_password ) :
        print("Geçersiz Kullanıcı Adı ve Şifre....")
        giris_hakki -= 1
        print("Giriş Hakkınız : ", giris_hakki )

    else  :
        print("Giriş Başarılı")
        break

    if ( giris_hakki == 0 ) :
        print("Giriş Hakkınız Bitti....")
        break