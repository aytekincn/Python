# Smtp modülü ile mail gönderme. Gmail Stmp serverine bağlanarak mail atma işlemi gerçekleştireceğiz.

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys

mesaj = MIMEMultipart

mesaj ["From"] = "aytekincan92@gmail.com"

mesaj ["To"] = "tekcancan9@gmail.com"

mesaj ["Subject"] = "Smtp Mail Gönderme"

yazi = """

Smtp ile mail gönderiyorum.
Aytekin Can


"""


mesaj_gövdesi = MIMEText( yazi, "plain" )

mesaj.attach( mesaj_gövdesi )

# Mesajlarımızın kimden geleceği, kime gideceği, başlığı, mesajı aytarladık ve mesaj gövdemizi oluşturduk.


try:
    mail = smtplib.SMTP("smtp.gmail.com", 587 ) # Hangi bağlantıyı kullanacağımızı giriyoruz.

    mail.ehlo() # smtp serverine bağlanıyoruz.
                                              # Bu iki fonksiyonu kullanmadığımız zaman mailimiz gönderilmeyecektir.
    mail.starttls() # Şifrelenmesi için kullanılan fonksiyon .

    mail.login("aytekincan92@gmail.com", "tekocan123")

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string() )

    print("Mail Başarıyla Gönderildi")
    mail.close()
except:
    sys.stderr.write("Bir Sorun Oluştu")
    sys.stderr.flush()




























