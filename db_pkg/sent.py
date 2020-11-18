try:
    from mail.mail_model import get_mail_from_dict
except:
    pass

class Sent:
    def __init__(self, chat_id = None, mail = None, time = None):
        self.chat_id = chat_id
        self.mail = mail
        self.time = time

def get_sent_from_dict(sent_dict):
    s = Sent(sent_dict["chat_id"], get_mail_from_dict(sent_dict["mail"]), sent_dict["time"])
    return s