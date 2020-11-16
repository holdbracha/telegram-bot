
class MailException(Exception):
    NONE_SENDER = 1
    NONE_RECEIVER = 2
    NONE_MAIL_ID = 3

    WRONG_SENDER = 1
    WRONG_RECEIVER = 2
    WRONG_MAIL_ID = 3

    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
