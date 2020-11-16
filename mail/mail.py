from .mail_exception import MailException

class Mail():
    def __init__(mail, json_data ):
        mail.mail_id = json_data["id"]
        mail.sender = json_data["from"]
        mail.receiver = json_data["to"]
        mail.date = json_data["date"]
        mail.subject = json_data["subject"]
        mail.set_mail_data_from_json(json_data)


    def set_mail_data_from_json(mail, json_data):
        if json_data["id"] != mail.mail_id:
            raise MailException("msg id is diffrent from object mail", MailException.WRONG_MAIL_ID)

            mail.msg = json_data["textBody"]
            try:
                mail.files = [file["filename"] for file in json_data["attachments"]]
                mail.have_files = len(mail.file) > 0
            except:
                mail.have_files = False





    #maybe have to transfer to model ?????????? @TODO
    def send_mail(mail):
        pass


