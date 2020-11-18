
try:
    from db_pkg import *
except:
    pass
try:
    from mail import *
except:
    pass
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
    half_hour_ago = str(datetime.datetime.now() - datetime.timedelta(minutes=30))
    mails_count = get_num_of_messages_between_times(chat_id, half_hour_ago)
    print("mails count" + str(mails_count))
    if mails_count >= 5:
        add_user_to_black_list(chat_id)
        return 'You sent a suspicious amount of emails during the last period. You are blocked!'
    mail = Mail(chat_id, operation = 'send')
    save_sending_mail(Sending(chat_id, mail, 'get_receiver'))
    return 'Who is the recipient?'


def get_receiver(params):
    params[1].update_mail('receiver', params[2])
    save_sending_mail(Sending(params[0], params[1], 'get_subject'))
    return 'What is the subject?'


def get_subject(params):
    params[1].update_mail('subject', params[2])
    save_sending_mail(Sending(params[0], params[1], 'get_msg'))
    return 'message?'

def get_msg(params):
    params[1].update_mail('msg', params[2])
    save_sending_mail(Sending(params[0], params[1], 'is_include_files'))
    return 'Do you want to add a file?'

def is_include_files(params):
    #print('mail--------------------------------:' + params[1].__dict__)
    if any(substring in params[2] for substring in ['no', 'not']):
        send_mail(params[1])
        save_sent_mail(Sent(params[0], params[1], str(datetime.datetime.now())))
        return 'Your message sent successfully :)'
    #else
    save_sending_mail(Sending(params[0], params[1], 'get_file'))
    return 'please attach a file'

def get_file(params):
    #TODO - check how to update
    params[1].update_mail('files', params[2])
    send_mail(params[1])
    save_sent_mail(Sent(params[0], params[1], str(datetime.datetime.now())))
    return 'Your message sent successfully :)'

def send_emails_to_user(chat_id):
    emails = get_all_recived_unreaded_mails(chat_id)
    res_list_messages = []
    for recived_mail in emails:
        # mail = recived_mail.mail
        # message = "You got a mail from: {}\nDate: {}\nSubject: {}\nMessage:\n{}".format(mail.sender, mail.date, mail.subject, mail.msg)
        mail = get_mail_from_dict(recived_mail["mail"])
        message = "You got a mail from: {}\nDate: {}\nSubject: {}\nMessage: {}".format(mail.sender, mail.date, mail.subject, mail.msg)

        res_list_messages.append(message)
        mark_readed_mail(mail.mail_id)
    return res_list_messages

def start_password_proccess(chat_id):
    save_encrypted_key(EncryptedKey(chat_id, next_action = 'get_url'))
    return 'Please write the URL of the website that you want a password for it'

def get_url(params):
    params[1].update_encrypted_key('_id', params[2])
    params[1].update_encrypted_key('next_action', 'get_nickname')
    save_encrypted_key(params[1])
    return 'Give nick name for the website'

def get_nickname(params):
    params[1].update_encrypted_key('nickname', params[2])
    params[1].update_encrypted_key('next_action', 'get_fixed_password_and_save')
    save_encrypted_key(params[1])
    return 'press your fixed password for that service'

def get_fixed_password_and_save(params):
    params[1].update_encrypted_key('next_action', 'get_fixed_password')
    password = set_encrypted_key(params[1])
    return "Your password save successfully :)"

def suspicious_message(chat_id):
    # add to black list
    add_user_to_black_list(chat_id)
    return "We are recognized suspicious words in your message. You are blocked!"

def non_action(chat_id):
    return "Don't understand. What do you want?"

handlers = {
    "suspicious_message": suspicious_message,
    "createTempMail": create_temp_mail,
    "start_sending_proccess": start_sending_proccess,
    "get_receiver": get_receiver,
    "get_subject": get_subject,
    "get_msg": get_msg,
    "is_include_files": is_include_files,
    "get_file": get_file,
    "send_emails_to_user": send_emails_to_user,
    "start_password_proccess": start_password_proccess,
    "get_url": get_url,
    "get_nickname": get_nickname,
    "get_fixed_password_and_save": get_fixed_password_and_save,
    "non_action": non_action
}

def get_action(action, params):
    if action not in handlers.keys():
        return "invalid operation"
    return handlers[action](params)
