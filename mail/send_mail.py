import smtplib, ssl
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import io
from config import USERNAME_MAIL, PASSWORD_MAIL
from .mail_exception import MailException

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = USERNAME_MAIL
password = PASSWORD_MAIL

# Create a secure SSL context
context = ssl.create_default_context()

def send_mail(mail = None):

    print(mail.sender)
    print(mail.msg)
    print(mail.subject)
    print(mail.receiver)
    # Try to log in to server and send email
    try:
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = mail.msg + f"\n please return answer to {mail.sender}"

        # setup the parameters of the message
        msg['From']= f"{mail.sender} <AnonyMailBotTelegram@gmail.com>"#str(Header('Magnus Eisengrim <meisen99@gmail.com>'))
        msg['To']= mail.receiver
        msg['Subject']=mail.subject

        # add in the message body
        msg.attach(MIMEText(message, 'html'))
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.send_message(msg)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
        raise MailException("error while sending mail: "+str(e), MailException.ERROR_SEND_MAIL)



def sendImage():
    url = "https://api.telegram.org/bot<Token>/sendPhoto";
    files = {'photo': open('/path/to/img.jpg', 'rb')}
    data = {'chat_id' : "YOUR_CHAT_ID"}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)

def sendImageRemoteFile(img_url):
    url = "https://api.telegram.org/bot<Token>/sendPhoto";
    remote_image = requests.get(img_url)
    photo = io.BytesIO(remote_image.content)
    photo.name = 'img.png'
    files = {'photo': photo}
    data = {'chat_id' : "YOUR_CHAT_ID"}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)
