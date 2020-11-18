
TOKEN = '1401486158:AAHSWmn-go9jvblVARbpozB-OzaAM51zdJU'
NGROK_URL = 'https://11b2e1c686d2.ngrok.io'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TOKEN, NGROK_URL)
TELEGRAM_RES = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML"#&parse_mode=html"

MONGO_PASSWORD = "brachasaraor"
MONGO_DB = "singular"
MONGO_URL = "mongodb+srv://singulary:{}@user.itzww.mongodb.net/{}?retryWrites=true&w=majority".format(MONGO_PASSWORD, MONGO_DB)

USERNAME_MAIL = "AnonyMailBotTelegram@gmail.com"
PASSWORD_MAIL = "or1sara2brachi3" #heroku with @ in end

