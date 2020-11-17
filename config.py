
TOKEN = '1401486158:AAHSWmn-go9jvblVARbpozB-OzaAM51zdJU'
NGROK_URL = 'https://3083c26366c4.ngrok.io'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TOKEN, NGROK_URL)
TELEGRAM_RES = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"

MONGO_PASSWORD = "brachasaraor"
MONGO_DB = "singular"
MONGO_URL = "mongodb+srv://singulary:{}@user.itzww.mongodb.net/{}?retryWrites=true&w=majority".format(MONGO_PASSWORD, MONGO_DB)

