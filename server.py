from flask import Flask, Response, request
import requests
from config import *
from Message import *
from action import getAction
from sql_utils import add_message_to_db

app = Flask(__name__, static_url_path='', static_folder='dist')
req_action = None



menu_text = """ Select operation: 
    1 - is prime
    2 - is palindrome"""

# @app.route('/message', methods=["POST"])
# def handle_message():
#     req = request.get_json()
#     print("got message: ", req['message']['text'])
#     chat_id = req['message']['chat']['id']
#     res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
#                        .format(TOKEN, chat_id, req['message']['text']))
#     return Response("success")

@app.route('/message', methods=["POST"])
def handle_message():
    message = Message(request.get_json())
    if message.action is None:
        res_message = 'The message need to be <action> <value>'
    else:
        res_message = getAction(message.action, message.value)
        if message.action != '/popular':
            add_message_to_db(message)
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(TOKEN, message.chat_id, res_message))
    return Response("success")

if __name__ == '__main__':

    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=5200, debug=True)