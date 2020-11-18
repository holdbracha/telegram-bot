try:
    from mail.mail_model import get_mail_from_dict
except:
    pass

class Recived:
    def __init__(self, chat_id = None, mail = None, time = None, mail_primary_key = None, readed = False):
        self._id = mail_primary_key
        self.chat_id = chat_id
        self.mail = mail
        self.time = time
        self.readed = False


def get_recived_from_dict(recived_dict):
    r = Recived(recived_dict["chat_id"], get_mail_from_dict(recived_dict["mail"]), recived_dict["time"], recived_dict["_id"], recived_dict["readed"])
    return r
