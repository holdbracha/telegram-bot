
import smtplib, ssl

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'kadima9876@gmail.com'
PASSWORD = '0527131328'

def get_contacts():
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = ["sara"]
    emails = ["sm5800810@gmail.com"]

    return names, emails

def read_template():
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    return Template("""Dear ${PERSON_NAME},\n\n
                    This is a test message. 
                    Have a great weekend! \n\n
                    Yours Truly""")

def send_mail():
    names, emails = get_contacts() #"sm5800810", "sm5800810@gmail.com"
    message_template = read_template()


    port = 465  # For SSL

    # Create a secure SSL context
    # context = ssl.create_default_context()
    #
    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as s:
    #     # s.login("kadima9876@gmail.com", "0527131328")

        # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']="kadima1313@gmail.com"
        msg['To']=email
        msg['Subject']="This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        #     s.send_message(msg)
        try:
           smtpObj = smtplib.SMTP('localhost')
           smtpObj.send_message(msg)
           print("Successfully sent email")
        except Exception as e:
           print("Error: unable to send email", e)
        del msg

    # # Terminate the SMTP session and close the connection
    # s.quit()

if __name__ == '__main__':
    send_mail()
