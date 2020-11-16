import smtplib, ssl
from .mail_exception import MailException

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

def send_mail(mail = None):
    try:
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "kadima1313@gmail.com"
        receiver_email = "sm5800810@gmail.com"
        password = "0527131328"
        message = """\
        Subject: Hi there
        
        This message is sent from Python."""

        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:

        raise MailException("error when send email", MailException.ERROR_SEND_MAIL)


    print('Email sent!')

send_mail(1)

