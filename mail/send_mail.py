import smtplib, ssl

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

def send_mail(mail = None):

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("kadima9876@gmail.com", "0527131328")
        # TODO: Send email here

        # sent_from = "kadima9876@gmail.com"
        # to = ['sm5800810@gmail.com']
        # subject = 'pleaze call me- now'
        # body = 'i need you -send me'
        #
        # email_text = """\
        # From: %s
        # To: %s
        # Subject: %s
        #
        # %s
        # """ % (sent_from, ", ".join(to), subject, body)

        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.ehlo()
        # server.login(gmail_user, gmail_password)
        # server.sendmail(sent_from, to, email_text)
        # server.close()
        sender_email = "kadima9876@gmail.com"
        receiver_email = "sm5800810@gmail.com"
        message = """\
        Subject: Hi there
    
        This message is sent from Python."""
        server.sendmail(sender_email, receiver_email, message)

        # Send email here
        print('Email sent!')

# send_mail(1)


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kadima9876@gmail.com"
receiver_email = "sm5800810@gmail.com"
password = "0527131328"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
