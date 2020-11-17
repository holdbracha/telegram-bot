from .mail_exception import MailException

class Mail():

    def __init__(self, mail_id = -1):
        self.mail_id = mail_id
        self.sender = None
        self.receiver = None
        self.date = None
        self.subject = None
        self.msg = None
        self.have_files = False
        self.files = []



    def update_mail(self, prop, value):
        self.__dict__[prop] = value

    def set_mail_data_from_json(self, json_data):
        if json_data["mail_id"] != self.mail_id:
            raise MailException("msg id is different from object mail", MailException.WRONG_MAIL_ID)

        self.sender = json_data.get("from")
        self.receiver = json_data.get("to")
        self.date = json_data.get("date")
        self.subject = json_data.get("subject")
        self.msg = json_data.get("textBody")

        try:
            self.files = [file["filename"] for file in json_data.get("attachments")]
            self.have_files = len(self.file) > 0
        except:
            self.have_files = False



def get_mail_from_dict(json_data):
    mail = Mail(json_data["mail_id"])
    mail.set_mail_data_from_json(json_data)
    return mail


mail = Mail()

action = {
    "action": "send",
    "subject": "kush",
    "add files":"yes",
    "last":"subject"
}




