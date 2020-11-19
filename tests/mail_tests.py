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
    mail.update_mail("receiver", "qhtpktw34fy@1secmail.net")
    print(mail.__dict__)
    send_mail(mail)


def test_create_address():
    temp_chat_id = 1390657756
    new_addr = get_new_mail_addr()

    print(new_addr)
    add_mail_address(temp_chat_id, new_addr)
    print("here")
    print (get_curr_mail_address_by_chat_id(temp_chat_id) , new_addr)
    print (get_chat_id_by_mail_address(new_addr) , temp_chat_id)

def test_get_new_mails_for_addr():
    temp_chat_id = 1390657756

    receiver_mail = "3qgb2xun8@esiix.com" #get_curr_mail_address_by_chat_id(temp_chat_id)#"exaar5f58z@1secmail.org"#"02zl36ogy7n@wwjmp.com"#"gd9kkvicamt@wwjmp.com"
    chat_id, num = get_mail_list_from_mail_addr(receiver_mail)
    if num > 0:
        print(num, chat_id)
    server.send_messages_to_user(chat_id)

def test_get_new_mails():
    server.check_new_mails()


def test_send_img():
    sendImageRemoteFile("")

