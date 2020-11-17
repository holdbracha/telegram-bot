from db imoprt *

class Message:
    def __init__(self, data):
        self.message = data['message']['text'].lower()
        self.chat_id = data['message']['chat']['id']

        mail, action = db.get_sending_mail(self.chat_id)
        if action is not None: # the user in the middle of sending proccess
            #if action in send_actions: # maybe unecessary
            self.action = action
            self.params = (self.chat_id, mail, self.message)
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