from config import TOKEN
bot = telepot.Bot(TOKEN)

def get_file_from_user_to_mail(file_id, filename):
    # fileID = msg["document"]["thumb"]["file_id"]
    bot.download_file(file_id, filename)

def send_file_from_mail_to_user(filename, chat_id):
    # let the human know that the pdf is on its way
    bot.sendMessage(chat_id, "pls wait..")
    # send the pdf doc
    bot.sendDocument(chat_id=chat_id, document=open(filename, 'rb'))

def send_photo(chat_id):
    bot.sendChatAction(chat_id, 'upload_photo')
    bot.sendPhoto(chat_id, open('lighthouse.jpg', 'rb'))




