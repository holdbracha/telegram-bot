from flask import Flask, Response, request
import requests
from config import *
from message import *
from action import get_action
from mail import *

app = Flask(__name__, static_url_path='', static_folder='dist')
req_action = None

@app.route('/message', methods=["POST"])
def handle_message():
    print(request.get_json())
    message = Message(request.get_json())
    res_message = get_action(message.action, message.params)
    res = requests.get(TELEGRAM_RES.format(TOKEN, message.chat_id, res_message))
    return Response("success")

@app.route('/sendEmailsToUser/<chat_id>', methods=["GET"])
def send_messages_to_user(chat_id):
    res_messages = get_action('send_emails_to_user', chat_id)
    for message in res_messages:
        requests.get(TELEGRAM_RES.format(TOKEN, chat_id, message))
    return Response("success")

@app.route('/check_new_mails')
def check_new_mails(): #will calles every minute by cron job
    addresses = get_all_mail_address()
    for addr in addresses:
        chat_id, num_of_new_mails = get_mail_list_from_mail_addr(addr["address"])
        if num_of_new_mails > 0:
            res_messages = get_action('send_emails_to_user', chat_id)
            for message in res_messages:
                requests.get(TELEGRAM_RES.format(TOKEN, chat_id, message))
    return Response("success")


if __name__ == '__main__':
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)
    app.run(port=3000, threaded = True, debug=True)
