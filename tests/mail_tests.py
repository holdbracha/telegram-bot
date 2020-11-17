import sys
sys.path.append('../')
from mail import *

def test_send_mail():
    mail = Mail()
    mail.update_mail("sender", "someone@gmail.com")
    mail.update_mail("subject", "hello all")
    mail.update_mail("msg", "this is the msg")
    mail.update_mail("receiver", "sm5800810@gmail.com")
    print(mail.__dict__)
    send_mail(mail)

test_send_mail()
