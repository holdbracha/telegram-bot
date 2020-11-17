
SEND_GRID_API_KEY = "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"

USERNAME_MAIL = "AnonyMailBotTelegram@gmail.com"
PASSWORD_MAIL = "or1sara2brachi3"

API_KEY_ELASTIC_MAIL = "C4821E049C341CF20B3FA900582018D0DE1B35239BEDE03BD6C77C2D8A3022D26DDBF0E3DD6314CF048C4C0BB1F97292"



from ElasticEmailClient import ApiClient, Email, Contact

ApiClient.apiKey = API_KEY_ELASTIC_MAIL

contacts = []
contacts.append("test1@test.com")
contactResponse = Contact.QuickAdd(contacts)

print (contactResponse)

subject = 'Your subject'
fromEmail = 'sm5800810@gmail.com'
fromName = 'sara'
bodyText = 'Text body'
bodyHtml = '<h1>Hello, {username}.</h1>'
files = { 'C://Users//IBM Thinkpad//Documents//study//startup//cou//hakaton-bot//singularly-master//mail//mail.py' }
filenameWithRecipients = 'mail.py' # same as the file above

emailResponse = Email.Send(subject, fromEmail, fromName, to="sm5800810@gmail.com",  bodyText = bodyText, bodyHtml = bodyHtml)#, attachmentFiles = files, mergeSourceFilename = filenameWithRecipients)


try:
    print ('MsgID to store locally: ', emailResponse['messageid'], end='\n') # Available only if sent to a single recipient
    print ('TransactionID to store locally: ', emailResponse['transactionid'])
except TypeError:
    print ('Server returned an error: ', emailResponse)
