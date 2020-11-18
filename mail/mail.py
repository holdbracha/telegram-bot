from .mail_exception import MailException
from db_pkg.db_utils import get_curr_mail_address_by_chat_id

class Mail():
    def __init__(self, mail_id = -1, operation = "receive"):
        self.mail_id = mail_id
        self.sender = None
        if operation == "send":
            self.sender = get_curr_mail_address_by_chat_id(mail_id)

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


        self.sender = json_data.get("from", json_data.get("sender"))
        self.receiver = json_data.get("to", json_data.get("receiver"))
        self.date = json_data.get("date")
        self.subject = json_data.get("subject")
        self.msg = json_data.get("textBody", json_data.get("msg"))

        try:
            self.files = [file["filename"] for file in json_data.get("attachments")]
            self.have_files = len(self.file) > 0
        except:
            self.have_files = False





mail = Mail()

action = {
    "action": "send",
    "subject": "kush",
    "add files":"yes",
    "last":"subject"
}




