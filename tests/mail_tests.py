import sys
sys.path.append('../')
from mail import *
from db_pkg import *

def test_send_mail():
    mail = Mail()
    mail.update_mail("sender", "someone@gmail.com")
    mail.update_mail("subject", "hello all")
    mail.update_mail("msg", "this is the msg")
    mail.update_mail("receiver", "sm5800810@gmail.com")
    print(mail.__dict__)
    send_mail(mail)


def test_create_address():
    temp_chat_id = "11111"
    new_addr = get_new_mail_addr()

    print(new_addr)
    add_mail_address(temp_chat_id, new_addr)
    print("here")
    assert (get_mail_address_by_chat_id(temp_chat_id) == new_addr)
    assert (get_chat_id_by_mail_address(new_addr) == temp_chat_id)

# def test_get_
