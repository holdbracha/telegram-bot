import requests
from .mail import Mail
from .mail_exception import MailException
from .setting import TEMP_MAIL_URL_GET_ADDRESSES, TEMP_MAIL_URL_GET_MAIL_DATA, TEMP_MAIL_URL_GET_MAILS_LIST, TEMP_MAIL_URL_GET_MAIL_FILE
import datetime
from .send_mail import send_mail
from db_pkg import *


import sys
sys.path.append('../')



def get_new_mail_addr(count = 1):

    try:
        res = requests.get(TEMP_MAIL_URL_GET_ADDRESSES.format(count))
        print(res.json)
        return res.json()[0]

    except:
        raise MailException(f"error at creating random addresses", MailException.ERROR_FORMATTING_URL)



def get_mail_list_from_mail_addr(mail_addr):

    try:
        user, domain = tuple(mail_addr.split("@"))
        res = requests.get(TEMP_MAIL_URL_GET_MAILS_LIST.format(user, domain))
        print(res)
        i=-1
        for i, mail_data in enumerate(res):
            mail = Mail(mail_data["id"])
            get_mail_data(mail)

        delete_mail_list_was_saved(mail_data)
        return i

    except:
        raise MailException(f"error at get mail list of {mail_addr}", MailException.ERROR_FORMATTING_URL)



def get_mail_data(mail):

    try:
        user, domain = tuple(mail.sender.split("@"))
        res = requests.get(TEMP_MAIL_URL_GET_MAIL_DATA.format(user, domain, mail.mail_id))
        print(res)
        mail.set_mail_data_from_json(res)
        chat_id = get_chat_id_by_mail_address(mail.receiver)
        received_ob = Received(chat_id, mail, mail.date, mail.mail_id)
        save_recived_mail(received_ob)
        return mail

    except:
        raise MailException(f"error at get mail list of {mail.sender}", MailException.ERROR_FORMATTING_URL)


def delete_mail_list_was_saved(mail_addr):
    login, domain = tuple(mail_addr.split["@"])
    try:
        s = requests.Session()
        s.post('https://www.1secmail.com/mailbox/',
                    data={'action':"deleteMailbox",
                        'login':login,
                        'domain':domain
                        }
        )
    except:
        raise MailException("invalid address mail or error by deleting mails", MailException.WRONG_RECEIVER)

def get_mail_files(mail):

    try:
        user, domain = tuple(mail.sender.split("@"))
        for filename in mail.files:
            res = requests.get(TEMP_MAIL_URL_GET_MAIL_FILE.format(user, domain, mail.mail_id, filename))
            #TODO  handle files
            print(res)
        return "success"

    except:
        raise MailException(f"error at get mail list of {mail.sender}", MailException.ERROR_FORMATTING_URL)


def create_mail(chat_id):
    mail_addr = get_mail_address_by_chat_id(chat_id) #func from db
    mail = Mail()
    mail.update_mail("sender", mail_addr)
    return mail


def create_mail_by_params(receiver, subject, msg, files=None, sender = "new" ):
    new_mail =  Mail()

    if  sender == "new":
        sendr = get_new_mail_addr()[0]
    new_mail.sender = sender
    new_mail.date = datetime.datetime.now()
    new_mail.receiver = receiver
    new_mail.subject = subject
    new_mail.msg = msg

    try:
        new_mail.have_files = len(files) > 0
    except:
        # there is no files
        new_mail.have_files = False
    new_mail.files = files



def get_mail_from_dict(json_data):
    mail = Mail(json_data["mail_id"])
    mail.set_mail_data_from_json(json_data)
    return mail


def check_new_mails(): #will calles every minute by cron job
    addresses = get_all_mail_address()
    for addr in addresses:
        get_mail_list_from_mail_addr(addr["address"])




