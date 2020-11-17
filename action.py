from mail import *
from db_pkg import *
import datetime

#send_actions = ['get_receiver', 'get_subject', 'get_msg', 'is_include_files', 'get_file']
#send_actions_strings = ['Who is the recipient?', 'What the subject?', 'message?', 'want to add file?']
#send_function_per_action = [sara.set_receiver, sara.set_subject, sara.set_msg, None, sara.add_file]  #Sara's functions

# def add_handler(handler):
#     handlers[str(handler)] = handler

def create_temp_mail(chat_id):
    mail_address = get_new_mail_addr(chat_id)
    add_mail_address(chat_id, mail_address)
    return mail_address


def start_sending_proccess(chat_id):
    mail = Mail(chat_id)
    save_sending_mail(Sending(chat_id, mail, 'get_receiver'))
    return 'Who is the recipient?'


def get_receiver(params):
    params[1].update_mail('receiver', params[2])
    save_sending_mail(Sending(params[0], params[1], 'get_subject'))
    return 'What the subject?'


def get_subject(params):
    params[1].update_mail('subject', params[2])
    save_sending_mail(Sending(params[0], params[1], 'get_msg'))
    return 'message?'

def get_msg(params):
    params[1].update_mail('message', params[2])
    save_sending_mail(Sending(params[0], params[1], 'is_include_files'))
    return 'want to add a file?'

def is_include_files(params):
    if any(substring in params[2] for substring in ['no', 'not']):
        send_mail(params[1])
        return 'Your message sent successfully :)'
    #else
    save_sending_mail(Sending(params[0], params[1], 'get_file'))
    return 'please attach a file'

def get_file(params):
    params[1].update_mail('file', params[2])
    send_mail(params[1])
    save_sent_mail(Sent(params[0], params[1], str(datetime.datetime.now())))
    return 'Your message sent successfully :)'

def send_emails_to_user(chat_id):
    emails = get_all_recived_unreaded_mails(chat_id)
    res_list_messages = []
    for recived_mail in emails:
        mail = recived_mail.mail
        message = "You got a mail from: {}\nDate: {}\nSubject: {}\nMessage: {}".format(mail.sender, mail.date, mail.subject, mail.msg)
        res_list_messages.append(message)
        mark_readed_mail(mail._id)
    return res_list_messages

def non_action(chat_id):
    return "Don't understand. What do you want?"

handlers = {
    "createTempMail": create_temp_mail,
    "sendMail": start_sending_proccess,
    "get_receiver": get_receiver,
    "get_subject": get_subject,
    "get_msg": get_msg,
    "get_file": get_file,
    "send_emails_to_user": send_emails_to_user,
    "non_action": non_action
}
#
# index = send_actions.index(action)
#             if send_function_per_action[index] is not None:
#                 send_function_per_action[index](mail)
#             if (action == 'is_include_files' and ('no' in self.message or 'not' in self.message)) or index == len(send_actions) - 1:
#                 sara.send_mail(mail)
#             else:
#                 brachi.save_sending_mail(self.chat_id, mail, send_actions[index + 1])
#


def get_action(action, params):
    if action not in handlers.keys():
        return "invalid operation"
    return handlers[action](params)
