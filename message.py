from db_pkg import *

suspicious_words = [' kill ', ' wait for you ', ' hurt ']

class Message:
    def __init__(self, data):
        if data.get('edited_message'):
            return False
        self.message = data['message']['text'].lower()
        self.chat_id = data['message']['chat']['id']

        sending = get_sending_mail(self.chat_id)
        if any(substring in self.message for substring in suspicious_words):
            self.action = 'suspicious_message'
            self.params = self.chat_id
        elif sending is not None: # the user in the middle of sending proccess
            #if action in send_actions: # maybe unecessary
            sending = get_sending_from_dict(sending)
            self.action = sending.next_action
            self.params = (self.chat_id, sending.mail, self.message)
        elif any(substring in self.message for substring in ['create', 'open', 'new']):
            self.action = 'createTempMail'
            self.params = self.chat_id
        elif 'send' in self.message:
            self.action = 'start_sending_proccess'
            self.params = self.chat_id
        else:
            self.action = 'non_action'
            self.params = self.chat_id


        #self.value = self.message.split(' ')[1]