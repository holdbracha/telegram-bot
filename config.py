
TOKEN = '1401486158:AAHSWmn-go9jvblVARbpozB-OzaAM51zdJU'
NGROK_URL = 'https://80f38f061f76.ngrok.io'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TOKEN, NGROK_URL)
TELEGRAM_RES = "https://api.telegram.org/bot{}/sendMessage?parse_mode=HTML&chat_id={}&text={}"#&parse_mode=html"

MONGO_PASSWORD = "brachasaraor"
MONGO_DB = "singular"
MONGO_URL = "mongodb+srv://singulary:{}@user.itzww.mongodb.net/{}?retryWrites=true&w=majority".format(MONGO_PASSWORD, MONGO_DB)

USERNAME_MAIL = "AnonyMailBotTelegram@gmail.com"
PASSWORD_MAIL = "or1sara2brachi3" #heroku with @ in end


firebaseConfig = {
"apiKey": "AIzaSyB3lmYn1aPAXaMR_7pOj4SMDQdOS_4Nx5c",
"authDomain": "anonymailbot-d3247.firebaseapp.com",
"databaseURL": "https://anonymailbot-d3247.firebaseio.com",
"projectId": "anonymailbot-d3247",
"storageBucket": "anonymailbot-d3247.appspot.com",
"messagingSenderId": "77512838602",
"appId": "1:77512838602:web:ac0fc9300307006e9b9333",
"measurementId": "G-PHJX0J0KR6"
}

