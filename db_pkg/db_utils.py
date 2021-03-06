
from config import MONGO_URL
import pymongo
from pymongo import MongoClient
from .encrypted_key import *

from datetime import datetime #need to delete############################################################


cluster = MongoClient(MONGO_URL)
db = cluster["singular"]
sent_colection = db["sent"]
sending_colection = db["sending"]
recived_colection = db["recived"]
address_mail_colection = db["address_mail"]
black_list_colection = db["black_list"]
user_password_colection = db["user_password"]
keys_colection = db["keys"]
encrypted_key_per_url_colection = db["encrypted_key_per_url"]



def save_sent_mail(sent): #void func. get dict o sent. saving the email in sent table and deleting the mail from sending table.
    sent = sent.__dict__
    sent['mail'] = sent['mail'].__dict__
    sent_colection.insert_one(sent)
    sending_colection.delete_one({"_id":sent["chat_id"]})

def save_sending_mail(sending): # chat id is primary key.
    sending = sending.__dict__
    sending['mail'] = sending['mail'].__dict__
    if not sending_colection.find_one({"_id":sending["_id"]}):
        sending_colection.insert_one(sending)
    else:
        sending_colection.find_one_and_replace({"_id":sending["_id"]}, sending)
        #sending_colection.find_one_and_replace({"_id":sending["chat_id"]}, sending)


def save_recived_mail(recived): # if mail_primary_key is exit -> not saving. set is_readed = False
    try:
        recived.mail = recived.mail.__dict__
        recived_colection.insert_one(recived.__dict__)
        return True

    except pymongo.errors.DuplicateKeyError:
        return False

def add_mail_address(chat_id, address):
    mail_address = {"chat_id":chat_id, "address":address}
    if not address_mail_colection.find_one(mail_address):
        address_mail_colection.find_one_and_update({"current":True}, {"$set":{"current":False}})
        mail_address["current"] = True
        address_mail_colection.insert_one(mail_address)


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
    #return address_mail_colection.find_one({"address": mail_address})["_id"]
    addresses =  address_mail_colection.find_one({"address":mail_address})
    return str(addresses["chat_id"])


def get_all_mail_address_by_chat_id(chat_id):
    results = address_mail_colection.find({"chat_id":chat_id})
    result = []
    for res in results:
        result.append(res["address"])

def get_curr_mail_address_by_chat_id(chat_id):
    return address_mail_colection.find_one({"chat_id":chat_id, "current":True})["address"]

def get_all_mail_address():
    docs = address_mail_colection.find()
    return list(docs)

######Black List#######################################
def get_num_of_messages_between_times(chat_id, from_time):
    sent_list = list(sent_colection.find({"chat_id":chat_id}))
    sum = 0
    for s in sent_list:
        if s["time"] > from_time:
            sum += 1
    return sum

def add_user_to_black_list(chat_id):
    try:
        black_list_colection.insert_one({"_id":chat_id})
    except pymongo.errors.DuplicateKeyError:
        pass

def get_black_list():
    b_list = black_list_colection.find({})
    res = []
    for b in b_list:
        res.append(b["_id"])
    return res
def is_in_black_list(chat_id):
    if black_list_colection.find_one({"_id":chat_id}):
        return True
    return False

########encrypted password################################
def save_encrypted_key(encryptedKey):
    dict_encryptedKey = encryptedKey.__dict__
    if not user_password_colection.find_one({"chat_id":encryptedKey.chat_id}):
        user_password_colection.insert_one(dict_encryptedKey)
    else:
        user_password_colection.find_one_and_replace({"chat_id":encryptedKey.chat_id}, dict_encryptedKey)

def set_encrypted_key(encryptedKey):
    obj = keys_colection.find_one({"password":encryptedKey.password})
    if not obj:
        key = encryptedKey.create_key()
        keys_colection.insert_one({"password":encryptedKey.password, "key":key})
    else:
        key = obj.get("key")

    encrypted_key = encryptedKey.encrypted_key(key)
    try:
        encrypted_key_per_url_colection.insert_one({"url":encryptedKey.url, "nickname":encryptedKey.nickname, "encrypted_key":encrypted_key, "chat_id":encryptedKey.chat_id})
    except pymongo.errors.DuplicateKeyError:
        pass
    user_password_colection.delete_one({"chat_id":encryptedKey.chat_id})
    return key



def get_key(encryptedKey):
    encrypted_key = encrypted_key_per_url_colection.find_one({"url":encryptedKey.nickname, "chat_id":encryptedKey.chat_id})

    if not encrypted_key:
        list_encrypted_key = encrypted_key_per_url_colection.find({"chat_id":encryptedKey.chat_id})
        for e in list_encrypted_key:
            if encryptedKey.nickname in e["nickname"]:
                encrypted_key = e["encrypted_key"]
                break
    else:
        encrypted_key = encrypted_key.get("encrypted_key")
    if not encrypted_key:
        return None
    p = keys_colection.find_one({"password":encryptedKey.password})["key"]
    password = encryptedKey.get_key_by_decrypted(encrypted_key, p)
    user_password_colection.delete_one({"chat_id":encrypted_key.chat_id})
    return password

def get_encrypted_key(chat_id): # return sending object by chat id. return None if there is no chat id in sending
    return user_password_colection.find_one({"chat_id":chat_id})