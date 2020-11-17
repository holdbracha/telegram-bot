
TOKEN = '1488507077:AAFpw8rUhzo6InUcCs1Uf-z9nxZFIuzngLc'
NGROK_URL = 'https://9e75ba55e77e.ngrok.io'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TOKEN, NGROK_URL)
TELEGRAM_RES = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN)

MONGO_PASSWORD = "brachasaraor"
MONGO_DB = "singular"
MONGO_URL = "mongodb+srv://singulary:{}@user.itzww.mongodb.net/{}?retryWrites=true&w=majority".format(MONGO_PASSWORD, MONGO_DB)

