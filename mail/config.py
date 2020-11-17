
SEND_MAIL_API_KEY = "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"

import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail, To

sg = sendgrid.SendGridAPIClient(
    api_key=SEND_MAIL_API_KEY#os.environ.get("SENDGRID_API_KEY")
)
from_email = Email("saraer@post.jce.ac.il")
to_email = To("sm5800810@gmail.com")
subject = "A test email from Sendgrid"
content = Content(
    "text/plain", "Here's a test email sent through Python"
)
mail = Mail(from_email, to_email, subject, content)
response = sg.send(mail)

# The statements below can be included for debugging purposes
print(response.status_code)
print(response.body)
print(response.headers)
