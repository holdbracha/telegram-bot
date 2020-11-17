from mail.mail import *

class Sending:
    def __init__(self, chat_id = None, mail = None, next_action = None):
        self._id = chat_id
        self.mail = mail
        self.next_action = next_action

def get_sending_from_dict(sending_dict):
    s = Sending(sending_dict["_id"], get_mail_from_dict(sending_dict["mail"]), sending_dict["next_action"])
    return s