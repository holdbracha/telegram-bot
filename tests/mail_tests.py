import sys
sys.path.append('../')
from mail import *
from db_pkg import *
import server

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

def test_get_new_mails():
    temp_chat_id = 1434038438
    # sender_addr = get_new_mail_addr()
    # add_mail_address(temp_chat_id, sender_addr)
    # receiver_mail = get_new_mail_addr()
    # add_mail_address(temp_chat_id, receiver_mail)
    #
    # mail = Mail()
    # mail.update_mail("sender", sender_addr)
    # mail.update_mail("subject", "hello all")
    # mail.update_mail("msg", "this is the msg")
    # mail.update_mail("receiver", receiver_mail)
    # send_mail(mail)
    # receiver_mail = "exaar5f58z@1secmail.org"#"02zl36ogy7n@wwjmp.com"#"gd9kkvicamt@wwjmp.com"
    server.check_new_mails()
    # chat_id, num = get_mail_list_from_mail_addr(receiver_mail)
    # if num > 0:
    #     print(num, chat_id)
    # server.send_messages_to_user(chat_id)

