from mail.mail import get_mail_from_dict
from config import MONGO_URL
import pymongo
from pymongo import MongoClient


from datetime import datetime #need to delete############################################################


cluster = MongoClient(MONGO_URL)
db = cluster["singular"]
sent_colection = db["sent"]
sending_colection = db["sending"]
recived_colection = db["recived"]
address_mail_colection = db["address_mail"]




def save_sent_mail(sent): #void func. get dict o sent. saving the email in sent table and deleting the mail from sending table.
    sent_colection.insert_one(sent)
    sending_colection.delete_one({"_id":sent["chat_id"]})

def save_sending_mail(sending): # chat id is primary key.
    if not sending_colection.find_one({"_id":sending["chat_id"]}):
        sending_colection.insert_one(sending)
    else:
        sending_colection.find_one_and_replace({"_id":sending["chat_id"]}, sending)
    sending_colection.insert_one(sending)

def save_recived_mail(recived): # if mail_primary_key is exit -> not saving. set is_readed = False
    result = True
    try:
        recived_colection.insert_one(recived)
    except pymongo.errors.DuplicateKeyError:
        result = False
    return result

def add_mail_address(chat_id, address):
    mail_address = {"_id":chat_id, "address":address}
    if not address_mail_colection.find_one(mail_address):
        address_mail_colection.insert_one(mail_address)
    else:
        address_mail_colection.find_one_and_update({"_id":chat_id}, {"$set":{"address":address}})



def get_all_sent_mails(chat_id): #return list of all sent mails of this user. return [] if there is no chat id that sent
    sents = sent_colection.find({"chat_id":chat_id})
    return list(sents)
    # result = []
    # for sent in sents:
    #     result.append(get_sent_from_dict(sent))
    # return result


def get_sending_mail(chat_id): # return sending object by chat id. return None if there is no chat id in sending
    return sending_colection.find_one({"_id":chat_id})
    # return get_sending_from_dict(res)
    


def get_all_recived_mails(chat_id): #return list of all recived mails of this user. return [] if there is no chat id that recived
    return list(recived_colection.find({"chat_id":chat_id}))


def get_all_recived_unreaded_mails(chat_id):
    return list(recived_colection.find({"chat_id":chat_id, "readed":False}))

def get_all_recived_readed_mails(chat_id):
    return list(recived_colection.find({"chat_id":chat_id, "readed":True}))

def mark_readed_mail(mail_primary_key): # set is_readed = True.
    recived_colection.find_one_and_update({"_id":mail_primary_key}, {"$set":{"readed":True}})

def get_chat_id_by_mail_address(mail_address):
    return address_mail_colection.find_one({"address":mail_address})["_id"]

def get_mail_address_by_chat_id(chat_id):
    return address_mail_colection.find_one({"_id":chat_id})["address"]

