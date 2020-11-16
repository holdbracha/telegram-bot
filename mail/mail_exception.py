
class MailException(Exception):
    NONE_SENDER = 1
    NONE_RECEIVER = 2
    NONE_MAIL_ID = 3

    WRONG_SENDER = 4
    WRONG_RECEIVER = 5
    WRONG_MAIL_ID = 6

    ERROR_SEND_MAIL = 7
    ERROR_FORMATTING_URL = 8


    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
