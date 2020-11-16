from .mail_exception import MailException

class Mail():
    def __init__(mail, mail_id = -1):
        mail.mail_id = mail_id
        mail.sender = None
        mail.receiver = None
        mail.date = None
        mail.subject = None
        mail.msg = None
        mail.have_files = False
        mail.files = []






    def set_mail_data_from_json(mail, json_data):
        if json_data["id"] != mail.mail_id:
            raise MailException("msg id is diffrent from object mail", MailException.WRONG_MAIL_ID)

        mail.sender = json_data.get("from")
        mail.receiver = json_data.get("to")
        mail.date = json_data.get("date")
        mail.subject = json_data.get("subject")
        mail.msg = json_data.get("textBody")

        try:
            mail.files = [file["filename"] for file in json_data.get("attachments")]
            mail.have_files = len(mail.file) > 0
        except:
            mail.have_files = False









